# Output Values for Provisioned Infrastructure
# DevOps Assignment 03: Infrastructure as Code (IaC)

output "instance_id" {
  description = "Unique AWS resource identifier for the EC2 instance"
  value       = aws_instance.web_server.id
}

output "instance_public_ip" {
  description = "Public IPv4 address of the EC2 instance"
  value       = aws_instance.web_server.public_ip
}

output "instance_public_dns" {
  description = "Public DNS hostname of the EC2 instance"
  value       = aws_instance.web_server.public_dns
}

output "security_group_id" {
  description = "Identifier of the created security group"
  value       = aws_security_group.web_server_sg.id
}
