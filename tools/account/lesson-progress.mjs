/**
 * Opens the canonical local progress store and migrates the former lesson-only
 * object format once. The legacy key is deliberately retained as a recovery copy.
 */
import { createLocalProgressStore } from "./progress-store.mjs";

const CANONICAL_KEY = "jg-learning-progress-v1";
const LEGACY_LESSON_KEY = "jg-lesson-progress-v1";
const LESSON_ID = /^(a1|a2|b1|b2|c1)-\d{3}$/;

export async function openLessonProgressStore(storage = globalThis.localStorage) {
  const store = createLocalProgressStore(storage, CANONICAL_KEY);
  await store.list();
  if (store.getStatus().state !== "local") return store;

  // A present canonical key, even an empty array, is authoritative.
  if (storage.getItem(CANONICAL_KEY) !== null) return store;

  const legacyRaw = storage.getItem(LEGACY_LESSON_KEY);
  if (legacyRaw === null) return store;

  const legacy = JSON.parse(legacyRaw);
  if (!legacy || typeof legacy !== "object" || Array.isArray(legacy))
    throw new TypeError("Legacy lesson progress has an invalid shape.");

  const records = [];
  for (const [id, value] of Object.entries(legacy)) {
    if (!LESSON_ID.test(id) || !value || value.completed !== true) continue;
    const parsedDate = new Date(value.completedAt);
    records.push({
      item_id: "lesson:" + id,
      status: "completed",
      // Epoch denotes an older completion whose timestamp was not recoverable.
      updated_at: Number.isNaN(parsedDate.getTime()) ? new Date(0).toISOString() : parsedDate.toISOString()
    });
  }

  if (records.length) await store.merge(records);
  return store;
}
