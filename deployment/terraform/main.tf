terraform {
  required_version = ">= 1.5.0"

  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.30"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.14"
    }
  }
}

provider "kubernetes" {
  config_path    = var.kubeconfig_path
  config_context = var.kube_context
}

provider "helm" {
  kubernetes {
    config_path    = var.kubeconfig_path
    config_context = var.kube_context
  }
}

resource "kubernetes_namespace" "theme_park" {
  metadata {
    name = var.namespace

    labels = {
      "app.kubernetes.io/name"       = "theme-park-ride"
      "app.kubernetes.io/managed-by" = "terraform"
      "environment"                  = var.environment
    }
  }
}

resource "helm_release" "theme_park_ride" {
  name             = var.release_name
  chart            = "../charts/theme-park-ride"
  namespace        = kubernetes_namespace.theme_park.metadata[0].name
  create_namespace = false

  values = [
    file("../charts/theme-park-ride/values.yaml"),
    file("../charts/theme-park-ride/values-${var.environment}.yaml")
  ]

  depends_on = [kubernetes_namespace.theme_park]
}
