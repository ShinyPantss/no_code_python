import matplotlib.pyplot as plt
import matplotlib
import time
import plot2d
"""
X Axis Data  list[or like list types(numpy array etc.)]
•	Not necessary <default range(len(y))>
Y Axis Data  list[or like list types(numpy array etc.)]

Labels and Title string
•	Set axis names and graph title
•	ax.set_xlabel('x-axis')
•	ax.set_ylabel('y-axis')
•	ax.set_title('the graph’)
"""
"""
Notes For Web side:
when x axis has been chosen as empty(no parameter), the user should see a warning below.

WARNING: x-axis has been arranged by getting reference the length of y axis parameters.
         To obtain better results please choose x-axis parameters.

"""


class SimplePlot:
    def __init__(self,
                 x_column=None, y_column=list(),
                 title='unnamed', xLabel='x axis', yLabel='y axis',
                 lineWidth=1, grid=False,
                 marker="", markersize=4):
                 # to obtain a visible marker result, min line width value must be 4

        if x_column is None:
            # if user does not prefer to enter x axis parameters,
            # x column will be arranged as the length of y axis parameters
            x_column = range(len(y_column))

        self.x_column = x_column
        self.y_column = y_column
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.title = title
        self.lineWidth = lineWidth
        self.grid = grid
        self.marker = marker
        self.markersize = markersize
        pass

    def simplePlot(self):
        # plt.style.use('_mpl-gallery')
        matplotlib.use('agg')  # necessary
        plt.ion()  # necessary
        fig, ax = plt.subplots()

        ax.plot(self.x_column, self.y_column, linewidth=self.lineWidth, marker=self.marker, markersize=self.markersize)

        # group 1 parameters(from graph doc classification)
        plt.title(self.title)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)

        # ax.linewidth(self.lineWidth)  # alias .set_lw(lw)
        # ^^^^^^^^ There is no linewidth module in plt lib,
        ax.grid(self.grid)

        graphName = str(time.time()).replace(".","")+".jpeg"
        # str(time.time()) --> 1234358745.2873263 
        # --> to prevent python to misunderstand remove dot(.) by .replace(".","")
        
        plt.savefig(graphName, format="jpeg")
        simpleGraph = plot2d.ImageUploader(graphName)
        return simpleGraph.create_and_upload_image()
        