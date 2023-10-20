from ElementClass import Element


class Table(Element):
    def __init__(self, table_title):
        self.table_title = table_title

    def __repr__(self):
        return f"Table title: {self.table_title}"

    def print_method(self):
        print(f"Table title: {self.table_title}")