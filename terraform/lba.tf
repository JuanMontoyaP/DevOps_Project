resource "aws_lb_target_group" "target-group" {
  health_check {
    interval            = 10
    path                = "/"
    protocol            = var.tg_protocol
    timeout             = 5
    healthy_threshold   = 5
    unhealthy_threshold = 2
  }

  name        = var.tg_name
  port        = var.tg_port
  protocol    = var.tg_protocol
  target_type = var.tg_target_type
  vpc_id      = data.aws_vpc.default.id
}

resource "aws_lb" "aplication-lb" {
  name               = var.lb_name
  internal           = false
  ip_address_type    = "ipv4"
  load_balancer_type = var.lb_type
  security_groups    = [aws_security_group.sg-cisco.id]
  subnets            = data.aws_subnet_ids.subnet.ids

  tags = {
    Name = var.lb_name
  }
}

resource "aws_lb_listener" "alb-listener" {
  load_balancer_arn = aws_lb.aplication-lb.arn
  port              = var.tg_port
  protocol          = var.tg_protocol
  default_action {
    target_group_arn = aws_lb_target_group.target-group.arn
    type             = "forward"
  }
}

resource "aws_lb_target_group_attachment" "ec2_attach" {
  count            = length(aws_instance.cisco)
  target_group_arn = aws_lb_target_group.target-group.arn
  target_id        = aws_instance.cisco[count.index].id
}