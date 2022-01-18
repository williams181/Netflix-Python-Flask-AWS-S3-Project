import boto3

arquivo = 'src\s3\jaspion.mp4'

def upload_life(arquivo):
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(arquivo, 'netflix-clone-josino-2', 'jaspion_s3.mp4')

upload = upload_life(arquivo)
