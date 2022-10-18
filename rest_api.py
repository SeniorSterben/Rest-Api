# MI PRIMER REST API
#PROGRAMACIÓN DE SOFTWARE
#SANTIAGO VELÁSQUEZ
#SENA:CGMLTI
#FICHA:2502640
#ERICK GRANADOS
#2020
#-----------------------------
#CREACIÓN DEL SERVIDOR LOCAL
from flask import Flask, jsonify

app = Flask(__name__) 

from store import stores

#FUNCIÓN DE TESTEO
@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})

#FUNCIÓN PARA RETORNAR TODA LA LISTA DE ITEMS EN GENERAL ADICIONANDO UN MENSAJE
@app.route('/store')
def poststore():
    return jsonify({"store": stores, "message": "Lista de productos"})

#FUNCIÓN PARA RETORNAR SOLO UN ELEMENTO EN ESPECÍFICO
@app.route('/store/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in stores if product['name'] == product_name]
    return jsonify({"product": productsFound[0]})

#CONDICIÓN PARA GUARDAR CAMBIOS EN EL SERVIDOR
if __name__ == '__main__':
    app.run(debug=True, port=4000)

