#!/usr/bin/env python3
"""Availability arithmetic.

Serial chains and parallel replicas."""

def serial(*avail):
    """Request must traverse all components."""
    a = 1.0
    for x in avail:
        a *= x
    return a

def parallel(a_component: float, n: int,
             ceiling: float = 1.0):
    """Any one of n independent replicas suffices.
    'ceiling' models correlated failure the replicas share."""
    a = 1 - (1 - a_component) ** n
    return min(a, ceiling)

if __name__ == "__main__":
    # Checkout path: edge -> app fleet -> db -> vendor
    edge  = parallel(0.999,  2)    # dual DNS/LB
    # shared deploys cap the fleet
    app   = parallel(0.995,  6, ceiling=0.9999)
    db    = 0.9995                 # primary + auto failover
    payv  = 0.999                  # single vendor
    total = serial(edge, app, db, payv)
    print(f"Journey ceiling: {total:.5%}")   # -> ~99.84%
