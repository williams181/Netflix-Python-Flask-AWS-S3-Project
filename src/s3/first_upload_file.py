import boto3

def upload_life1(file, file_name):
    with open(file, 'rb') as file:
        file_content = file.read()
        file.close()
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(file_content, 'netflix-clone-josino', file_name)

