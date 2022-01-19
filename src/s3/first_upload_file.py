import boto3

def upload_life1(file, file_name):
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(file, 'netflix-clone-josino', file_name)


