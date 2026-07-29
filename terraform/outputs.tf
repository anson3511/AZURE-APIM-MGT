output "function_app_name" {
  description = "Name of the Function App"
  value       = azurerm_linux_function_app.function_app.name
}

output "function_app_hostname" {
  description = "Default hostname of the Function App"
  value       = azurerm_linux_function_app.function_app.default_hostname
}

output "function_app_url" {
  description = "Base URL of the Function App"
  value       = "https://${azurerm_linux_function_app.function_app.default_hostname}"
}