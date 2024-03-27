from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import plot2d


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        x = plot2d.ImageUploader()
        url = x.create_and_upload_image()
        return url
    elif request.method == "POST":
        return jsonify({"message": "Hello World"})


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
