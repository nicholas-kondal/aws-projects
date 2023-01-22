# https://github.com/RamVegiraju/streamlit-apps/blob/master/Rekognition-Mood-Detection/app.py
# https://towardsdatascience.com/building-an-emotion-detection-application-54697de9ae01
# To run: streamlit run rekognition-mood-detection.py

# WARNING: need AWS credentials (specifically access keys) in ~/.aws/credentials
# Generate keys at https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/security_credentials (DO NOT STORE anywhere public)

import streamlit as st
import boto3

# Boto3 clients for S3 and Rekognition
s3 = boto3.resource('s3', region_name = 'ap-southeast-2')
rekogClient = boto3.client('rekognition', region_name = 'ap-southeast-2')
imagesBucket = "rekognition-mood-detection"

st.title("Emotion Detection with AWS Rekognition")
st.header("Upload Image")
inputFile = st.file_uploader("Image for Emotion Detection", type = "jpeg")

# Upload File to S3
if inputFile is not None:
    imageFileName = inputFile.name
    S3Name = "streamlit-" + imageFileName
    s3.meta.client.upload_file(f"./{imageFileName}", imagesBucket, S3Name)

    # Emotion Detection
    response = rekogClient.detect_faces(
        Image = {
            'S3Object': {
                'Bucket': imagesBucket,
                'Name': S3Name
            }
        },
        Attributes = ['ALL']
    )

    st.subheader("Main Emotion Detected")
    emotions = response['FaceDetails'][0]['Emotions']
    for emotion in emotions:
        confidence = emotion['Confidence']
        if confidence >= 50:
            st.write("Majority Emotion: " + emotion['Type'])
            st.write("Confidence Score: " + str(confidence))

    st.subheader("All Emotions Detected")
    for emotion in emotions:
        st.write(str(emotion['Type']) + ": " + str(emotion['Confidence']))