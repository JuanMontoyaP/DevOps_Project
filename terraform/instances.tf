resource "aws_instance" "cisco" {
  count = var.number_instances

  ami             = var.ami_id
  instance_type   = var.instace_type
  key_name        = "us-west-key"
  security_groups = ["${aws_security_group.sg-cisco.name}"]

  tags = {
    "Name" : "cisco_demo"
  }
}