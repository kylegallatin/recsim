variable "cloud_provider" {
  description = "The cloud provider to use (aws, gcp, azure)"
  type        = string
}

module "aws" {
  source    = "./cloud_providers/aws"
  count     = var.cloud_provider == "aws" ? 1 : 0
  # ... Pass necessary variables
}

module "gcp" {
  source    = "./cloud_providers/gcp"
  count     = var.cloud_provider == "gcp" ? 1 : 0
  # ... Pass necessary variables
}

# ... Similarly for other providers
