from SubChapterClass import SubChapter


class Chapter:
    def __init__(self, chapter_name):
        self.chapter_name = chapter_name
        self.subchapters = []

    def __repr__(self):
        return f"Chapter name: {self.chapter_name}"

    def print_instance(self):
        print(f"Chapter name: {self.chapter_name}")
        for i in range(len(self.subchapters)):
            self.subchapters[i].print_instance()

    def get_length_subchapters(self):
        return len(self.subchapters)

    def create_sub_chapter(self, new_subchapter_name):
        current_length = self.get_length_subchapters()

        new_subchapter = SubChapter(new_subchapter_name)
        self.subchapters.append(new_subchapter)

        return current_length

    def get_sub_chapter(self, index):
        if self.subchapters[index] is None:
            raise IndexError(f"The index provided {index} does not exist.")
        return self.subchapters[index]