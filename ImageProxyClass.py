from ElementClass import Element
from ImageClass import Image


class ImageProxy(Element):
    def __init__(self,url):
        self.url = url
        # self.dim = dim

    def load_image(self):
        real_image = Image(self.url)
        return real_image

    def print_method(self):
        new_image = self.load_image()
        print(new_image)