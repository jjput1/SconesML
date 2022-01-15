import json

# The Thresshhh
THRESHOLD = 0.95


def lambda_handler(event, context):


    # Inference Grabber
    inferSTR = event["body"]["inferences"]

    # Inference Splitter
    infersplit = inferSTR.split()

    infer1 = infersplit[0]
    infer2 = infersplit[1]

    #individual replace statements is easier on step functions interpreter
    infer1 = infer1.replace(',', "")
    infer1 = infer1.replace('[', "")
    infer2 = infer2.replace(']', "")

    # Defined the badchars and removed them since its a string
    #badchars = "[]"

    #for character in badchars:

    #    inferenceGood1 = infer1.replace(character, "")
    #    inferenceGood2 = infer2.replace(character, "")





    #Now that its formated as a number it can become a float
    inferFloat1= float(infer1)
    inferFloat2= float(infer2)

    #The largest becomes final inferFloat unless 50/50 then 1 becomes final
    if inferFloat1 >= inferFloat2:
        inferFloat = inferFloat1

    elif inferFloat1 < inferFloat2:
        inferFloat = inferFloat2

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
