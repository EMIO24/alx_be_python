class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
class Ebook(Book):
    
    def __init__(self, title, author, file_size):
        Book.__init__(self, title, author)
        self.file_size = file_size
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        Book.__init__(self, title, author)
        self.page_count = page_count 
        
class Library:
    def __init__(self, books):
        self.books = []
        
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append()
            
    def add_book(self, book):
        print(Book)
        