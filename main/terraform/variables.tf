variable "credentials" {
  description = "Project Creds"
  default     = file("/workspaces/DataCamp2024/main/terraform/keys/my-creds.json")
}

variable "project" {
  description = "Project Name"
  default     = "datacamp2024-412820"
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "Storage Bucket Name"
  default     = "datacamp2024-412820-terrabucket"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"
}