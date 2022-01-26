import boto3

def upload_file(file, file_name):
    s3 = boto3.client('s3')
    s3.upload_file(file,'netflix-clone-josino', file_name)
    