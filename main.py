from models.ParagraphClass import Paragraph
from models.SectionClass import Section
from models.ImageProxyClass import ImageProxy
from models.ImageClass import Image
from models.TableClass import Table
from services.RenderContentVisitorClass import RenderContentVisitor
from services.BookStatisticsClass import BookStatistics
from models.BookClass import Book
from services.TableOfContentUpdateClass import TableOfContentUpdate


cap1 = Section("Capitolul 1")
p1 = Paragraph("Paragraph 1")
cap1.add(p1)

p2 = Paragraph("Paragraph 2")
cap1.add(p2)

p3 = Paragraph("Paragraph 3")
cap1.add(p3)

p4 = Paragraph("Paragraph 4")
cap1.add(p4)

cap1.add(ImageProxy("ImageOne"))
cap1.add(Image("ImageTwo"))
cap1.add(Paragraph("Some text"))
cap1.add(Table("Table 1"))

"""
Testing for the first time just with printing
"""
print("Testing for the first time just with printing\n")
r = RenderContentVisitor()
cap1.accept(r)
print("\n\n")

"""
Testing the stats
"""
print("Testing the stats\n")
stats = BookStatistics()
cap1.accept(stats)
stats.print_statistics()
print("\n\n")

"""
Testing the Table of Contents
"""

b = Book("The book")
cap1 = Section("Chapter 1")
cap11 = Section("Subchapter 1.1")
cap2 = Section("Chapter 2")

cap1.add(Paragraph("Paragraph 1"))
cap1.add(Paragraph("Paragraph 2"))
cap1.add(Paragraph("Paragraph 3"))

cap11.add(ImageProxy("ImageOne"))
cap11.add(Image("ImageTwo"))

cap2.add(Paragraph("Paragraph 4"))

cap1.add(cap11)
cap1.add(Paragraph("Some text"))
cap1.add(Table("Table 1"))

b.add_content(cap1)
b.add_content(cap2)

print("Testing the Table of Contents\n")
tocUpdate = TableOfContentUpdate()
b.accept(tocUpdate)
tocUpdate.get_toc().accept(RenderContentVisitor())
