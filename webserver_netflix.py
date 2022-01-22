from flask import Flask, render_template, url_for

app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/listar')
def listar():
    return render_template('listarFilmes.html', messages=messages)

@app.route('/assistir')
def assistir():
    return render_template('assistirFilmes.html', messages=messages)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrarFilmes.html', messages=messages)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
