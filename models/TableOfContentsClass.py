from models.ElementClass import Element


class TableOfContents(Element):
    def __init__(self):
        self.list_strings = []

    def print_table_of_contents(self):
        for element in self.list_strings:
            print(element)

    def add_element(self, element):
        self.list_strings.append(element)

    def accept(self,visitor):
        visitor.visit_table_of_contents(self)