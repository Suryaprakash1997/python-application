import json

def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"  # ✅ Ensures HTTP response format
        },
        "body": json.dumps({"message": "This is manually deployed!- at 14.04.2025 PM"})
        }
