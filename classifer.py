import scatterPlot
import barPlot
import simplePlot


class Classifer:
    def __init__(self, data):
        self.plotType = data["plotType"]
        self.data = data.data
        pass

    def classify(self):
        if self.plotType == "simplePlot":

            return simplePlot.SimplePlot(self.data)
        elif self.plotType == "scatterPlot":
            return "scatter"
        elif self.plotType == "barPlot":
            return "bar"
        else:
            return "invalid plot type"
