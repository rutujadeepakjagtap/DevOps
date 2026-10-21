# Main Infrastructure Declaration: Security Group & EC2 Instance
# DevOps Assignment 03: Infrastructure as Code (IaC)

# Fetch latest Amazon Linux 2023 AMI via AWS Systems Manager Parameter Store
data "aws_ssm_parameter" "amazon_linux_2023" {
  name = "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
}

# Author dedicated Security Group for Web and SSH Traffic
resource "aws_security_group" "web_server_sg" {
  name        = "terraform-web-server-sg"
  description = "Allow inbound SSH and HTTP web traffic for DevOps Lab"

  ingress {
    description = "SSH administrative access"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP web application traffic"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "terraform-web-sg"
  }
}

# Provision Amazon EC2 Instance
resource "aws_instance" "web_server" {
  ami                    = data.aws_ssm_parameter.amazon_linux_2023.value
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.web_server_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              dnf update -y
              dnf install -y nginx
              systemctl enable --now nginx
              echo "<h1>Provisioned with Terraform IaC - Rutuja Jagtap (123B1B146)</h1>" > /usr/share/nginx/html/index.html
              EOF

  tags = {
    Name = var.instance_name
  }
}
