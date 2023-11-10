from ElementClass import Element


class Paragraph(Element):
    def __init__(self, paragraph_name):
        self.paragraph_name = paragraph_name

    def __repr__(self):
        return f"Paragraph: {self.paragraph_name}"

    def print_method(self):
        print(f"Paragraph: {self.paragraph_name}")
