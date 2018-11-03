class LibraryInformationSystem(object): 
	common = 10 
	def __init__(self): 
			self.myvariable = 3 
	def myfunction(self, arg1, arg2): 
			return self.myvariable 

class Book():
	title = ''
	
class Library():
	books = []
	def add_books(self, newBooks):
		self.books = newBooks
	def add_book(self, newBook):
		self.books.append(newBook)
	def get_books(self):
		return self.books

book_1 = Book()
book_1.title = 'History of Libraries in Nigeria'
book_2 = Book()
book_2.title = 'How Computer Networks Work'
book_3 = Book()
book_3.title = 'Learn Java in 21 Days'
our_3_books = [book_1, book_2, book_3]
library = Library()
library.add_book(our_3_books)
library_books = library.books
book_titles = map(lambda book:book.title,library_books)
print(list(book_titles))

