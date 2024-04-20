from flask import Flask, request
from flask_cors import CORS
import os
from random import randint
import classifer
from flask import jsonify

import datasetpuller

app = Flask(__name__)
CORS(app)


@app.route("/plot", methods=["GET", "POST"])
def index():

    if request.method == "GET":

        return "GET request recieved"

    elif request.method == "POST":

        data = request.get_json()

        plot = classifer.Classifer(data)
        url = plot.classify()

        return jsonify(url)


@app.route("/datasetInfos", methods=["GET", "POST"])
def api():
    if request.method == "GET":
        return "GET request recieved"

    elif request.method == "POST":
        data = request.get_json()

        columns = datasetpuller.DSpull(data["api"]).get_columns()
        # above line creates an instance of the DSpull class with the api as the url then calls the get_columns method on it
        return jsonify(columns)


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
