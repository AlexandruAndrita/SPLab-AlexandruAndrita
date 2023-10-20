from ParagraphClass import Paragraph
from ImageClass import Image
from TableClass import Table


class SubChapter:
    def __init__(self, subchapter_name):
        self.subchapter_name = subchapter_name
        self.elements_list = []

    def __repr__(self):
        return f"Subchapter name: {self.subchapter_name}"

    """
    print each subchapter individually with its respective elements (i.e. paragraphs, images, tables)
    """
    def print_instance(self):
        print(f"Subchapter name: {self.subchapter_name}")
        for i in range(len(self.elements_list)):
            self.elements_list[i].print_method()

    def create_new_paragraph(self,paragraph_name):
        paragraph_instance = Paragraph(paragraph_name)
        self.elements_list.append(paragraph_instance)

    def create_new_image(self,image_name):
        image_instance = Image(image_name)
        self.elements_list.append(image_instance)

    def create_new_table(self,table_name):
        table_instance = Table(table_name)
        self.elements_list.append(table_instance)

