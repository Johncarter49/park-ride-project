output "namespace" {
  description = "Namespace used for deployment."
  value       = kubernetes_namespace.theme_park.metadata[0].name
}

output "helm_release" {
  description = "Installed Helm release name."
  value       = helm_release.theme_park_ride.name
}

output "chart_version" {
  description = "Chart version applied by Helm."
  value       = helm_release.theme_park_ride.version
}
