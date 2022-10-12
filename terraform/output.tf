output "elb-dns-name" {
  value = aws_lb.aplication-lb.dns_name
}

output "instance_ip_addr" {
  value       = aws_instance.cisco.*.public_ip
  description = "The private IP address of the main server instance."
}
