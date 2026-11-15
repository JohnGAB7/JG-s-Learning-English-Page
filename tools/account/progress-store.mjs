/**
 * Local-first progress storage. list() returns recoverable records; getStatus()
 * exposes degraded reads. Failed writes are rethrown so callers show session-only.
 * A failed read blocks writes in this instance to avoid destructive overwrites.
 * Writing drafts are deliberately outside this store.
 */
import { mergeProgress, normalizeProgress } from "./progress-core.mjs";
export function createLocalProgressStore(storage, key = "jg-learning-progress-v1") {
  if (!storage || typeof storage.getItem !== "function" || typeof storage.setItem !== "function")
    throw new TypeError("A Web Storage-compatible object is required.");
  let state = "local", detail = null;
  function read() {
    let raw;
    try { raw = storage.getItem(key); }
    catch { state = "degraded"; detail = "storage-unavailable"; return []; }
    if (!raw) return [];
    let parsed;
    try { parsed = JSON.parse(raw); }
    catch { state = "degraded"; detail = "corrupt-json"; return []; }
    if (!Array.isArray(parsed)) { state = "degraded"; detail = "invalid-storage-shape"; return []; }
    const valid = []; let skipped = 0;
    for (const record of parsed) {
      try { valid.push(normalizeProgress(record)); }
      catch { skipped += 1; }
    }
    if (skipped) { state = "degraded"; detail = "invalid-records-skipped"; }
    return mergeProgress(valid);
  }
  function write(records) {
    if (state === "degraded") throw new Error("Local progress could not be read; refusing a potentially destructive write.");
    const normalized = mergeProgress(records);
    try { storage.setItem(key, JSON.stringify(normalized)); }
    catch (error) { state = "session-only"; detail = "storage-write-failed"; throw error; }
    return normalized;
  }
  return Object.freeze({
    mode: "local",
    async list() { return read(); },
    getStatus() { return Object.freeze({ state, detail }); },
    async upsert(record) { const current = read(); return write(mergeProgress(current, [normalizeProgress(record)])); },
    async merge(records) { const current = read(); return write(mergeProgress(current, records)); }
  });
}
