#!/usr/bin/env python3
"""The Last Nine appendix calculator.

The availability math in one file."""
import math

MIN_YEAR = 525_600

def downtime(slo, minutes=MIN_YEAR):
    return minutes * (1 - slo)    # minutes of allowed down

def serial(*a):
    out = 1.0
    for x in a: out *= x
    return out

def parallel(a, n, ceiling=1.0):
    return min(1 - (1 - a) ** n, ceiling)

def budget_events(slo, window_days, rps):
    return rps * 86_400 * window_days * (1 - slo)

def incident_cost(rps, err, secs, slo, window_days):
    allowed = budget_events(slo, window_days, rps)
    return rps * err * secs / allowed

def burn_rate(err_fraction, slo):
    return err_fraction / (1 - slo)

def littles(rps, latency_s, burst=1.5, util=0.7):
    return math.ceil(rps * latency_s * burst / util)

def quorum_tolerance(n):
    return (n - 1) // 2

if __name__ == "__main__":
    # Expected output: 5.26, 0.99950, 0.9999, 8.9%, 643
    print(f"{downtime(0.99999):.2f} min/yr at five nines")
    print(f"{serial(*[0.9999]*5):.5f} ceiling, 5x four-nines")
    print(f"{parallel(0.99, 2):.4f} from two 99% replicas")
    print(f"{incident_cost(2000, .3, 720, .999, 28):.1%} "
          f"of budget for the 12-min 30% incident")
    print(f"pool {littles(2000, 0.15)}")
