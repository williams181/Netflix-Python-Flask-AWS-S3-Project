from importlib.resources import contents
from flask import Flask, render_template, url_for, flash, redirect, send_file, request
from src.s3.indiano_donwload_file import download_file
from src.s3.indiano_upload_file import upload_file
from src.s3.new_upload_file import show_image
from src.s3.new_show_file import show_image2
from werkzeug.datastructures import Headers
import os

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '1234567890'

database_name = 'acess.db'
pathname = os.path.realpath(__file__)
pathname = os.path.split(pathname)[0]
database_path = os.path.join(pathname, database_name)
print(database_path)

UPLOAD_FOLDER = os.path.join(pathname, 'uploads')

DOWNLAOD_FILE = os.path.join(pathname, 'donwloads')

BUCKET = "netflix-clone-josino"

messages = [{'title': 'NETFLIX',
             'content': 'BEM VINDO!!!'}]

# show index
@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')

# Upload video
@app.route('/cadastrar', methods=('GET', 'POST'))
def cadastrar():
    if request.method == 'POST':
        filme = request.form['filme']
        arquivo = os.path.join(UPLOAD_FOLDER, filme)
        salvar = upload_file(arquivo, file_name=filme)
        print(salvar)
        if not filme:
            flash('POR FAVOR ESCOLHA UM FILME!!!')
        else:
            messages.append({'filme': filme})
            return redirect(url_for('index'))

    return render_template('cadastrarFilmes.html', messages=messages)

# donwload video
@app.route('/baixar', methods=('GET', 'POST'))
def baixar():
    if request.method == 'GET':
        filme = request.method['GET']
        arquivo = os.path.join(DOWNLAOD_FILE, filme)
        output = download_file(arquivo, BUCKET)

    return send_file(output, as_attachment=True)

# show videos
@app.route('/assistir', methods=('GET', 'POST'))
def assistir():
    contents = show_image(BUCKET)
    return render_template('assistirFilmes.html', contents=contents)

# show video
@app.route('/<key>', methods=['GET'])
def get_specific_media(key):
    contents = show_image2(key)
    return render_template('filme.html', contents=contents)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
