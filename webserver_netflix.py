from flask import Flask, render_template, request, url_for, flash, redirect
from src.s3.indiano_upload_file import upload_file2
from src.model.document import Documento, Filme
import os
import json



app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '1234567890'

database_name = 'acess.db'
pathname = os.path.realpath(__file__)
pathname = os.path.split(pathname)[0]
database_path = os.path.join(pathname, database_name)
print(database_path)

PATH_TEMP_FILES = os.path.join(pathname, 'temp')

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

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
        salvar = upload_file2(arquivo, file_name=filme)
        print(salvar)
        # if not filme:
        #     flash('Title is required!')
        # else:
        #     messages.append({'filme': filme})
        #     return redirect(url_for('index'))

    return render_template('cadastrarFilmes.html', messages=messages)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
