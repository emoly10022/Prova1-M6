from flask import Flask, request, jsonify
from produtoController import APIController

app = Flask(__name__)
api_controller = APIController()

@app.route('/calcular_valor_projetado', methods=['POST'])
def calcular_valor_projetado():
    data = request.json
    id_usuario = data.get('id_usuario')
    id_produto = data.get('id_produto')

    valor_projetado = api_controller.calcular_valor_projetado(id_usuario, id_produto)

    return jsonify({'valor_projetado': valor_projetado})
