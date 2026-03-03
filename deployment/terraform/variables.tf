variable "kubeconfig_path" {
  description = "Path to kubeconfig file."
  type        = string
  default     = "~/.kube/config"
}

variable "kube_context" {
  description = "Kubernetes context name to use from kubeconfig."
  type        = string
  default     = null
}

variable "namespace" {
  description = "Namespace where the Helm release will be deployed."
  type        = string
  default     = "theme-park"
}

variable "release_name" {
  description = "Helm release name."
  type        = string
  default     = "theme-park-ride"
}

variable "environment" {
  description = "Target environment value. Expected: dev or prod."
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "prod"], var.environment)
    error_message = "environment must be either 'dev' or 'prod'."
  }
}
