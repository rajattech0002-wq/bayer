terraform {
  required_version = ">= 1.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Example resource - replace with your actual infrastructure
resource "null_resource" "example" {
  triggers = {
    message = "Terraform configuration is working!"
  }
}

output "message" {
  value = null_resource.example.triggers.message
}
