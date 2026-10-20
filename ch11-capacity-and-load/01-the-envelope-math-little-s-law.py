#!/usr/bin/env python3
"""Little's Law envelope math for the checkout path."""

def concurrency(rps: float, latency_s: float) -> float:
    return rps * latency_s                   # L = lambda x W

def pool_size(rps: float, latency_s: float,
              burst: float = 1.5,
              util_target: float = 0.7) -> int:
    """Size a bounded pool: expected concurrency, bursted,
    landed below the knee."""
    need = concurrency(rps, latency_s) * burst / util_target
    return int(need + 0.5)

if __name__ == "__main__":
    # Normal day
    print(pool_size(rps=2000, latency_s=0.150))     # -> 643
    # Fraud API browning out to 700ms timeouts:
    print(concurrency(2000, 0.700))       # -> 1400 in flight
    # The 6x sale at healthy latency:
    print(pool_size(rps=12000, latency_s=0.150))   # -> 3857
