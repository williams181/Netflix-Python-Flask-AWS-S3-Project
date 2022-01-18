import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'ASIA5NBMOBZQS6BE73WD'
SECRET_KEY = 'cj7SksK9ShjjeQsGpGyv/3L0KyrAUFyHHdzgns08'


local_file = 'C:\\Users\\william\\Desktop\\projetoifpe\\aws-josino-video\\data\\video\\jaspion.mp4'

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws(local_file, 'netflix-clone-josino', 'jaspion.mp4')