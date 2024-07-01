# Invoice PDF Generator

To run it succesfully, build and run the docker image with

> docker build -t invoicegen .
> docker run -p 5000:5000 invoicegen

The default docker image (300MB) uses xhtml2pdf python library to render the pdf contents. This is a lightweight solution, but lacking in nuances. A heavier solution (650 MB) is to use the weasyprint library, included in a separate folder. To use it, move it to the main directory and replace the Dockerfile with Dockerfile_weasy, and requirements.txt with requirements_weasy.txt

To generate an invoice PDF, go to `/form` and fill out the details, or send a POST request to `/generate_invoice` with a JSON body containing the invoice details.

Example request from cmd, when running on localhost, sending a file called test_invoice.json

> curl -X POST http://127.0.0.1:5000/generate_invoice -H "Content-Type: application/json" -d @test_invoice.json --output test_invoice.pdf

test_invoice.json

```json
{
    "content": {
        "tasks": [
            {
                "description": "Development work",
                "name": "Task 1",
                "price": 1000
            },
            {
                "description": "Testing",
                "name": "Task 2",
                "price": 500
            }
        ]
    },
    "date": "2024-06-29",
    "invoice_no": 123,
    "recipient": {
        "address": "456 Elm St",
        "country": "Wonderland",
        "name": "XYZ Ltd",
        "pdv_id": "987654321",
        "postal_code": 2000,
        "town": "Gotham"
    },
    "sender": {
        "address": "123 Main St",
        "country": "Wonderland",
        "name": "ABC Corp",
        "pdv_id": "123456789",
        "postal_code": 1000,
        "town": "Metropolis"
    }
}
```

You can edit the test_invoice.json according to this schema:

```json
{
    "properties": {
        "content": {
            "properties": {
                "tasks": {
                    "items": {
                        "properties": {
                            "description": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "price": {
                                "type": "number"
                            }
                        },
                        "required": [
                            "name",
                            "price"
                        ],
                        "type": "object"
                    },
                    "minItems": 1,
                    "type": "array"
                }
            },
            "required": [
                "tasks"
            ],
            "type": "object"
        },
        "date": {
            "description": "Date of the invoice",
            "format": "date",
            "type": "string"
        },
        "invoice_no": {
            "description": "Unique invoice number",
            "type": "integer"
        },
        "recipient": {
            "properties": {
                "address": {
                    "type": "string"
                },
                "country": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "pdv_id": {
                    "type": "string"
                },
                "postal_code": {
                    "type": "integer"
                },
                "town": {
                    "type": "string"
                }
            },
            "required": [
                "name",
                "pdv_id"
            ],
            "type": "object"
        },
        "sender": {
            "properties": {
                "address": {
                    "description": "Street name and number, with whitespaces",
                    "type": "string"
                },
                "country": {
                    "description": "Name of country",
                    "type": "string"
                },
                "name": {
                    "description": "Name of company",
                    "type": "string"
                },
                "pdv_id": {
                    "description": "PDV ID, without whitespaces",
                    "type": "string"
                },
                "postal_code": {
                    "description": "Numbers only",
                    "type": "integer"
                },
                "town": {
                    "description": "Name of town",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "pdv_id",
                "address",
                "postal_code",
                "town",
                "country"
            ],
            "type": "object"
        }
    },
    "required": [
        "invoice_no",
        "date",
        "sender",
        "recipient",
        "content"
    ],
    "type": "object"
}
```
