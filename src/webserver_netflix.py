from flask import Flask
from flask import Flask, request, Response, jsonify
import json
app = Flask(__name__)

@app.route('/oi', methods=['GET'])
def hello_world():
    data = {'mensagem':'Netflix'}
    return Response(response=json.dumps(data), status=200, mimetype='application/json')

@app.route('/index', methods=['GET'])
def show_index():
    return 'src\\index.html'


@app.route('/cadastro', methods=['POST'])
def cadastrar_filme(current_user):
    return 'cadastro'

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
