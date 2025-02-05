from jinja2 import Environment, FileSystemLoader
import os


def render_template(template_name: str, template_vars: dict, output_file_path: str):
	"""
    Render a Jinja2 template with provided variables and save the result to a file.

    Args:
    - template_name: The name of the Jinja2 template file.
    - template_vars: A dictionary of variables to be used for rendering the template.
    - output_file_path: Path to save the rendered template output.

    Returns:
    - None
    """
	# Ensure template directory exists
	template_dir = os.path.dirname(template_name) or "templates"
	template_file = os.path.basename(template_name)

	# Set up the Jinja2 environment
	env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)

	# Load and render the template
	try:
		template = env.get_template(template_file)
		rendered_template = template.render(template_vars)

		# Write the rendered content to the output file
		with open(output_file_path, "w") as f:
			f.write(rendered_template)

		print(f"{output_file_path} has been created successfully!")
	except Exception as e:
		print(f"Error while rendering template: {e}")


# Example usage
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

# Function call example
render_template("templates/main.tf.j2", template_vars, "main.tf")
