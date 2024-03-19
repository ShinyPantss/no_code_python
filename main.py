from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
