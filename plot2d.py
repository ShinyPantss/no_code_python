import matplotlib.pyplot as plt
import matplotlib
import numpy as np


from supabase import create_client
import os


url: str = os.environ.get("SUPABASE_URL")
print(url)
key: str = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


class ImageUploader:
    def __init__(self):
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

