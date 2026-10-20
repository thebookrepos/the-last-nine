resource "aws_route53_health_check" "region_a_checkout" {
  fqdn              = "a.checkout.example.com"
  type              = "HTTPS"
  # the path exercises the whole journey
  resource_path     = "/synthetic/checkout"
  failure_threshold = 3
  request_interval  = 10    # seconds
  measure_latency   = true
}

resource "aws_route53_record" "checkout_a" {
  zone_id         = var.zone_id
  name            = "checkout.example.com"
  type            = "A"
  set_identifier  = "region-a"
  failover_routing_policy { type = "PRIMARY" }
  health_check_id = (
    aws_route53_health_check.region_a_checkout.id
  )
  alias {
    name                   = var.region_a_lb
    zone_id                = var.region_a_lb_zone
    evaluate_target_health = true
  }
  ttl = 60
}
# SECONDARY record for region B mirrors the above,
# minus the health check
