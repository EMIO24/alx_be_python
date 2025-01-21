def __init__(self):
    pass
class Book:
    def __init__(self, title, author, _is_checked_out, _books):
        self.title = title
        self.author = author
        self._is_checked_out = True
        
class Library(Book):
    def __init__(self, _books):
        self._books = []
        
    def add_book(self):
        self._books.append(Book)
    
    def check_out_book(self, title):
        for self.title in self._books:
            if self.title == title:
                if self._is_checked_out is False:
                    self._books.remove(title)
            else:
                return 'unavailable'
    def return_book(self):
        for title in self._books:
            if self.title != title:
                if self._is_checked_out is True:
                    self._books.append(self)
    def list_available_books(self):
        return self._books
    