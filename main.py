from BookClass import Book
from AuthorClass import Author
from SectionClass import Section
from ParagraphClass import Paragraph
from ImageClass import Image

noapteBuna = Book("Noapte buna, copii!")
#author = Author("Radu Pavel Gheo","")
author = Author("Radu Pavel Gheo")
noapteBuna.add_author(author)

cap1 = Section("Capitolul 1")
cap11 = Section("Capitolul 1.1")
cap111 = Section("Capitolul 1.1.1")
cap1111 = Section("Subchapter 1.1.1.1")

noapteBuna.add_content(Paragraph("Multumesc celor care ..."))
noapteBuna.add(cap1)

cap1.add(Paragraph("Moto capitol"))
cap1.add(cap11)


cap11.add(Paragraph("Text from subchapter 1.1"))
cap11.add(cap111)
cap111.add(Paragraph("Text from subchapter 1.1.1"))
cap111.add(cap1111)
cap1111.add(Image("Image subchapter 1.1.1.1"))

noapteBuna.print_instance()



