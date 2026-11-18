# Supabase R&D lab — setup and review notes

**Status:** preparation only. This document describes the isolated ChatGPT R&D project; it is not a production configuration.

## Project identity

- Organization: `JG'S Learning English Lab`
- Project: `jg-s-learning-english-lab`
- Project ref: `crrbycpwheatongsbpdv`
- Region: `eu-central-1` (Frankfurt)
- Plan: Free
- PostgreSQL: 17.11
- Observed state on 2026-11-15: project healthy, no application tables in `public`, no recorded migrations, no Edge Functions.

Do not use Claude's separate `jg-learning-english-eu` project for this R&D work.

## Migration in this branch

`supabase/migrations/20261115000100_create_progress.sql`

Creates one minimal `public.progress` table with:

- composite primary key `(user_id, item_id)`;
- FK to `auth.users(id)` with delete cascade;
- stable content IDs, not page URLs;
- only `started` and `completed` states;
- per-user RLS policy for authenticated users;
- monotonic completion and non-decreasing timestamps;
- a 5,000-item per-user cap that permits an UPSERT of an existing item at the cap;
- trigger functions declared `SECURITY INVOKER`, with default PUBLIC execution revoked after trigger creation.

The migration is prepared in GitHub only. It has **not** been applied to Supabase.

## Important platform checks before applying

### Data API exposure

Supabase announced that new tables in the `public` schema are no longer exposed to the Data API by default, with enforcement across projects from 2026-10-30. This project was created after that date.

Therefore, SQL grants and RLS alone do not prove that the table is reachable through the browser client. Before enabling remote sync, explicitly verify the Data API's exposed-schema/table configuration for this project and expose only what the application needs.

Reference: https://supabase.com/changelog/breaking-change-new-tables-not-exposed-by-default

### Existing automatic-RLS event trigger

The initial read-only inspection found:

- event trigger `ensure_rls`, enabled for `ddl_command_end`;
- function `public.rls_auto_enable()`, owned by `postgres`;
- function is `SECURITY DEFINER` and fixes `search_path` to `pg_catalog`;
- EXECUTE is granted to `PUBLIC`, inherited by `anon` and `authenticated`;
- its body enables RLS on newly created tables in `public`.

Supabase's own RLS guide documents an automatic-RLS event-trigger pattern with a SECURITY DEFINER function. The security advisor still flags broad EXECUTE grants on SECURITY DEFINER functions. Because this is an event-trigger function rather than an ordinary RPC function, do not assume the finding proves that a client can invoke it through PostgREST.

Do not alter this existing trigger as part of the progress-table migration. Review its provenance and test any privilege hardening in an isolated environment before changing it.

References:
- https://supabase.com/docs/guides/database/postgres/row-level-security
- https://supabase.com/docs/guides/database/functions

### Auth configuration

Auth settings were not available through the connected read-only inspection. Before enabling account creation, verify in the Supabase Dashboard:

- email sign-up and email-confirmation behavior;
- allowed redirect URLs for the actual R&D site;
- SMTP deliverability and sender identity;
- session lifetime and sign-out behavior;
- account deletion and session-revocation flow.

Do not enable the account CTA in the learner-facing product until the complete flow and privacy notice are reviewed.

## Verification plan before remote sync

1. Apply the reviewed migration only to this isolated lab project, after explicit approval.
2. Re-read table definition, grants, RLS state and policies.
3. Test anonymous access is denied.
4. Test user A cannot read, update or delete user B's rows.
5. Test a user can insert and update their own progress.
6. Test an UPSERT of an existing item succeeds when that user already has 5,000 rows.
7. Test insertion of a 5,001st distinct item is rejected.
8. Test `completed` cannot regress to `started`, and `updated_at` cannot move backwards.
9. Re-run Supabase security and performance advisors.
10. Verify Data API exposure and a real authenticated client request.

## Explicit non-goals for this stage

- No Auth configuration changes.
- No account deletion endpoint or Edge Function.
- No remote synchronization or frontend credentials.
- No production data, no Claude Supabase changes.
- No migration has been applied and no deployment has occurred.
