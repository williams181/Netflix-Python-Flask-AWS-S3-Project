import boto3

fileName = 'jaspion.pm4'

def upload_life(arquivo):
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(arquivo, 'netflix-clone-josino', 'jaspion.mp4')

arquivo = 'data\\video\\jaspion.mp4'

upload = upload_life(arquivo)
