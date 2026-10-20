# tc/netem on one replica's interface: 150ms +/- 40ms
# latency, 1% loss. Tests ch 6's claims: does replication
# lag alert (ch 5's RPO rule)? Does the lease hold or
# falsely fail over (ch 6's failover clock)?
tc qdisc add dev eth0 root netem delay 150ms 40ms loss 1%

# The abort is the removal, pre-staged in the same runbook:
tc qdisc del dev eth0 root
