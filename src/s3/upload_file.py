import boto3

arquivo = ''

fileName = ''

def upload_life(arquivo):
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(arquivo, 'testetextract', fileName)

upload = upload_life(arquivo)
