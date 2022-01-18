import json
import base64
import boto3

BUCKET_NAME = 'netflix-clone-josino-2'

def lambda_handler(event):
    file_content = base64.b64decode(event['content'])
    file_path = 'jaspion.mp4'
    s3 = boto3.client('s3')
    try:
        s3_response = s3.put_object(Bucket=BUCKET_NAME, Key=file_path, Body=file_content)
    except Exception as e:
        raise IOError(e)
    return {
        'statusCode': 200,
        'body': {
            'file_path': file_path
        }
    }
