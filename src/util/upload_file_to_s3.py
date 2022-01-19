from s3.indiano_upload_file import upload_file2
from s3.first_upload_file import upload_life1
from model import document
from model.document import Documento, Filme, Serie

file = 'data\\video\\'

file_name = ''

upload_test1 = upload_life1(file, file_name)

upload_test2 = upload_file2(file, file_name)