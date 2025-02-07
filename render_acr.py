from jinja2 import Environment, FileSystemLoader
import os
import json


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



def main():
	"""Render the main.tf file using the provided template variables."""
	# read json file
	file_name = 'terraform.tfvars.json'
	print(f"Reading the template variables from {file_name}")
 
	with open(file_name) as f:
		template_vars = json.load(f)
	
	# print template variables
	print(f"The template variables are : \n {template_vars}")

	render_template("templates/main.tf.j2", template_vars, "main.tf")


# Function call example
if __name__ == "__main__":
	main()