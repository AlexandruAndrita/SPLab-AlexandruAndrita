from ParagraphClass import Paragraph
from SectionClass import Section
from AlignLeftClass import AlignLeft
from AlignRightClass import AlignRight
from AlignCenterClass import AlignCenter

cap1 = Section("Capitolul 1")
p1 = Paragraph("Paragraph 1")
cap1.add(p1)

p2 = Paragraph("Paragraph 2")
cap1.add(p2)

p3 = Paragraph("Paragraph 3")
cap1.add(p3)

p4 = Paragraph("Paragraph 4")
cap1.add(p4)

print("Printing without Alignment")
print()
cap1.print_method()

p1.set_align_strategy(AlignCenter())
p2.set_align_strategy(AlignRight())
p3.set_align_strategy(AlignLeft())

print()
print("Printing with Alignment")
print()
cap1.print_method()




