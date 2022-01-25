from flask import Flask, render_template, url_for, flash, request, redirect, send_file
#from indiano_donwload_file import download_file
#from indiano_upload_file import upload_file
#from indiano_list_file import list_files
#from src.model.document import Documento, Filme
#import json
import os
import boto3

def upload_file2(file, file_name):
    s3 = boto3.client('s3')
    s3.upload_file(file,'netflix-clone-josino', file_name)


app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '1234567890'

database_name = 'acess.db'
pathname = os.path.realpath(__file__)
pathname = os.path.split(pathname)[0]
database_path = os.path.join(pathname, database_name)
print(database_path)

PATH_TEMP_FILES = os.path.join(pathname, 'temp')

messages = [{'title': 'NETFLIX',
             'content': 'BEM VINDO!!!'}]

@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html', messages=messages)

@app.route('/listar', methods=('GET', 'POST'))
def listar():
    return render_template('listarFilmes.html', messages=messages)

@app.route('/assistir', methods=('GET', 'POST'))
def assistir():
    return render_template('assistirFilmes.html', messages=messages)

@app.route('/cadastrar', methods=('GET', 'POST'))
def cadastrar():
    if request.method == 'POST':
        filme = request.form['filme']
        arquivo = os.path.join(PATH_TEMP_FILES, filme)
        salvar = upload_file(arquivo, file_name=filme)
        print(salvar)
        if not filme:
            flash('Um Filme e Necessario!!!')
        else:
            messages.append({'filme': filme})
            return redirect(url_for('index'))

    return render_template('cadastrarFilmes.html', messages=messages)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
