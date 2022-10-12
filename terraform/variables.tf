# Instance variables

variable "number_instances" {
  description = "Number of instances to build"
  type        = number
}

variable "ami_id" {
  description = "AMI ID of the image to be created"
  type        = string
}

variable "instace_type" {
  description = "Instace type of the image to be created"
  type        = string
}

# Security Group Variables
variable "sg_name" {
  description = "Security Group name"
  type        = string
}

variable "sg_ingress_rules" {
  description = "Security Group ingress rules"
  type        = list(any)
}

variable "sg_egress_rules" {
  description = "Security Group egress rules"
  type        = list(any)
}

# Target Group Variables
variable "tg_name" {
  description = "Target group name"
  type        = string
}

variable "tg_port" {
  description = "Port of the target group"
  type        = number
}

variable "tg_protocol" {
  description = "Protocol of the target group"
  type        = string
}

variable "tg_target_type" {
  description = "Target type of the target group"
  type        = string
}

# Load Balancer Variables
variable "lb_name" {
  description = "Name of the load balancer application"
  type        = string
}

variable "lb_type" {
  description = "Load balancer type"
  type        = string
}