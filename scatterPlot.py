import matplotlib.pyplot as plt
import plot2d
import time
import matplotlib

class ScatterPlot:
    def __init__(self, x_column=list(), y_column=list(),
                 title='unnamed', xLabel='x axis', yLabel='y axis',
                 markerSize=15, grid=False):

        self.x_column = x_column
        self.y_column = y_column
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.title = title
        self.markerSize = [markerSize for each in range(len(y_column))]
        # for each bar needs one width value
        self.grid = grid
        pass

    def scatterPlot(self):
        # plt.style.use('_mpl-gallery')
        matplotlib.use('agg')  # necessary
        plt.ion()  # necessary
        
        fig, ax = plt.subplots()
        
        ax.scatter(self.x_column, self.y_column, s=self.markerSize)

        plt.title(self.title)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.grid(self.grid)
        ax.set_axisbelow(True)  # this line provides to take grids to back of bars
        # ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.5)

        
        graphName = str(time.time()).replace(".","")+".jpeg"
        plt.savefig(graphName, format="jpeg")
        scatterGraph = plot2d.ImageUploader(graphName)
        return scatterGraph.create_and_upload_image()
        # plt.show()

