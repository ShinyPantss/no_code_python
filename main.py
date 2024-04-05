from flask import Flask, jsonify, request
import simplePlot
from flask_cors import CORS
import os
import plot2d
import time

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        # x = plot2d.ImageUploader()
        # print("name----->",x.nameOFfile)
        # url = x.create_and_upload_image()
        plot = simplePlot.SimplePlot(y_column=[4,2,3,10],title='deneme')
        url = plot.simplePlot()
        return url
    elif request.method == "POST":
        return jsonify({"message": "Hello World"})


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
