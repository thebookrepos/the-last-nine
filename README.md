# The Last Nine: Companion Repository

Code, configuration, templates and worksheets for **The Last Nine: How Many Nines Can You Really Afford? A Site Reliability Engineering Guide to What You Really Need and How to Get There** by Hemant Sharma.

The book prints every listing. Long lines wrap on the printed page. The copies here keep each line whole so you can copy and run them.

## What is here

| Folder | Listings |
|---|---|
| [Chapter 1: What 99.999% Actually Means](ch01-what-99-999-actually-means/) | none |
| [Chapter 2: The Cost Curve](ch02-the-cost-curve/) | none |
| [Chapter 3: Honest SLOs](ch03-honest-slos/) | 4 |
| [Chapter 4: Eliminating Single Points of Failure](ch04-eliminating-single-points-of-failure/) | 2 |
| [Chapter 5: Multi-Region and Disaster Recovery](ch05-multi-region-and-disaster-recovery/) | 4 |
| [Chapter 6: Data Layer Availability](ch06-data-layer-availability/) | 2 |
| [Chapter 7: Graceful Degradation](ch07-graceful-degradation/) | 4 |
| [Chapter 8: Change Is the Number One Killer](ch08-change-is-the-number-one-killer/) | 4 |
| [Chapter 9: Observability for Your Last Nine](ch09-observability-for-your-last-nine/) | 3 |
| [Chapter 10: Incident Command](ch10-incident-command/) | 2 |
| [Chapter 11: Capacity and Load](ch11-capacity-and-load/) | 4 |
| [Chapter 12: Chaos Engineering](ch12-chaos-engineering/) | 4 |
| [Chapter 13: Drills That Actually Fail Over](ch13-drills-that-actually-fail-over/) | 2 |
| [Chapter 14: Dependency Risk](ch14-dependency-risk/) | 2 |
| [Chapter 15: On-Call That Scales](ch15-on-call-that-scales/) | 3 |
| [Chapter 16: Blameless Postmortems and the Learning Loop](ch16-blameless-postmortems/) | 2 |
| [Chapter 17: The Field Checklist](ch17-the-field-checklist/) | none |
| [Appendix A: Availability Math Cheat Sheet](appA-availability-math-cheat-sheet/) | 2 |
| [Appendix B: Incident Command Runbook Template](appB-incident-command-runbook-template/) | 2 |
| [Appendix C: The SLO Worksheet](appC-the-slo-worksheet/) | 2 |

Each listing file starts with its number in the chapter and the section it comes from. Each folder has a README that maps files to sections.

## Versions

Examples target Kubernetes 1.30 or later, Prometheus 2 or 3, PostgreSQL with Patroni and etcd 3, Envoy and Argo Rollouts. Load and fault tests use k6, Toxiproxy and Linux tc/netem. The Appendix A calculator needs Python 3.10 or later and no extra packages:

```
python3 appA-availability-math-cheat-sheet/02-the-cheat-sheet-as-code.py
```

When a newer release changes a flag name or default, the listing here gets updated and the change goes in [CHANGELOG.md](CHANGELOG.md).

Two JSON listings carry inline comments, as they do in the book. They use the `.jsonc` extension. Remove the comments before you feed them to a strict JSON parser.

## Report errata or ask a question

Open an [issue](../../issues/new/choose). Pick the template that fits:

- **Erratum**: a mistake in the book or a listing. Include the page number and edition (paperback, Kindle or other).
- **Question**: something in the book is unclear.
- **Version update**: a tool release broke or changed a listing.

Confirmed errata are listed in [ERRATA.md](ERRATA.md) and fixed in the next printing.

## Contribute

Pull requests are welcome. Good contributions include:

- Fixes for listings that break on a newer tool version
- Ports of a listing to another stack (for example, a Datadog version of a Prometheus rule)
- Worked examples from your own SLOs, drills or postmortems, with private details removed

See [CONTRIBUTING.md](CONTRIBUTING.md) before you open a pull request.

## License

The code and configuration in this repository are released under the [MIT License](LICENSE). The book text is not covered by this license and remains under copyright.

If the book helped you, a short review on Amazon helps other engineers find it.
