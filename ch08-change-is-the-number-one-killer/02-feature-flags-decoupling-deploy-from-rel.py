# The kill-switch pattern: fails static, defaults safe,
# one-line shed
flags = FlagClient(
    # async refresh; never in the request path
    refresh_interval=30,
    # survives a flag-service outage
    local_cache="/var/run/flags",
    # compiled-in last resort, chosen for safety
    defaults={
        "fraud.use_ml_scoring": False,  # conservative path
        "recs.enabled": True,
    },
)

def score_transaction(txn):
    # kill switch: the incident commander can force False
    if flags.get("fraud.use_ml_scoring"):
        return ml_score(txn)
    return rules_score(txn)             # degrade path
