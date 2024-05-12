import matplotlib.pyplot as plt
import plot2d
import time
import matplotlib

class BarPlot:
    def __init__(self, data=None):

        self.mainDATA = data
        self.data = self.mainDATA["data"]  # data is a dictionary that contains all parameters except the x and y column data
        
        # group 1 parameters - y axis parameters and x axis parameters
        self.y_column = self.mainDATA.get("yColumnData", None)  # warning: x and y column data is not in data["data"], they are in data <mainDATA>
        self.x_column = self.mainDATA.get("xColumnData", None)
        
        
        # group 2 parameters -  title, xLabel, yLabel
        self.title = self.data.get("title", 'unnamed')
        self.xLabel = self.data.get("xLabel", 'x axis')
        self.yLabel = self.data.get("yLabel", 'y axis')
        
        # group 3 parameters - width, grid
        self.width = [self.data.get("Width", 0.8)]*len(self.y_column)  # for each bar needs one width value
        self.grid = self.data.get("grid", False)
        # other parameters can be added
        
        if self.x_column is None:
            # if user does not prefer to enter x axis parameters,
            # x column will be arranged as the length of y axis parameters
            self.x_column = range(len(self.y_column))

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
        
        barGraph = plot2d.ImageUploader(graphName)
        return barGraph.create_and_upload_image()

