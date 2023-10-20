from BookClass import Book
from AuthorClass import Author

discoTitanic = Book("Disco Titanic")
author = Author("Radu Pavel Gheo")

discoTitanic.add_author(author)
indexChapterOne = discoTitanic.create_chapter("Capitolul 1")
indexChapterOne = discoTitanic.create_chapter("Capitolul 2")
indexChapterOne = discoTitanic.create_chapter("Capitolul 3")
chp1 = discoTitanic.get_chapter(indexChapterOne)
#print(chp1)
indexSubChapterOneOne = chp1.create_sub_chapter("Subcapitolul 1.1")
indexSubChapterOneOne = chp1.create_sub_chapter("Subcapitolul 1.2")
scOneOne = chp1.get_sub_chapter(indexSubChapterOneOne)
#print(scOneOne)

scOneOne.create_new_paragraph("Paragraph 1")
scOneOne.create_new_paragraph("Paragraph 2")
scOneOne.create_new_paragraph("Paragraph 3")
scOneOne.create_new_image("Image 1")
scOneOne.create_new_paragraph("Paragraph 4")
scOneOne.create_new_table("Table 1")
scOneOne.create_new_paragraph("Paragraph 5")

scOneOne.print_instance()
print("\n")
discoTitanic.print_instance()