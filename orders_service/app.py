from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'

# Pedidos armazenados em memória
orders = []
order_id = 1

def verify_token(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return data['username']
    except Exception:
        return None

@app.route('/pedidos', methods=['POST'])
def create_order():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user = verify_token(token)
    if not user:
        return jsonify({"msg": "Token inválido"}), 401
    global order_id
    data = request.json
    data['id'] = order_id
    order_id += 1
    data['user'] = user
    orders.append(data)
    return jsonify(data), 201

@app.route('/pedidos', methods=['GET'])
def list_orders():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user = verify_token(token)
    if not user:
        return jsonify({"msg": "Token inválido"}), 401
    return jsonify([o for o in orders if o['user'] == user])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
