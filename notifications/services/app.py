"""Microservcio Notificacion """
import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/notifications')
def send_notifications():
    # obtienes los productos a caducar
    response = requests.get(
        'https://fyqn8yqxea.us-west-2'
        '.awsapprunner.com/inventario/caduca'
    )
    expiring_products = response.json()

    # Obtienes los productos por nombre
    product_names = []
    for product in expiring_products:
        url= f'https://s93n3ben38.us-west-2.awsapprunner'\
            f'.com/products/{product["idproducto"]}'
        response = requests.get(url)
        product_name = response.json()
        product_names.append(product_name)

    
    # Send notifications for each expiring product
    for product_name in product_names:
        # Code to send notification for each product_name
        pass

    return jsonify({'message': 'Notifications sent'})


if __name__ == '__main__':
    app.run()
