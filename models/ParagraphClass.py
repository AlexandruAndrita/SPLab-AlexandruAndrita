from models.ElementClass import Element


class Paragraph(Element):
    def __init__(self, paragraph_name):
        self.paragraph_name = paragraph_name
        self.number_paragraphs = 0

    def __repr__(self):
        return f"Paragraph: {self.paragraph_name}"

    def print_method(self):
        print(f"Paragraph: {self.paragraph_name}")

    def set_align_strategy(self, AlignStrategy):
        self.paragraph_name = AlignStrategy.render(self.paragraph_name)

    def accept(self,visitor):
        visitor.visit_paragraph(self)

    def get_paragraph_name(self):
        return self.paragraph_name

