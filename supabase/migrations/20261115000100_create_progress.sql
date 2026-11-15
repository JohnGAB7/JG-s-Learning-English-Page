-- JG's Learning English — learner progress foundation
-- Apply only after John creates and reviews the Supabase project.
-- No project credentials or production connection are part of this migration.

create table if not exists public.progress (
  user_id uuid not null references auth.users (id) on delete cascade,
  item_id text not null check (
    length(item_id) between 1 and 180
    and item_id ~ '^(lesson|studio|speak|review):[a-z0-9][a-z0-9._:-]*$'
  ),
  status text not null check (status in ('started', 'completed')),
  updated_at timestamptz not null default now(),
  constraint progress_user_item_pk primary key (user_id, item_id)
);

alter table public.progress enable row level security;

-- A learner can only read or mutate rows whose owner is the authenticated user.
-- RLS is the security boundary; client-side filtering is never sufficient.
drop policy if exists "Learners manage their own progress" on public.progress;
create policy "Learners manage their own progress"
  on public.progress
  for all
  to authenticated
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

revoke all on table public.progress from anon;
grant select, insert, update, delete on table public.progress to authenticated;

comment on table public.progress is
  'Minimal learner progress only. No names, profile fields, writing drafts, or lesson content.';
comment on column public.progress.item_id is
  'Stable content identifier, e.g. lesson:a1-001 or studio:listening-a2-041.';
