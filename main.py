from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import plot2d


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        data = request.json
        print(data)
        plot2d.Plot2D(x=[1, 2, 3], y=[4, 5, 6]).show()
    elif request.method == "POST":
        return jsonify({"message": "Hello World"})


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
