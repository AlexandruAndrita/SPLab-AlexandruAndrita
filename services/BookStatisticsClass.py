from models.VisitorClass import Visitor


class BookStatistics(Visitor):
    def __init__(self):
        self.number_images = 0
        self.number_tables = 0
        self.number_paragraphs = 0

    def visit_book(self,book):
        pass

    def visit_section(self,section):
        section.print_method()

    def visit_table_of_contents(self,table_of_contents):
        pass

    def visit_paragraph(self,paragraph):
        self.number_paragraphs +=1

    def visit_image_proxy(self,image_proxy):
        self.number_images += 1

    def visit_image(self,image):
        self.number_images += 1

    def visit_table(self,table):
        self.number_tables += 1

    def __repr__(self):
        output_string = "Book Statistics:\n" + f"*** Number of images: {self.number_images}\n" + f"*** Number of tables: {self.number_tables}" + f"*** Number of paragraphs: {self.number_paragraphs}"
        return output_string

    def print_statistics(self):
        print("Book Statistics:")
        print(f"*** Number of images: {self.number_images}")
        print(f"*** Number of tables: {self.number_tables}")
        print(f"*** Number of paragraphs: {self.number_paragraphs}")

