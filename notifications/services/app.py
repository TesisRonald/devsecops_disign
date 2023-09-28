"""This module contains code for a notification microservice in Flask."""
import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/notifications')
def send_notifications():
    # Make a request to the /products/expiring route to get the list of expiring products
    response = requests.get('127.0.0.1:5000/products/expiring')
    expiring_products = response.json()

    # Make another request to a different route to get the names of the products
    product_names = []
    for product in expiring_products:
        response = requests.get(f'127.0.0.1:5000/products/{product["id"]}/name')
        product_name = response.json()
        product_names.append(product_name)

    # Send notifications for each expiring product
    for product_name in product_names:
        # Code to send notification for each product_name
        pass

    return jsonify({'message': 'Notifications sent'})

if __name__ == '__main__':
    app.run()
