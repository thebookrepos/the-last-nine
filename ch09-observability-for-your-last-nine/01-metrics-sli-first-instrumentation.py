from prometheus_client import Counter, Histogram
import time

REQS = Counter("http_requests_total", "requests",
               ["route", "method", "code"])
LAT = Histogram("http_request_duration_seconds", "latency",
                ["route", "method"],
                buckets=(.025, .05, .1, .25, .5, 1, 2, 5))
                # buckets bracket the SLO thresholds: 0.5
                # and 2.0 must be edges, or the SLI can't be
                # computed from this data

def middleware(handler):
    def wrapped(req):
        start = time.monotonic()
        try:
            resp = handler(req)
            code = resp.status
        except Exception:
            code = 500
            raise
        finally:
            # "/orders/{id}", never the raw path: cardinality
            route = req.route_template
            REQS.labels(route, req.method, str(code)).inc()
            elapsed = time.monotonic() - start
            LAT.labels(route, req.method).observe(elapsed)
        return resp
    return wrapped
