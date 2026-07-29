variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
}

variable "location" {
  description = "Azure region for the resources"
  type        = string
  default     = "Canada Central"
}

variable "storage_account_name" {
  description = "Globally unique storage account name"
  type        = string
}

variable "function_app_name" {
  description = "Globally unique Function App name"
  type        = string
}