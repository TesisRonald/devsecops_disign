from flask import Flask, jsonify, request
from bson.errors import InvalidId
from bson import ObjectId
from db import db_client
from datetime import datetime, timedelta
from flask_wtf.csrf import CSRFProtect  # type: ignor

app = Flask(__name__)
csrf = CSRFProtect(app)


@app.route('/inventario')
def get_inventorys():
    """Obtiene una lista de productos del inventario.
    Esta función obtiene una lista 
    de productos del inventario desde
    la base de datos y los devuelve en
    formato JSON.   
    """
    results = db_client.inventario.find()
    inventario = []
    for result in results:
        inventario.append({
            'id': str(result['_id']),
            'idproducto': result['idproducto'],
            'codigo': result['codigo'],
            'fechavenc': result['fechavenc'],
            'Undlote': result['Undlote'],
        })
    return jsonify(inventario)


@app.route('/inventario/<string:inventory_id>')
def get_inventory(inventory_id):
    """Obtiene un producto del inventario por su ID.

    Esta función busca un producto 
    en la base de datos por su ID y 
    lo devuelve en formato JSON. 
    Si el producto no se encuentra, 
    devuelve un error 404.

    Args:
    inventory_id (str): El ID del producto a buscar.

    Returns:
        json: Un objeto JSON que representa el producto encontrado o un mensaje de error si no se encuentra.
    """
    try:
        result = db_client.inventario.find_one({'_id': ObjectId(inventory_id)})
    except InvalidId:
        result = None
    if result is None:
        return jsonify({'error': 'Producto no encontrado'}), 404
    inventario = {
        'id': str(result['_id']),
        'idproducto': result['idproducto'],
        'codigo': result['codigo'],
        'fechavenc': result['fechavenc'],
        'Undlote': result['Undlote'],
    }
    return jsonify(inventario)


@app.route('/inventario', methods=['POST'])
def create_inventory():
    """Crea un nuevo producto en el inventario.

    Esta función recibe datos a través de una solicitud POST
    y los guarda en la base de datos. Devuelve el ID del producto creado.

    Returns:
        json: Un objeto JSON que contiene el ID del producto creado.
    """

    if request is not None:
        id = db_client.inventario.insert_one(
            {
                'idproducto': request.json['idproducto'],
                'codigo': request.json['codigo'],
                'fechavenc': request.json['fechavenc'],
                'Undlote': request.json['Undlote'],
            }
        )
        respose = {
            'id': str(id.inserted_id),
            'registrado': 'registrado en el inventario'
        }
        return respose

    else:
        return jsonify({'message': 'Not found'}), 404


@app.route('/inventario/caduca')
def get_expiring_products():
    """Obtiene una lista de productos que están a punto de caducar.

    Esta función busca productos cuya fecha de
    caducidad sea dentro de una semana y los 
    devuelve en formato JSON.

    Returns:
        json: Un objeto JSON con una lista de productos a caducar.
    """
    next_week = datetime.now() + timedelta(weeks=12)
    next_week_str = next_week.strftime('%Y-%m-%d')
    results = db_client.inventario.find({'fechavenc': {'$lt': next_week_str}})
    products = []
    for result in results:
        products.append({
            'id': str(result['_id']),
            'idproducto': result['idproducto'],
            'codigo': result['codigo'],
            'fechavenc': result['fechavenc'],
            'Undlote': result['Undlote'],
        })
    return jsonify(products)


if __name__ == '__main__':
    app.run()
