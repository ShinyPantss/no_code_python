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
        # data = request.title
        # print(data)
        # x = plot2d.ImageUploader()
        # print("name----->",x.nameOFfile)
        # url = x.create_and_upload_image()
        # plot = simplePlot.SimplePlot(y_column=[randint(1,10),randint(1,10),randint(1,10),randint(1,10)])
        # url = plot.simplePlot()
        # return url
        return "GET request recieved"
    elif request.method == "POST":
<<<<<<< Updated upstream
        data = request.get_json()
=======
        data = request.json
        # title = data.get('title', 'unnamed')  # .get(,*) there exists second parameter to provide a default value, 
        # if get func does not return a value
        # x = plot2d.ImageUploader()
        # print("name----->",x.nameOFfile)
        # url = x.create_and_upload_image()
        # plot = simplePlot.SimplePlot(y_column=[randint(1,10),randint(1,10),randint(1,10),randint(1,10)])
        plot = scatterPlot.ScatterPlot(y_column=[randint(1,10),randint(1,10),randint(1,10),randint(1,10)],x_column=[randint(1,10),randint(1,10),randint(1,10),randint(1,10)],grid=True,title="title")
        url = plot.scatterPlot()
        print("url---->",url)
        return url
>>>>>>> Stashed changes
        
        print(f"\n\n\n\n\n{data}\n\n\n\n\n")
        plot = classifer.Classifer(data)
        # title = data.get('title', 'unnamed')
        # url = plot.scatterPlot()
        url = plot.classify()
        print(f"\n\n\n\n\n{url}\n\n\n\n\n")
        return url


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
