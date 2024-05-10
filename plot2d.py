import matplotlib.pyplot as plt
import matplotlib
from supabase import create_client
import os
from time import time
from deleter import del_current_img

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


class ImageUploader:
    def __init__(self, nameOFfile):
        
        self.nameOFfile = nameOFfile
        pass

    def create_and_upload_image(self):
        matplotlib.use('agg')  # necessary
        plt.ion()
        # Görüntüyü bir bayt akışına dönüştürme
        
        plt.savefig(self.nameOFfile, format="jpeg")
        
        with open(self.nameOFfile, "rb") as f:
            byte_stream = f.read()

            # Bayt akışını yükle
            supabase.storage.from_("deneme").upload(
                self.nameOFfile,
                byte_stream,
                file_options={"content-type": "image/jpeg"},
            )
        link_of_image = supabase.storage.from_("deneme").get_public_url(
            self.nameOFfile
        )
        
        del_current_img(self.nameOFfile)  # delete the graph image after uploading it from the local(railway server)
        
        return link_of_image


"""response = supabase.table('DataSets').insert({"data_name":"deneme2"}).execute()
print(response)
"""

"""
# Old version
class ImageUploader:
    def __init__(self, xLabel=False, yLabel=False, title='unnamed', lineWidth=1, grid=False, ):
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.title = title
        self.lineWidth = lineWidth
        self.grid = grid
        pass

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



class BarPlot:
    def __init__(self, x_column=list(), y_column=list(), xLabel=False, yLabel=False, title='unnamed', lineWidth=1, grid=False):
        self.x_column = x_column
        self.y_column = y_column
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.title = title
        self.lineWidth = lineWidth
        self.grid = grid
        pass

    def barPlot(self):
        plt.style.use('_mpl-gallery')
        fig, ax = plt.subplots()
        ax.plot(self.x_column, self.y_column, linewidth=self.lineWidth)

        ax.set_xlabel(self.xLabel)
        ax.set_ylabel(self.yLabel)
        ax.grid(self.grid)


        ax.set(xlim=(0, 8), xticks=np.arange(min(self.x_column), max(self.x_column)),
               ylim=(0, 8), yticks=np.arange(min(self.y_column), max(self.y_column)))
        # the part above requires rearrange xlim ylim xticks yticks

        plt.show()

"""