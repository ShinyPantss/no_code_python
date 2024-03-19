import matplotlib.pyplot as plt
import io
from PIL import Image


class Plot2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self):
        # plot
        plt.plot(self.x, self.y)

    def show(self):
        # Getting the current figure
        fig = plt.gcf()

        # Convert the figure to a PIL Image
        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        img = Image.open(buf)

        # Show the image
        img.show()


# Creating list of Month and Share_buy for Plotting Line Graph
Month = ["January", "February", "March"]
Share_buy = [10, 17, 30]

# Create an instance of Plot2D class
plotter = Plot2D(Month, Share_buy)

# Plot the data
plotter.plot()

# Show the plot
plotter.show()
