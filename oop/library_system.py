class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

        
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        
    def __str__(self):
        return f"{super().__str__()}, File Size: {self.file_size} MB"
    
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count 
        
    def __str__(self):
        return f"{super().__str__()}, Pages: {self.page_count}"        
class Library:
    def __init__(self, books):
        self.books = []
        
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append()
            
    def list_books(self):
        print(Book)
        