import json
import base64
import boto3

def lambda_handler(event, context):
    
    bucket_name = 'netflix-clone-josino'
    s3_client = boto3.client('s3')
    
    file_content = base64.b64decode(event['content'])
    merchantId = event['merchantId']
    catelogId = event['catelogId']
    file_name = event['fileName']
    
    file_path = '{}/{}/{}.mp4'.format(merchantId, catelogId, file_name)

    s3_response = s3_client.put_object(Bucket=bucket_name, Key=file_path, Body=file_content, ContentType='video/mp4')    

    return {
        'statusCode': 200,
        "merchantId":merchantId,
        "catelogId":catelogId,
        "file_name":file_name,
    }
