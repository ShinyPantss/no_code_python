import matplotlib.pyplot as plt
import plot2d
import time
import matplotlib

class ScatterPlot:
    def __init__(self, data, x_column=[1, 2, 3], y_column=[1, 2, 3]):
        
        self.mainDATA = data
        self.data = self.mainDATA["data"]  # data is a dictionary that contains all parameters except the x and y column data
        
        # group 1 parameters - y axis parameters and x axis parameters
        self.y_column = self.mainDATA.get("yColumnData", None)  # warning: x and y column data is not in data["data"], they are in data <mainDATA>
        self.x_column = self.mainDATA.get("xColumnData", None)
        
        # group 2 parameters -  title, xLabel, yLabel
        self.title = self.data.get("title", 'unnamed')
        self.xLabel = self.data.get("xLabel", 'x axis')
        self.yLabel = self.data.get("yLabel", 'y axis')
        
        # group 3 parameters - markerSize, grid, color
        self.markerSize = [self.data.get("markerSize", 15)]*len(self.y_column)  # for each bar needs one width value
        self.grid = self.data.get("grid", False)
        self.color = self.data.get("color", "blue")
        # other parameters can be added
        
    def scatterPlot(self):
        # summary: this function creates a scatter plot graph and returns the image url
        
        matplotlib.use('agg')  # necessary
        plt.ion()  # necessary
        
        fig, ax = plt.subplots()
        
        ax.scatter(self.x_column, self.y_column, s=self.markerSize,c=self.color)

        # group 1 parameters(from graph doc classification)
        plt.title(self.title)
        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        
        plt.grid(self.grid)
        ax.set_axisbelow(True)  # this line provides to take grids to back of bars
        # ax.yaxis.grid(color='gray', linestyle='-', linewidth=0.5)
        
        graphName = str(time.time()).replace(".","")+".jpeg"
        
        scatterGraph = plot2d.ImageUploader(graphName)
        return scatterGraph.create_and_upload_image()



# %% old version
# def __init__(self, x_column=list(), y_column=list(),
#              title='unnamed', xLabel='x axis', yLabel='y axis',
#              markerSize=15, grid=False):

#     self.x_column = x_column
#     self.y_column = y_column
#     self.xLabel = xLabel
#     self.yLabel = yLabel
#     self.title = title
#     self.markerSize = [markerSize for each in range(len(y_column))]
#     # for each bar needs one width value
#     self.grid = grid
