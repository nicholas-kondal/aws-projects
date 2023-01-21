Sources:
- https://www.youtube.com/watch?v=2-mCo7q2Iw4
- https://www.youtube.com/watch?v=BgougRcbYCE

General Steps:
1. Create notebook instance and add startup_prediction.* and 50_Startups.csv files
2. Run notebook and follow instructions in there
3. Create Lambda function with Python runtime and new role
4. Add sagemaker_lambda.py to Lambda function and follow instructions in there
5. Create REST API in API Gateway: https://ap-southeast-2.console.aws.amazon.com/apigateway/main/apis?region=ap-southeast-2
- Create POST method and type Lambda function name then Save
- Click on Actions > Deploy API > New Stage > Stage Name: [e.g. Lambda function name] > Deploy
6. Test API (e.g. in Postman - use raw and JSON as Body) by going to Stages > POST > Invoke URL