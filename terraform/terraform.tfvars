# Instance variables
number_instances = 1
ami_id           = "ami-09208e69ff3feb1db"
instace_type     = "t2.micro"

# Security groups variables
sg_name = "lb-sg-cisco"
sg_ingress_rules = [
  {
    description = "Access to port 80 from the exterior",
    from_port   = 80,
    to_port     = 80,
    protocol    = "tcp",
    cidr_blocks = ["0.0.0.0/0"]
  },
  {
    description = "Access to port 22 from the exterior",
    from_port   = 22,
    to_port     = 22,
    protocol    = "tcp",
    cidr_blocks = ["0.0.0.0/0"]
  }
]
sg_egress_rules = [
  {
    description = "Access to port 8080 from the exterior",
    from_port   = 0,
    to_port     = 0,
    protocol    = -1,
    cidr_blocks = ["0.0.0.0/0"]
  }
]

# Target group
tg_name        = "cisco-tg"
tg_port        = 80
tg_protocol    = "HTTP"
tg_target_type = "instance"

# Load balancer variables
lb_name = "cisco-alb"
lb_type = "application"