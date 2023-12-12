from models.SectionClass import Section


class Book(Section):
    def __init__(self, book_title):
        super().__init__(book_title)
        self.author = None
        self.elements=[]

    def print_instance(self):
        print(f"Book: {self.get_section_name()}\n\n"+"Authors")
        self.author.print_author()
        print()
        super().print_method(print_section_name=False)

    def add_author(self, new_author):
        self.author = new_author

    def add_content(self,element_to_be_added):
        self.add(element_to_be_added)



