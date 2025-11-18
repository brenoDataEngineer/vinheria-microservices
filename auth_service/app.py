# app.py
from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'

# Usuários - exemplo em memória
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users:
        return jsonify({"msg": "Usuário já cadastrado"}), 400
    users[username] = password
    return jsonify({"msg": "Usuário registrado"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if users.get(username) == password:
        token = jwt.encode({
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"msg": "Credenciais inválidas"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
