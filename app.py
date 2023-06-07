from flask import Flask, jsonify
from flask_caching import Cache
import requests

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route("/")
def inicio():
    return "<h1>Página inicial</h1>"

@app.route("/objetos")
@cache.cached(timeout=90)
def objetos():

    url = "https://api.chucknorris.io/jokes/random"

    objetos = list()
    ids = set()

    while len(objetos) < 25:
        respuesta = requests.get(url)
        respuesta_json = respuesta.json()
        ide = respuesta_json["id"]
        if ide not in ids:
            objetos.append(respuesta_json)
            ids.add(ide)

    return jsonify({"Objetos":objetos})

@app.route("/jokes")
@cache.cached(timeout=90)
def jokes():

    bromas = list()

    url = "https://api.chucknorris.io/jokes/random"

    objetos = list()
    ids = list()

    while len(objetos) < 25:
        respuesta = requests.get(url)
        respuesta_json = respuesta.json()
        ide = respuesta_json["id"]
        if ide not in ids:
            objetos.append(respuesta_json)
            ids.append(ide)

    for ob in objetos:
        broma = ob["value"]

        bromas.append(broma)

    return jsonify({"jokes":bromas})

if __name__ == "__main__":
    app.run(debug = True, port = 4000)
