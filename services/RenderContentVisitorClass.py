from models.VisitorClass import Visitor


class RenderContentVisitor(Visitor):
    def __init__(self):
        pass

    def visit_book(self,book):
        book.print_instance()

    def visit_section(self,section):
        section.print_method()

    def visit_table_of_contents(self,table_of_contents):
        table_of_contents.print_table_of_contents()

    def visit_paragraph(self,paragraph):
        paragraph.print_method()

    def visit_image_proxy(self,image_proxy):
        image_proxy.print_method()

    def visit_image(self,image):
        image.print_method()

    def visit_table(self,table):
        table.print_method()

