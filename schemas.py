SENDER_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "description": "Name of company"},
        "pdv_id": {"type": "string", "description": "PDV ID, without whitespaces"},
        "address": {"type": "string", "description": "Street name and number, with whitespaces"},
        "postal_code": {"type": "integer", "description": "Numbers only"},
        "town": {"type": "string", "description": "Name of town"},
        "country": {"type": "string", "description": "Name of country"}
    },
    "required": ["name", "pdv_id", "address", "postal_code", "town", "country"]
}

RECIPIENT_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "pdv_id": {"type": "string"},
        "address": {"type": "string"},
        "postal_code": {"type": "integer"},
        "town": {"type": "string"},
        "country": {"type": "string"}
    },
    "required": ["name", "pdv_id"]
}

TASK_SCHEMA = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "description": {"type": "string"},
        "price": {"type": "number"}
    },
    "required": ["name", "price"]
}

CONTENT_SCHEMA = {
    "type": "object",
    "properties": {
        "tasks": {
            "type": "array",
            "minItems": 1,
            "items": TASK_SCHEMA
        }
    },
    "required": ["tasks"]
}

INVOICE_SCHEMA = {
    "type": "object",
    "properties": {
        "invoice_no": {
            "type": "integer",
            "description": "Unique invoice number"
        },
        "date": {
            "type": "string",
            "format": "date",
            "description": "Date of the invoice"
        },
        "sender": SENDER_SCHEMA,
        "recipient": RECIPIENT_SCHEMA,
        "content": CONTENT_SCHEMA
    },
    "required": ["invoice_no", "date", "sender", "recipient", "content"]
}

from jsonschema import validate, ValidationError, SchemaError
from typing import Dict, Any


def validate_schema(instance: Dict[str, Any], schema: Dict[str, Any]) -> None:
    """
    Validate a JSON instance against a JSON schema.

    Args:
        instance (Dict[str, Any]): The JSON object to validate.
        schema (Dict[str, Any]): The JSON schema to validate against.

    Raises:
        ValidationError: If the instance is invalid according to the schema.
        SchemaError: If the schema itself is invalid.
        Exception: For any other errors during validation.

    Returns:
        None
    """
    try:
        validate(instance=instance, schema=schema)
        print("Validation successful: The instance is valid according to the schema.")
    except ValidationError as ve:
        print(f"Validation error: {ve.message}")
        raise
    except SchemaError as se:
        print(f"Schema error: {se.message}")
        raise
    except Exception as e:
        print(f"Unexpected error during validation: {str(e)}")
        raise