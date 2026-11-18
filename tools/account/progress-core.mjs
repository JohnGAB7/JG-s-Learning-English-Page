/**
 * Pure progress primitives. item_id values must be stable catalogue IDs
 * (e.g. lesson:a1-001, studio:<activity_id>, speak:<topic-id>-<level>),
 * never page URLs. The database trigger mirrors the monotonic completion rule.
 */
const VALID_STATUSES = new Set(["started","completed"]);
const ITEM_ID = /^(lesson|studio|speak|review):[a-z0-9][a-z0-9._:-]*$/;
export function normalizeProgress(record) {
  if (!record || typeof record !== "object") throw new TypeError("A progress record must be an object.");
  const {item_id:itemId,status,updated_at:updatedAt}=record;
  if(typeof itemId!=="string"||!ITEM_ID.test(itemId)) throw new TypeError("Invalid progress item_id.");
  if(!VALID_STATUSES.has(status)) throw new TypeError("Invalid progress status.");
  const date=updatedAt==null?new Date(0):new Date(updatedAt);
  if(Number.isNaN(date.getTime())) throw new TypeError("Invalid progress updated_at.");
  return {item_id:itemId,status,updated_at:date.toISOString()};
}
export function mergeProgress(...collections) {
  const merged=new Map();
  for(const collection of collections) {
    if(!Array.isArray(collection)) throw new TypeError("Each progress collection must be an array.");
    for(const raw of collection) {
      const next=normalizeProgress(raw), current=merged.get(next.item_id);
      if(!current){merged.set(next.item_id,next);continue;}
      merged.set(next.item_id,{item_id:next.item_id,status:current.status==="completed"||next.status==="completed"?"completed":"started",updated_at:new Date(Math.max(Date.parse(current.updated_at),Date.parse(next.updated_at))).toISOString()});
    }
  }
  return [...merged.values()].sort((a,b)=>a.item_id.localeCompare(b.item_id));
}
export function countCompleted(records){return records.reduce((n,r)=>n+(r.status==="completed"?1:0),0);}
