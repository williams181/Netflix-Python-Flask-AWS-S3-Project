import boto3

file_path = 'src\\s3\\teste.jpg'

def textextract_detect_file(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
        file.close()

    textractcliente = boto3.client("textract", aws_access_key_id="ASIA4CEA772BGEL2RDA4",
                                aws_secret_access_key="dpqj3yS9SQBPRTyJ9263u67Bx2SzySyKbDT64lj6", region_name="us-east-1")

    resposta = textractcliente.detect_document_text(
        Document={
            'Bytes': file_content
        }
    )
        
    return resposta

upload = textextract_detect_file(file_path)