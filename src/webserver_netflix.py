from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from functools import wraps
import json
import os
import uuid
import time

# Declare a flask app
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

SECRET_KEY = 'cj7SksK9ShjjeQsGpGyv/3L0KyrAUFyHHdzgns08'
database_name = 'acess.db'
pathname = os.path.realpath(__file__)
pathname = os.path.split(pathname)[0]
database_path = os.path.join(pathname, database_name)
print(database_path)
app.config['SECRET_KEY']=SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

PATH_TEMP_FILES = os.path.join(pathname, 'temp')

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    token = db.Column(db.String(50))
    
def init_acess_db():
    if not os.path.exists(database_path):
        print("Database acess não encontrado.")
        print("Criando base de dados.")
        db_conn = sqlite3.connect(database_path)
        db_conn.close()
        db.create_all()

def add_user(name):
    new_user = Usuario(token=str(uuid.uuid4()), name=name) 
    db.session.add(new_user)
    db.session.commit()

def get_token(name):
    user = Usuario.query.filter_by(name=name).first() 
    return user.token

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return Response(response=json.dumps({'mensagem': 'Um token valido deve ser informado!!!...'}), status=404, mimetype='application/json')#jsonify({'message': 'a valid token is missing'})

        try:
            current_user = Usuario.query.filter_by(token=token).first()
        except:
            return Response(response=json.dumps({'mensagem': 'Este Token e inválido!!!'}), status=404, mimetype='application/json')#jsonify({'message': 'token is invalid'})

        if current_user is None:
            return Response(response=json.dumps({'mensagem': 'Este Token e inválido!!!'}), status=404, mimetype='application/json')#jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
    return decorator

@app.route('/oi', methods=['GET'])
@token_required
def hello(current_user):
    data = {'mensagem':'Árvore'}
    return Response(response=json.dumps(data), status=200, mimetype='application/json')

@app.route('/processar', methods=['POST'])
@token_required
def processar_documento(current_user):


    if __name__ == '__main__':
        init_acess_db()
        username= 'root'
        user = Usuario.query.filter_by(name=username).first() 
        if user is None:
            add_user(username)
        
        print(get_token(username))

        print('='*50)
        print('Running...')
        print('='*50)

        app.run(host='0.0.0.0', port=4000, debug=True)
