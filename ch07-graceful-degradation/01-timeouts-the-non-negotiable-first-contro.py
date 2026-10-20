import time, requests

DEADLINE_HEADER = "x-request-deadline"   # unix epoch seconds

def remaining(req) -> float:
    default = time.time() + 2.0
    deadline = float(req.headers.get(DEADLINE_HEADER,
                                     default))
    return deadline - time.time()

def call_downstream(req, url, floor=0.05, ceiling=1.0):
    # reserve 50ms to respond
    budget = min(remaining(req) - 0.05, ceiling)
    if budget < floor:
        raise DeadlineExceeded(
            "no time left; fail before wasting work")
    return requests.get(
        url,
        timeout=budget,
        headers={DEADLINE_HEADER: str(time.time() + budget)},
    )
