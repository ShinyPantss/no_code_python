import matplotlib.pyplot as plt
import plot2d
import time
import matplotlib

class BarPlot:
    def __init__(self, data, y_column=[1, 2, 3]):

        self.data = data["data"]
        
        # group 1 parameters - y axis parameters and x axis parameters
        self.y_column = y_column
        self.x_column = self.data.get("x_column", None)
        
        # group 2 parameters -  title, xLabel, yLabel
        self.title = self.data.get("title", 'unnamed')
        self.xLabel = self.data.get("xLabel", 'x axis')
        self.yLabel = self.data.get("yLabel", 'y axis')
        
        # group 3 parameters - width, grid
        self.width = [self.data.get("Width", 0.8)]*len(y_column)  # for each bar needs one width value
        self.grid = self.data.get("grid", False)
        # other parameters can be added
        
        if self.x_column is None:
            # if user does not prefer to enter x axis parameters,
            # x column will be arranged as the length of y axis parameters
            self.x_column = range(len(y_column))

    def barPlot(self):
        # summary: this function creates a bar plot graph and returns the image url
        
        matplotlib.use('agg')  # necessary
        plt.ion()  # necessary
        
        fig, ax = plt.subplots()
        
        ax.bar(self.x_column, self.y_column, width=self.width)

        # group 1 parameters(from graph doc classification)
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

