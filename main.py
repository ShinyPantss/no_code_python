from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return jsonify({"Emreye Selam": "Hayirli olsun kardes"})


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
