class PriorityShedder:
    """Admission control by criticality tier under
    concurrency pressure."""
    LIMITS = {"critical": 1.00, "normal": 0.80,
              "sheddable": 0.60}
    # a tier is admitted only while
    # in-flight < limit * max_concurrency

    def __init__(self, max_concurrency: int):
        self.max = max_concurrency
        self.in_flight = 0

    def admit(self, tier: str) -> bool:
        frac = self.in_flight / self.max
        if frac >= self.LIMITS.get(tier, 0.6):
            return False     # fast 503 + Retry-After
        self.in_flight += 1
        return True

    def done(self):
        self.in_flight -= 1
