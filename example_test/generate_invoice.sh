#!/bin/bash

# Define variables
JSON_FILE="test_invoice.json"
OUTPUT_FILE="test_invoice.pdf"
URL="http://127.0.0.1:5000/generate_invoice"

# Ensure JSON file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "Error: JSON file '$JSON_FILE' not found."
    exit 1
fi

# Execute curl command
curl -X POST "$URL" \
    -H "Content-Type: application/json" \
    -d @"$JSON_FILE" \
    --output "$OUTPUT_FILE"

# Check if the curl command was successful
if [ $? -eq 0 ]; then
    echo "Invoice generated successfully: $OUTPUT_FILE"
else
    echo "Error: Failed to generate invoice."
    exit 1
fi
