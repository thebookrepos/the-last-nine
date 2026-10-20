import random, time

class RetryBudget:
    """Token bucket: retries may spend up to 10% of
    recent request volume."""
    def __init__(self, ratio=0.1, capacity=100):
        self.tokens = capacity
        self.capacity, self.ratio = capacity, ratio
    def on_request(self):
        self.tokens = min(self.capacity,
                          self.tokens + self.ratio)
    def try_spend(self) -> bool:
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False      # budget gone: no retry, fail fast

def call_with_retry(fn, budget, attempts=3, base=0.05,
                    cap=1.0):
    for attempt in range(attempts):
        try:
            return fn()
        except TransientError:
            last = attempt == attempts - 1
            if last or not budget.try_spend():
                raise
            backoff = min(cap, base * 2 ** attempt)
            time.sleep(random.uniform(0, backoff))
