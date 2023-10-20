class Author:
    def __init__(self, author_name):
        self.author_name = author_name

    def __repr__(self):
        return f"Author name: {self.author_name}"

    def print_instance(self):
        print(f"Author name: {self.author_name}")