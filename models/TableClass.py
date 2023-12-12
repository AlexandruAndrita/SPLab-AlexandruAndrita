from models.ElementClass import Element


class Table(Element):
    def __init__(self, table_title):
        self.table_title = table_title

    def __repr__(self):
        return f"Table title: {self.table_title}"

    def print_method(self):
        print(f"Table title: {self.table_title}")

    def accept(self,visitor):
        visitor.visit_table(self)

    def get_table_title(self):
        return self.table_title

