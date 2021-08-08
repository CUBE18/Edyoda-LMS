import sys
from Book import Book
from Catalog import Catalog
from Librarian import Librarian
from Member import Member
from Library import Library


b1 = Book("an","nn","12",47)
b2 = Book("21","n123n","122",41237)
print(Book.get_all_books())


library = Library(5,5)
library.add_book_to_rack(b1,1,1234)
library.add_book_to_rack(b1,1,3455)
library.remove_book_from_rack(1234)

member1 = Member("shamanth","Banglore",22,889128319,123123,library)
member2 = Member("Usha","Banglore",22,8899788789,123124,library)