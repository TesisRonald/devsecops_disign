from flask import Flask, jsonify, request
from bson.errors import InvalidId
from bson import ObjectId
from db import db_client
from flask_wtf.csrf import CSRFProtect  # type: ignore

app = Flask(__name__)
csrf = CSRFProtect(app)


@app.route('/products')
def get_products():
    """Lista serial
    Keyword arguments:
    cargamos todo los seriales con su id
    Return: se crea un json de todo los seriales
    """

    results = db_client.products.find()
    products = []
    for result in results:
        products.append({
            'id': str(result['_id']),
            'name': result['name'],
            'price': result['price']
        })
    return jsonify(products)


@app.route('/products/<string:product_id>')
def get_product(product_id):
    try:
        result = db_client.products.find_one({'_id': ObjectId(product_id)})
    except InvalidId:
        result = None
    if result is None:
        return jsonify({'error': 'Producto no encontrado'}), 404
    produc = {
        'id': str(result['_id']),
        'name': result['name'],
        'price': result['price']
    }
    return jsonify(produc)


@app.route('/products', methods=['POST'])
def create_product():
    # if resultado

    if request is not None:
        product_id = db_client.products.insert_one(
            {
                'name': request.json['name'],
                'price': request.json['price']
            }
        )
        respose = {
            'id': str(product_id.inserted_id),
            'registrado': 'registrado producto'
        }
        return respose

    else:
        return jsonify({'message': 'Not found'}), 404


if __name__ == '__main__':
    app.run()
