import json
import sagemaker
import base64
from sagemaker.serializers import IdentitySerializer
import boto3

runtime= boto3.client('runtime.sagemaker')

ENDPOINT = "image-classification-2022-01-15-19-38-41-511"


def lambda_handler(event, context):
    print("HELLLLLLOOOOOOOOOO image-data")
    #print(event["image_data"])
    image_data = event["body"]["image_data"]
    key = event["body"]["s3_key"]
    bucket = event["body"]["s3_bucket"]
    #print(image_data)
    # Decoder clause
    image = base64.b64decode(image_data)

    # Predictor Build
    predictor = sagemaker.predictor.Predictor(
    endpoint_name=ENDPOINT,
    sagemaker_session=sagemaker.session.Session(),
    serializer=IdentitySerializer("image/png")
    )
    print("HELLO world.self.")
    print(image)

    # Prediction call
    inference = predictor.predict(image)

    # Pass back data for step function
    inferences = inference.decode('utf-8')

    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": inferences
        }
    }
