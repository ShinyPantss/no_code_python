import scatterPlot
import barPlot
import simplePlot


class Classifer:
    def __init__(self, data):

        self.plotType = data.get("plotType", None)
        self.data = data
        
    def classify(self):
        
        if self.plotType == "simplePlot":
            
            plot = simplePlot.SimplePlot(data=self.data)
            url = plot.simplePlot()
            
        elif self.plotType == "barPlot":
            
            plot = barPlot.BarPlot(data=self.data)
            url = plot.barPlot()
            
        elif self.plotType == "scatterPlot":
            plot = scatterPlot.ScatterPlot(data=self.data)
            url = plot.scatterPlot()
            
        else:
            url = "invalid plot type"
            
        return url
