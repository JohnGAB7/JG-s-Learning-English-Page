-- JG's Learning English — learner progress foundation
-- Apply only after John creates and reviews the Supabase project.
create table if not exists public.progress (
  user_id uuid not null references auth.users (id) on delete cascade,
  item_id text not null check (length(item_id) between 1 and 180 and item_id ~ '^(lesson|studio|speak|review):[a-z0-9][a-z0-9._:-]*$'),
  status text not null check (status in ('started', 'completed')),
  updated_at timestamptz not null default now(),
  constraint progress_user_item_pk primary key (user_id, item_id)
);
alter table public.progress enable row level security;
drop policy if exists "Learners manage their own progress" on public.progress;
create policy "Learners manage their own progress" on public.progress for all to authenticated
  using ((select auth.uid()) = user_id) with check ((select auth.uid()) = user_id);
revoke all on table public.progress from anon;
grant select, insert, update, delete on table public.progress to authenticated;

-- Completed is monotonic at database level. Reset is DELETE; without tombstones,
-- another device may reintroduce a deleted row. A reset_at design is deferred.
create or replace function public.progress_keep_completed() returns trigger
language plpgsql set search_path = '' as $$
begin
  if tg_op = 'UPDATE' then
    if old.status = 'completed' then new.status := 'completed'; end if;
    new.updated_at := greatest(old.updated_at, new.updated_at);
  end if;
  return new;
end;
$$;
drop trigger if exists progress_keep_completed_trigger on public.progress;
create trigger progress_keep_completed_trigger before update on public.progress
for each row execute function public.progress_keep_completed();

-- Per-user Free-tier guardrail. Advisory lock serializes concurrent inserts.
create or replace function public.progress_limit_rows_per_user() returns trigger
language plpgsql security definer set search_path = '' as $$
declare current_count bigint;
begin
  perform pg_catalog.pg_advisory_xact_lock(pg_catalog.hashtextextended(new.user_id::text, 0));
  select count(*) into current_count from public.progress where user_id = new.user_id;
  if current_count >= 5000 then
    raise exception 'Progress limit reached (5000 items per learner).' using errcode = '54000';
  end if;
  return new;
end;
$$;
drop trigger if exists progress_limit_rows_per_user_trigger on public.progress;
create trigger progress_limit_rows_per_user_trigger before insert on public.progress
for each row execute function public.progress_limit_rows_per_user();
comment on table public.progress is 'Minimal learner progress only. Maximum 5000 rows per learner; no profile data or writing drafts.';
comment on column public.progress.item_id is 'Stable catalogue ID, never a page URL.';
