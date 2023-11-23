import json
import os
import sys

if "AWS_EXECUTION_ENV" not in os.environ:
    from ...sms_messages_as_spam_or_ham.src.model_manager import Model_Manager
else:
    sys.path.append("/opt/")
    from src.model_manager import Model_Manager

def lambda_handler(event, context):
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello",
        }),
    }