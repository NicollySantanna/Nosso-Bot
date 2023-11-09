import requests 
import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)

    # definições e nomes que coloquei no DIALOGFLOW
    # intentName = Selecione

    intentName = data['queryResult']['intent']['displayName']
    nome = data['queryResult']['parameters']['nome'] 
    setor = data['queryResult']['parameters']['nome']

    if intentName == "Selecione":

        data['fulfillmentText'] = f"{nome},iremos encaminhar para o {setor} desejado."

    return jsonify(data)

# run flask

if __name__ == '__main__':
    app.debug = False
    app.run()