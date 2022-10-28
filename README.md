# Rest-Api
Las API son conjuntos de definiciones y protocolos que se utilizan para diseñar e integrar el software de las aplicaciones.Suele considerarse como el contrato entre el proveedor de información y el usuario, donde se establece el contenido que se necesita por parte del consumidor (la llamada) y el que requiere el productor (la respuesta).
Lo primero es crear una base de datos la cual vamos a recopilar con el método get y post.

Creación de los items de la Store:

stores = [
    {"name": "chair", "price": 175.50, "quantity": 6},
    {"name": "table", "price": 200, "quantity": 10},
]

Ahora creamos el servidor local:

from flask import Flask, jsonify

app = Flask(__name__) 

from store import stores

Ahora creamos el endpoint donde se conectará el API para obtener información, agregandole el formato de texto llamado jsonify para que nos retorne los datos así:

@app.get("/store")
def get_store():
    return jsonify({"store": stores, "message": "Lista de productos"})
Con este código hacemos que se ejecute en el puerto 4000, tambien sirve para guardar cambios en el código gracias a la condición.

if __name__ == '__main__':
    app.run(debug=True, port=4000)





