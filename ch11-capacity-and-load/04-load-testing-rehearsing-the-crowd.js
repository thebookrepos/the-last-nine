// k6: the spike scenario, checkout journey, criticality
// tags included
import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  scenarios: {
    spike: {
      executor: "ramping-arrival-rate",
      startRate: 200, timeUnit: "1s",
      preAllocatedVUs: 2000,
      stages: [
        // baseline
        { target: 200, duration: "5m" },
        // the spike: 4.5x in under a minute
        { target: 900, duration: "45s" },
        // hold past autoscaler lag
        { target: 900, duration: "10m" },
        // release: watch the herd
        { target: 200, duration: "30s" },
        // recovery observation
        { target: 200, duration: "10m" },
      ],
    },
  },
  thresholds: {
    // The test's SLOs mirror production's: tier-1 must hold
    "http_req_duration{tier:critical}": ["p(99)<2000"],
    "http_req_failed{tier:critical}":   ["rate<0.001"],
    // Sheddable traffic is EXPECTED to fail during the spike:
    // its 503 rate is the shedding working, and asserting
    // it low would fail the test for succeeding.
  },
};

export default function () {
  const res = http.post(
    "https://staging.example.com/v1/checkout",
    JSON.stringify({ cart: "synthetic-t-77" }),
    { headers: { "x-criticality": "critical",
                 "x-synthetic": "loadtest" },
      tags: { tier: "critical" } });
  check(res, {
    "2xx or shed": (r) => r.status < 500 || r.status === 503,
  });
  sleep(0.1);
}
