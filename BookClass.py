from ChapterClass import Chapter


class Book:
    def __init__(self, book_title):
        self.book_title = book_title
        self.author = None
        self.chapters = []

    def __repr__(self):
        return f"Book title: {self.book_title}"

    def print_instance(self):
        print(f"Book title: {self.book_title}")
        self.author.print_instance()
        for i in range(len(self.chapters)):
            self.chapters[i].print_instance()

    def add_author(self, new_author):
        self.author = new_author

    def get_length_chapters(self):
        return len(self.chapters)

    def create_chapter(self, chapter_name):
        current_length = self.get_length_chapters()

        new_chapter = Chapter(chapter_name)
        self.chapters.append(new_chapter)

        return current_length

    def get_chapter(self, index):
        if self.chapters[index] is None:
            raise IndexError(f"The index provided {index} does not exist.")
        return self.chapters[index]