import json
from sms_messages_as_spam_or_ham.src.model_manager import Model_Manager

def lambda_handler(event, context):
    message = event.get('message')
    
    model_manager = Model_Manager()
    
    model = model_manager.use_saved_model(path='sms_messages_as_spam_or_ham/model/GBM_3_AutoML_1_20231123_10521')
    
    prediction = model_manager.make_single_prediction(model=model, single_message=message)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            "prediction": prediction
        }),
    }