-- The outage: one migration, atomic in the worst sense.
ALTER TABLE orders RENAME COLUMN state TO status;
-- Every instance of the current code errors on the
-- next query.

-- Expand (deploy 1): additive only, both code versions valid
ALTER TABLE orders ADD COLUMN status TEXT;     -- nullable
CREATE INDEX CONCURRENTLY idx_orders_status ON orders(status);

-- Migrate (deploy 2): code dual-writes state+status, reads
-- status with fallback to state; backfill runs throttled in
-- the background
UPDATE orders SET status = state
WHERE status IS NULL AND id BETWEEN :lo AND :hi; -- batched

-- Contract (deploy 3, weeks later, after verification):
-- the point of no return, taken only when metrics prove
-- no reader remains
ALTER TABLE orders DROP COLUMN state;
