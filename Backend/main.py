from flask import Flask
from flask.globals import request
app=Flask(__name__)

@app.route('/')
def hola():
    return "pagina de prueba"

