output "container_registry_name" {
  description = "Azure container registry name"
  value       = module.acr.container_registry_name
}

output "acr_rg" {
  description = "Azure container registry RG"
  value       = module.acr.acr_rg
}

output "acr_login_server" {
  description = "The URL that can be used to log into the container registry"
  value       = module.acr.acr_login_server
}

output "acr_admin_enabled" {
  description = "Admin user is enabled for acr or not"
  value       = module.acr.acr_admin_enabled
}

output "acr_admin_username" {
  description = "Username associated with the Container Registry Admin account - if the admin account is enabled"
  value       = module.acr.acr_admin_username
}

output "acr_admin_password" {
  description = " Password associated with the Container Registry Admin account - if the admin account is enabled"
  value       = nonsensitive(module.acr.acr_admin_password)
  sensitive   = false
}

output "acr_anonymous_pull_enabled" {
  description = "Anonymous pull is enabled on ACR or not"
  value       = module.acr.acr_anonymous_pull_enabled
}