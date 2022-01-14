import json
import boto3
import base64

import matplotlib.pyplot as plt

s3_client = boto3.client('s3')

def lambda_handler(event, context):

    #addressing
    bucket = "sagemaker-us-east-2-669350239385"
    key = event['s3_key']


    #download data
    #image_data_a = event["image_data"]
    #s3_client = boto3.client('s3')
    #artifact = s3_client.get_object(Bucket=bucket, Key=key)

    cashe = "/tmp/image.png"

    #plt.imsave(cashe, artifact)
    #plt.savefig("/tmp/image.png")

    s3_client.download_file(bucket, key, cashe)

    #read data
    with open(cashe, "rb") as f:
        image_data = base64.b64encode(f.read())

    print(image_data)

    #pass
    print("Event:", event.keys())
    return {
        "statusCode" :200,
        "body": {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }
