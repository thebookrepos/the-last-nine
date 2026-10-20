-- The ledger path: overlap guaranteed
-- (LOCAL_QUORUM both ways, N=3)
CONSISTENCY LOCAL_QUORUM;
INSERT INTO payments.ledger (account, txn_id, amount, at)
VALUES ('a-1029', 8f3e..., 129.00, toTimestamp(now()));

SELECT balance FROM payments.balances
WHERE account = 'a-1029';          -- also at LOCAL_QUORUM

-- The activity feed: availability chosen on purpose
CONSISTENCY ONE;
INSERT INTO activity.events (user, at, kind)
VALUES ('a-1029', now(), 'login');
