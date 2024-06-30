from flask import Flask, request, jsonify, send_file, render_template
import io

# local imports
from schemas import validate_schema, INVOICE_SCHEMA
from generate_invoice_pdf import generate_invoice_pdf

app = Flask(__name__)

@app.route('/')
def index():
    """
    Main page providing usage instructions for the microservice.
    
    Returns:
        str: Rendered HTML content with instructions.
    """
    example_json = {
        "invoice_no": 123,
        "date": "2024-06-29",
        "sender": {
            "name": "ABC Corp",
            "pdv_id": "123456789",
            "address": "123 Main St",
            "postal_code": 1000,
            "town": "Metropolis",
            "country": "Wonderland"
        },
        "recipient": {
            "name": "XYZ Ltd",
            "pdv_id": "987654321",
            "address": "456 Elm St",
            "postal_code": 2000,
            "town": "Gotham",
            "country": "Wonderland"
        },
        "content": {
            "tasks": [
                {
                    "name": "Task 1",
                    "description": "Development work",
                    "price": 1000
                },
                {
                    "name": "Task 2",
                    "description": "Testing",
                    "price": 500
                }
            ]
        }
    }
    return render_template('index.html', example_json=example_json, schema=INVOICE_SCHEMA)

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    """
    Endpoint to generate an invoice PDF.

    Expects JSON data for the invoice and validates it.
    Returns the generated PDF.

    Returns:
        Response: PDF file if successful, or JSON error message.
    """
    try:
        # Parse the JSON data from the request
        invoice_data = request.json
        
        # Validate the invoice data against the schema
        validate_schema(invoice_data, INVOICE_SCHEMA)
        
        # Generate the PDF from the invoice data
        pdf_content = generate_invoice_pdf(invoice_data)
        
        # Return the generated PDF as a file response
        return send_file(
            io.BytesIO(pdf_content),
            download_name='invoice.pdf',
            as_attachment=True,
            mimetype='application/pdf'
        )
    except Exception as e:
        # Return an error response if validation or PDF generation fails
        response = {
            "error": str(e)
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)