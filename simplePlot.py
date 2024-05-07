import matplotlib.pyplot as plt
import matplotlib
import time
import plot2d

class SimplePlot:
    def __init__(self, y_column=[1, 2, 3, 4], data=None):
        # data is a dictionary that contains all parameters

        self.data = data["data"]
        
        # group 1 parameters - y axis parameters and x axis parameters
        self.y_column = y_column  # requires update
        self.x_column = self.data.get("x_column", None)
        
        # group 2 parameters -  title, xLabel, yLabel
        self.title = self.data.get("title", 'unname')
        self.xLabel = self.data.get("xLabel", 'x axis')
        self.yLabel = self.data.get("yLabel", 'y axis')
        
        # group 3 parameters - lineWidth, grid
        self.lineWidth = self.data.get("lineWidth", 1)
        self.grid = self.data.get("grid", False)
        
        # group 4 parameters - marker, markersize
        self.marker = self.data.get("marker", "")
        self.markersize = self.data.get("markersize", 4)  # to obtain a visible marker result, min line width value must be 4
        # other parameters can be added
        
        if self.x_column is None:
            # if user does not prefer to enter x axis parameters,
            # x column will be arranged as the length of y axis parameters
            self.x_column = range(len(y_column))


    def simplePlot(self):
        # summary: this function creates a simple plot graph and returns the image url
        
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
        # --> to prevent python to misunderstand remove dot(.) by replace(".","")
        
        # plt.savefig(graphName, format="jpeg") creating fig is in imageuploader
        simpleGraph = plot2d.ImageUploader(graphName)
        
        return simpleGraph.create_and_upload_image()
        
        

# %% old version
# class SimplePlot:
#     def __init__(self,
#                  x_column=None, y_column=list(),
#                  title='unnamed', xLabel='x axis', yLabel='y axis',
#                  lineWidth=1, grid=False,
#                  marker="", markersize=4):
#                  # to obtain a visible marker result, min line width value must be 4

#         if x_column is None:
#             # if user does not prefer to enter x axis parameters,
#             # x column will be arranged as the length of y axis parameters
#             x_column = range(len(y_column))

#         self.x_column = x_column
#         self.y_column = y_column
#         self.xLabel = xLabel
#         self.yLabel = yLabel
#         self.title = title
#         self.lineWidth = lineWidth
#         self.grid = grid
#         self.marker = marker
#         self.markersize = markersize
