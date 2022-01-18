import boto3

def textextract_detect_file(file_path):
    with open(file_path, 'rb') as file:
        file_content = file.read()
        file.close()

    textractcliente = boto3.client("", aws_access_key_id="",
                                aws_secret_access_key="", region_name="")

    resposta = textractcliente.detect_document_text(
        Document={
            'Bytes': file_content
        }
    )
        
    return resposta

