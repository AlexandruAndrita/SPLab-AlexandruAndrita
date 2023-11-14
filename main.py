from BookClass import Book
from SectionClass import Section
from ImageProxyClass import ImageProxy
import time

startime = time.time()

img1 = ImageProxy("Pamela Anderson")
img2 = ImageProxy("Kim Kardashian")
img3 = ImageProxy("Kirby Griffin")

playboy1 = Section("Front Cover")
playboy1.add(img1)
playboy2 = Section("Summer Girls")
playboy2.add(img2)
playboy2.add(img3)
playboy = Book("Playboy")
playboy.add_content(playboy1)
playboy.add_content(playboy2)

stoptime = time.time()

print(f"Creation of the content book: {stoptime-startime} milliseconds")
startime = time.time()
playboy1.print_method()
stoptime = time.time()

print(f"Printing the section 1 took: {stoptime-startime} milliseconds")

startime = time.time()
playboy1.print_method()
stoptime = time.time()

print(f"Printing again the section 1 took: {stoptime-startime} milliseconds")





