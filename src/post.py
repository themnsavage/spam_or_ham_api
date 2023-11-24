import json
from model_manager import Model_Manager

def lambda_handler(event, context):
    body = json.loads(event["body"])
    message = body.get('message')
    print(f'body: {body}')
    print(f'message:{message}')
    model_manager = Model_Manager()
    
    model = model_manager.use_saved_model(path='GBM_3_AutoML_1_20231123_10521')
    
    prediction = model_manager.make_single_prediction(model=model, single_message=message)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message,
            "prediction": prediction
        }),
    }