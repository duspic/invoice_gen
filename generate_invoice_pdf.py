from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from typing import Dict, Any

def generate_invoice_pdf(invoice: Dict[str, Any]) -> bytes:
    """
    Generate a PDF invoice from JSON data using a Jinja template.

    Args:
        invoice (Dict[str, Any]): The invoice JSON data.

    Returns:
        bytes: The PDF file content as bytes.
    """
    # Set up the Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader(searchpath='templates'))
    template = env.get_template('invoice.html')

    # Render the template with the invoice data
    html_content = template.render(invoice=invoice)

    # Generate the PDF from the rendered HTML
    pdf = HTML(string=html_content).write_pdf()
    return pdf
