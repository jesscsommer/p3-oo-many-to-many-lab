class Author:

    all = []
    
    def __init__ (self, name):
        self.name = name
        type(self).all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.author == self]
    
    def books(self):
        return [c.book for c in Contract.all if c.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        all_royalties = [c.royalties for c in Contract.all if c.author == self]
        return sum(all_royalties)


class Book:

    all = []
    
    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.book == self]
    
    def authors(self):
        return [c.author for c in Contract.all if c.book == self]


class Contract:
    
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)
       
    @property 
    def author(self):
        return self._author 
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value 
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value 
    
    @property
    def date(self):
        return self._date
    
    @date.setter 
    def date(self, value):
        if not type(value) == str:
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not type(value) == int: 
            raise Exception
        self._royalties = value 

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key = lambda i: i.date)