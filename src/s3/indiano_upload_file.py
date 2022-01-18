import boto3

s3 = boto3.client('s3')
s3.upload_file('src\s3\jaspion.mp4','netflix-clone-josino-2', 'jaspion_s3.mp4')