class Author:
    def __init__(self, author_name):
        self.author_name = author_name

    # def __init__(self, author_name, author_surname):
    #     self.author_name = author_name
    #     self.author_surname = author_surname

    def __repr__(self):
        # return f"Author: {self.author_name} - Author surname: {self.author_surname}"
        return f"Author: {self.author_name}"

    def print_author(self):
        # print(f"Author: {self.author_name} - Author surname: {self.author_surname}")
        print(f"Author: {self.author_name}")