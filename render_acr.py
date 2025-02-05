from jinja2 import Environment, FileSystemLoader

# Define the template variables
template_vars = {
    "resource_group_name": "myResourceGroup",
    "location": "centralIndia",
    "environment": "dev",
    "application_name": "devwithkrishna",
    "temporary": "true",
    "container_registry_name": "myContwainerxdeXgi00y",
    "sku_name": "Premium",
    "georeplications": [
        {"location": "SouthIndia", "zone_redundancy_enabled": "false"},
        {"location": "eastus2", "zone_redundancy_enabled": "true"}
    ],
    "container_registry_config": {
        "retention_policy_in_days": 37,
        "public_network_access_enabled": "true",
        "quarantine_policy_enabled": "true",
        "zone_redundancy_enabled": "true",
        "admin_enabled": "true",
        "anonymous_pull_enabled": "true",
        "data_endpoint_enabled": "true",
        "trust_policy_enabled": "true"
    },
    "azure_services_bypass": "None"
}

# Set up the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader("templates"), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("main.tf.j2")

# Render the template with the provided variables
rendered_template = template.render(template_vars)

# Write the rendered template to a new file
output_file_path = "main.tf"
with open(output_file_path, "w") as f:
    f.write(rendered_template)

print(f"{output_file_path} has been created successfully!")

