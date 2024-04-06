import matplotlib.pyplot as plt
import plot2d
import time
import matplotlib

class BarPlot:
    def __init__(self, x_column=None, y_column=list(),
                 title='unnamed', xLabel='x axis', yLabel='y axis',
                 width=0.8, grid=False):

        if x_column is None:
            # if user does not prefer to enter x axis parameters,
            # x column will be arranged as the length of y axis parameters
            x_column = range(len(y_column))

        self.x_column = x_column
        self.y_column = y_column
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.title = title
        self.width = [width for each in range(len(y_column))]
        # for each bar needs one width value
        self.grid = grid
        pass

    def barPlot(self):
        # plt.style.use('_mpl-gallery')
        matplotlib.use('agg')  # necessary
        plt.ion()  # necessary
        
        fig, ax = plt.subplots()
        
        ax.bar(self.x_column, self.y_column, width=self.width)

        plt.title(self.title)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.grid(self.grid)
        ax.set_axisbelow(True)  # this line provides to take grids to back of bars
        # ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.5)

        
        graphName = str(time.time()).replace(".","")+".jpeg"
        plt.savefig(graphName, format="jpeg")
        barGraph = plot2d.ImageUploader(graphName)
        return barGraph.create_and_upload_image()
        # plt.show()

