resource "azurerm_resource_group" "acr_rg" {
  name     = "myResourceGroup"
  location = "centralIndia"
  tags = {
    Environment     = "DEV"
    Orchestrator    = "Terraform"
    DisplayName     = "MYRESOURCEGROUP"
    ApplicationName = "devwithkrishna"
    Temporary       = "TRUE"
  }
}

resource "azurerm_container_registry" "acr" {
  name                = "myContwainerxdeXgi00y"
  resource_group_name = azurerm_resource_group.acr_rg.name
  location            = azurerm_resource_group.acr_rg.location
  sku                 = "Premium"

  georeplications {

      location                = "SouthIndia"
      zone_redundancy_enabled = false
      tags = {
        Environment     = "DEV"
        Orchestrator    = "Terraform"
        DisplayName     = "replication-MYCONTWAINERXDEXGI00Y"
        ApplicationName = "devwithkrishna"
        Temporary       = "TRUE"
      }

  }
  georeplications {

      location                = "eastus2"
      zone_redundancy_enabled = true
      tags = {
        Environment     = "DEV"
        Orchestrator    = "Terraform"
        DisplayName     = "replication-MYCONTWAINERXDEXGI00Y"
        ApplicationName = "devwithkrishna"
        Temporary       = "TRUE"
      }

  }

  retention_policy_in_days      = 37
  public_network_access_enabled = true
  quarantine_policy_enabled     = true
  zone_redundancy_enabled       = true
  admin_enabled                 = true
  anonymous_pull_enabled        = true
  data_endpoint_enabled         = true
  trust_policy_enabled          = true

  network_rule_bypass_option = "None"
  tags = {
    Environment     = "DEV"
    Orchestrator    = "Terraform"
    DisplayName     = "MYCONTWAINERXDEXGI00Y"
    ApplicationName = "devwithkrishna"
    Temporary       = "TRUE"
  }
}