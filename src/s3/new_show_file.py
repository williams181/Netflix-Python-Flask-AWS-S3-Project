import boto3
from werkzeug.datastructures import Headers
from flask import Flask, request, stream_with_context

BUCKET = "netflix-clone-josino"

def show_image2(BUCKET):
    s3_client = boto3.client('s3')
    public_urls = []
    try:
        for item in s3_client.list_objects(BUCKET=BUCKET)['Contents']:
            presigned_url = s3_client.generate_presigned_url('get_object', Params = {'Bucket': BUCKET, 'Key': item['Key']}, ExpiresIn = 100)
            public_urls.append(presigned_url)
    except Exception as e:
        pass
    print("[INFO] : The contents inside show_image = ", public_urls)
    return public_urls