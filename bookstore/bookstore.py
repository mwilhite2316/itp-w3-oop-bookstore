class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.authors = []
        self.books = []
        
    def get_books(self):
        return self.books
        
    def add_book(self, book):
        self.books.append(book)
        
    def search_books(self, title='', author=''):
        books = []
        for book in self.books:
            if title != '':
                if title.lower() in book.title.lower():
                    books.append(book)
            elif author != '':
                if book.author == author:
                    books.append(book)
        return books
        


class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books
        
        
        
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
        
   
        
    
