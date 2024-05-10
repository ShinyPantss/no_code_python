from flask import Flask, request
from flask_cors import CORS
import os
from random import randint
import classifer
from flask import jsonify
from checker import isCSV, isPDF, isXLSX
import datasetpuller

app = Flask(__name__)
CORS(app)


@app.route("/plot", methods=["GET", "POST"])
def index():

    if request.method == "GET":

        return "GET request recieved"

    elif request.method == "POST":

        data = request.get_json()
        xColumn, yColumn = data["data"]["xColumn"], data["data"]["yColumn"]
        # axises = datasetpuller.DSpull(data).xyColumn([xColumn, yColumn])
        plot = classifer.Classifer(data)
        url = plot.classify()

        return jsonify(url)


@app.route("/datasetInfos", methods=["GET", "POST"])
def api():
    if request.method == "GET":
        return "GET request recieved"

    elif request.method == "POST":
        print("\n\n\nqqqq\n\n\n")
        data = request.get_json()
        print(data)
        columns = datasetpuller.DSpull(data["api"]).get("columns")
        df = datasetpuller.DSpull(data["api"]).get("dataset")
        print("\n\n\n",columns,"\n\n\n")
        print("\n\n\n",df,"\n\n\n")
        # above line creates an instance of the DSpull class with the api as the url then calls the get_columns method on it
        return jsonify('api')
"""
@app.route("/supabase", methods=["GET", "POST"])
def supabase():
    if request.method == "GET":
        return "GET request recieved"

    elif request.method == "POST":
        data = request.get_json()
        print(data)
        if isCSV(data):
            return jsonify({"csv": "csv"})
        return jsonify({"supabase": "supabase"})
"""
if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
