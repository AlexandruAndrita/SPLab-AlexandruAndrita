from models.VisitorClass import Visitor
from models.TableOfContentsClass import TableOfContents


class TableOfContentUpdate(Visitor):
    def __init__(self):
        self.table_of_contents = TableOfContents()
        self.page = 0
        self.set_contents = set()

    def visit_book(self,book):
        for element in book.elements:
            element.accept(self)

    def visit_section(self,section):
        section_title = section.get_section_name()

        el = f"Section: {section_title} {'.' * (90-len(section_title) + len('Section: '))} {self.page}"
        self.table_of_contents.add_element(el)

        self.page += 1

    def visit_paragraph(self,paragraph):
        paragraph_title = paragraph.get_paragraph_name()
        el = f"Paragraph: {paragraph_title} {'.' * (90-len(paragraph_title) + len('Paragraph: '))} {self.page}"
        self.table_of_contents.add_element(el)
        self.page += 1

    def visit_image_proxy(self,image_proxy):
        image_proxy_title = image_proxy.get_image_url()
        el = f"Image Proxy: {image_proxy_title} {'.' * (90-len(image_proxy_title) + len('Image Proxy: '))} {self.page}"
        self.table_of_contents.add_element(el)
        self.page += 1

    def visit_image(self,image):
        image_name = image.get_image_name()
        el = f"Image: {image_name} {'.' * (90-len(image_name) + len('Image: '))} {self.page}"
        self.table_of_contents.add_element(el)
        self.page += 1

    def visit_table(self,table):
        table_title = table.get_table_title()
        el = f"Table: {table_title} {'.' * (90-len(table_title) + len('Table: '))} {self.page}"
        self.table_of_contents.add_element(el)
        self.page += 1

    def get_toc(self):
        return self.table_of_contents

