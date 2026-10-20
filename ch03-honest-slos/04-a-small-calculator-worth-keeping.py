#!/usr/bin/env python3
"""Error budget arithmetic for a request-based SLO."""

def budget(slo_pct: float, window_days: int, rps: float):
    error_frac = 1 - slo_pct / 100
    total = rps * 86400 * window_days
    allowed = total * error_frac
    full_outage_min = window_days * 1440 * error_frac
    return allowed, full_outage_min

def incident_cost(rps: float, error_rate: float,
                  minutes: float, allowed: float) -> float:
    failed = rps * error_rate * minutes * 60
    return failed / allowed * 100

if __name__ == "__main__":
    allowed, outage_min = budget(slo_pct=99.9, window_days=28,
                                 rps=2000)
    print(f"Budget: {allowed:,.0f} failed requests "
          f"({outage_min:.1f} min full-outage equivalent)")

    # A deploy failing 30% of traffic for 12 minutes:
    pct = incident_cost(rps=2000, error_rate=0.30, minutes=12,
                        allowed=allowed)
    print(f"That incident spent {pct:.1f}% "
          f"of the 28-day budget")
