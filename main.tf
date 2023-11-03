provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "myResourceGroup"
  location = "East US"
}

resource "azurerm_kubernetes_cluster" "example" {
  name                = "myakscluster"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  dns_prefix          = "myaksdns"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_B2s"
  }

  service_principal {
    client_id     = "3d8063b3-3657-4a03-8fe5-ab9fc694c9f3"
    client_secret = "IF58Q~TEHCrN55sCYzBMrFIM1JluGC08JrJgVbd0"
  }

  tags = {
    environment = "dev"
  }
}
