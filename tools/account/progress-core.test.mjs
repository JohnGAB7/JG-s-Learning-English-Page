import test from "node:test";
import assert from "node:assert/strict";
import { countCompleted, mergeProgress, normalizeProgress } from "./progress-core.mjs";
import { createLocalProgressStore } from "./progress-store.mjs";

const row = (item_id, status, updated_at) => ({ item_id, status, updated_at });

test("union preserves records present on either device", () => {
  const result = mergeProgress(
    [row("lesson:a1-001", "started", "2026-01-01T00:00:00Z")],
    [row("studio:listening-a2-041", "completed", "2026-01-02T00:00:00Z")]
  );
  assert.equal(result.length, 2);
});

test("completed wins even when the started record is newer", () => {
  const result = mergeProgress(
    [row("lesson:a1-001", "completed", "2026-01-01T00:00:00Z")],
    [row("lesson:a1-001", "started", "2026-02-01T00:00:00Z")]
  );
  assert.deepEqual(result, [
    row("lesson:a1-001", "completed", "2026-02-01T00:00:00.000Z")
  ]);
});

test("latest timestamp wins independently of status", () => {
  const result = mergeProgress(
    [row("lesson:a1-001", "started", "2026-01-02T00:00:00Z")],
    [row("lesson:a1-001", "started", "2026-01-03T00:00:00Z")]
  );
  assert.equal(result[0].updated_at, "2026-01-03T00:00:00.000Z");
});

test("merge is idempotent and deterministic", () => {
  const source = [row("lesson:a1-002", "completed", "2026-01-01T00:00:00Z")];
  assert.deepEqual(mergeProgress(source, source), mergeProgress(source));
});

test("rejects unknown identifiers and statuses", () => {
  assert.throws(() => normalizeProgress(row("profile:email", "started", null)));
  assert.throws(() => normalizeProgress(row("lesson:a1-001", "skipped", null)));
});

test("counts completed items only", () => {
  assert.equal(countCompleted([
    row("lesson:a1-001", "completed", null),
    row("lesson:a1-002", "started", null)
  ]), 1);
});

test("local store writes first and reads back normalized progress", async () => {
  const data = new Map();
  const storage = {
    getItem: key => data.get(key) ?? null,
    setItem: (key, value) => data.set(key, value)
  };
  const store = createLocalProgressStore(storage);
  await store.upsert(row("lesson:a1-001", "completed", "2026-01-01T00:00:00Z"));
  assert.equal((await store.list())[0].status, "completed");
});
