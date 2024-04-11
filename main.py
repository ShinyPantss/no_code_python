from flask import Flask, request
from flask_cors import CORS
import os
from random import randint
import classifer

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return "GET request recieved"
    
    elif request.method == "POST":

        data = request.get_json()
        
        print(f"\n\n\n\n\n{data}\n\n\n\n\n")
        plot = classifer.Classifer(data)

        url = plot.classify()
        print(f"\n\n\n\n\n{url}\n\n\n\n\n")
        
        return url

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
