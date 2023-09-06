from flask import Flask, jsonify
import uuid

app = Flask(__name__)
app.debug = True
"""
Este metodo sirve para generar el serial.
"""

@app.route("/")
def code():
    serial = generat_serial()
    result = {"codigo": serial}
    return jsonify(result)

def generat_serial():
    """
    Este código sirve para generar un código único
    """
    # Genera un UUID y toma los primeros 10 caracteres
    serial = str(uuid.uuid4())[:10]
    return serial

if __name__ == '__main__':
    app.run()
