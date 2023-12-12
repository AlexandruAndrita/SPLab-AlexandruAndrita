from models.ElementClass import Element
import time


class Image(Element):
    def __init__(self, image_name):
        self.image_name = image_name
        # time.sleep(5)

    def __repr__(self):
        return f"Image with name: {self.image_name}"

    def print_method(self):
        print(f"Image with name: {self.image_name}")

    def accept(self, visitor):
        visitor.visit_image(self)

    def get_image_name(self):
        return self.image_name

