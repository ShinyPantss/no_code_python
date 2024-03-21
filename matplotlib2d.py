import matplotlib.pyplot as plt

class Plot2D:

    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def plot(self):
        plt.plot(self.x, self.y)
        plt.savefig('foo.png')


Month = ["January", "February", "March"]
Share_buy = [10, 17, 30]

plot = Plot2D(Month, Share_buy)
plot.plot()