/**
 * Storage contract for learner progress.
 *
 * The application writes locally first. A future authenticated adapter may sync
 * the same records to the account, but must never make learning depend on the API.
 * Writing drafts are intentionally outside this contract.
 */
import { mergeProgress, normalizeProgress } from "./progress-core.mjs";

export function createLocalProgressStore(storage, key = "jg-learning-progress-v1") {
  if (!storage || typeof storage.getItem !== "function" ||
      typeof storage.setItem !== "function") {
    throw new TypeError("A Web Storage-compatible object is required.");
  }

  function read() {
    const raw = storage.getItem(key);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    if (!Array.isArray(parsed)) throw new TypeError("Stored progress must be an array.");
    return mergeProgress(parsed);
  }

  function write(records) {
    const normalized = mergeProgress(records);
    storage.setItem(key, JSON.stringify(normalized));
    return normalized;
  }

  return Object.freeze({
    mode: "local",
    async list() {
      return read();
    },
    async upsert(record) {
      return write(mergeProgress(read(), [normalizeProgress(record)]));
    },
    async merge(records) {
      return write(mergeProgress(read(), records));
    }
  });
}

/**
 * Future remote adapter contract:
 * { mode: "account", list(): Promise<Progress[]>,
 *   upsert(record): Promise<Progress>, merge(records): Promise<Progress[]> }
 * Remote failures must be caught by the application boundary, not hidden here,
 * so the UI can accurately report local-only vs account-synced persistence.
 */
