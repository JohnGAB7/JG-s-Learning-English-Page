import test from "node:test";
import assert from "node:assert/strict";
import { countCompleted, mergeProgress, normalizeProgress } from "./progress-core.mjs";
import { createLocalProgressStore } from "./progress-store.mjs";
const row = (item_id, status, updated_at) => ({ item_id, status, updated_at });

test("union preserves records from both devices", () => {
  assert.equal(mergeProgress([row("lesson:a1-001","started","2026-01-01Z")],[row("studio:listening-a2-041","completed","2026-01-02Z")]).length,2);
});
test("completed wins over a newer started state", () => {
  const result=mergeProgress([row("lesson:a1-001","completed","2026-01-01T00:00:00Z")],[row("lesson:a1-001","started","2026-02-01T00:00:00Z")]);
  assert.equal(result[0].status,"completed"); assert.equal(result[0].updated_at,"2026-02-01T00:00:00.000Z");
});
test("latest timestamp wins for same status", () => {
  assert.equal(mergeProgress([row("lesson:a1-001","started","2026-01-02T00:00:00Z")],[row("lesson:a1-001","started","2026-01-03T00:00:00Z")])[0].updated_at,"2026-01-03T00:00:00.000Z");
});
test("merge is idempotent", () => { const x=[row("lesson:a1-002","completed","2026-01-01T00:00:00Z")]; assert.deepEqual(mergeProgress(x,x),mergeProgress(x)); });
test("rejects invalid IDs and statuses", () => { assert.throws(()=>normalizeProgress(row("profile:email","started",null))); assert.throws(()=>normalizeProgress(row("lesson:a1-001","skipped",null))); });
test("counts completed only", () => { assert.equal(countCompleted([row("lesson:a1-001","completed",null),row("lesson:a1-002","started",null)]),1); });
test("local store persists and reads normalized progress", async()=>{ const data=new Map(); const s=createLocalProgressStore({getItem:k=>data.get(k)??null,setItem:(k,v)=>data.set(k,v)}); await s.upsert(row("lesson:a1-001","completed","2026-01-01T00:00:00Z")); assert.equal((await s.list())[0].status,"completed"); });
test("corrupt JSON degrades without crashing and blocks writes",async()=>{const s=createLocalProgressStore({getItem:()=>"{bad",setItem:()=>{}}); assert.deepEqual(await s.list(),[]); assert.deepEqual(s.getStatus(),{state:"degraded",detail:"corrupt-json"}); await assert.rejects(s.upsert(row("lesson:a1-001","started",null)));});
test("getItem throwing degrades and blocks writes",async()=>{const s=createLocalProgressStore({getItem:()=>{throw Error("blocked")},setItem:()=>{}}); assert.deepEqual(await s.list(),[]); assert.deepEqual(s.getStatus(),{state:"degraded",detail:"storage-unavailable"}); await assert.rejects(s.upsert(row("lesson:a1-001","started",null)));});
test("setItem quota error rejects and reports session-only",async()=>{const s=createLocalProgressStore({getItem:()=>null,setItem:()=>{throw Error("quota exceeded")}}); await assert.rejects(s.upsert(row("lesson:a1-001","started",null)),/quota exceeded/); assert.deepEqual(s.getStatus(),{state:"session-only",detail:"storage-write-failed"});});
test("invalid stored item IDs are skipped while valid rows survive",async()=>{const data=[row("lesson:a1-001","completed","2026-01-01T00:00:00Z"),row("profile:email","started","2026-01-02T00:00:00Z")]; const s=createLocalProgressStore({getItem:()=>JSON.stringify(data),setItem:()=>{}}); assert.deepEqual(await s.list(),[row("lesson:a1-001","completed","2026-01-01T00:00:00.000Z")]); assert.deepEqual(s.getStatus(),{state:"degraded",detail:"invalid-records-skipped"});});
