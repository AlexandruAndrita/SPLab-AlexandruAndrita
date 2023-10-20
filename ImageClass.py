from ElementClass import Element


class Image(Element):
    def __init__(self, image_name):
        self.image_name = image_name

    def __repr__(self):
        return f"Image name: {self.image_name}"

    def print_method(self):
        print(f"Image name: {self.image_name}")