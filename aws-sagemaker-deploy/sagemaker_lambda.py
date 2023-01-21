# To give Lambda access to SageMaker model:
# 1. Go to the IAM console: https://us-east-1.console.aws.amazon.com/iamv2/home?region=ap-southeast-2#/roles
# 2. Find the role created when creating the Lambda
# 3. Attach the AmazonSageMakerFullAccess policy
# 4. Go to the Lambda console, create a function, and select the role you created.

import boto3 # AWS SDK for Python
import json

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    data = json.loads(json.dumps(event))
    payload = data['data'] # input is sent as a value of the key 'data' which you specify
    print(payload)

    runtime = boto3.client('runtime.sagemaker') # endpoint name is deployment.endpoint in startup_prediction.py
    response = runtime.invoke_endpoint(EndpointName="sagemaker-scikit-learn-2023-01-21-06-23-51-611", Body=json.dumps(payload))
    print(response)
    result = json.loads(response['Body'].read().decode())
    print(result)

    return result[0]

# Test the function by:
# 1. Deploying the function
# 2. Clicking "Test" and configuring a test event in the Lambda console
# 3. Creating a JSON object e.g.: {"data": [[165349.2,136897.8,471784.1,1]]} and clicking "Test"