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
def create_and_upload_image(self):
    matplotlib.use("Agg")
    # Görüntü oluşturma
    plt.ion()
    x = np.linspace(0, 10, 100)
    y = np.cos(x)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid()
    plt.title("emrenin grafiği")

    nameOFfile = "deneme_emre3.jpeg"

    # Görüntüyü bir bayt akışına dönüştürme
    x = plt.savefig(nameOFfile, format="jpeg")
    with open(nameOFfile, "rb") as f:
        byte_stream = f.read()

        # Bayt akışını yükle
        supabase.storage.from_("deneme").upload(
            nameOFfile,
            byte_stream,
            file_options={"content-type": "image/jpeg"},
        )
    link_of_image = supabase.storage.from_("deneme").get_public_url(
        nameOFfile
    )
    return link_of_image

