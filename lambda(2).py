import json

# The Thresshhh
THRESHOLD = 0.71


def lambda_handler(event, context):


    # Inference Grabber
    inferSTR = event["body"]["inferences"]

    infersplit = inferSTR.split()

    inferHigh = infersplit[1]

    badchars = ",]"

    for character in badchars:

        inferenceGood = inferHigh.replace(character, "")

    inferFloat= float(inferenceGood)


    #Check vals
    meets_threshold = (inferFloat >= THRESHOLD)

    #If we are above the threshold then we are good!
    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
