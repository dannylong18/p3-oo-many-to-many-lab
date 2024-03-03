class Author:
    
    all = []

    def __init__(self, name = ''):
        self.name = name

        Author.all.append(self)

    def contracts(self):
         return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
         return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
         return Contract(self, book, date, royalties)
    
    def total_royalties(self):
         return sum([contract.royalties for contract in self.contracts()])

class Book:
    
    all = []

    def __init__(self, title = ''):
        self.title = title

        Book.all.append(self)

    def contracts(self):
         return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
         return [contract.author for contract in self.contracts()]
    
class Contract:

    all = []

    def __init__(self, author, book, date = '', royalties = 0):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    def get_author(self):
        return self._author
        
    def set_author(self, author):
         if not isinstance (author, Author):
              raise Exception ('author must be instance of class Author!')
         else:
              self._author = author

    author = property(get_author, set_author)

    @property
    def book(self):
         return self._book 
    
    @book.setter
    def book (self,book):
         if not isinstance (book, Book):
                raise Exception ('book must be instance of class Book!')
         else:
              self._book = book

    @property
    def date(self):
         return self._date
    
    @date.setter
    def date(self,date):
         if not isinstance(date, str):
                raise Exception ('date must be a string!')
         else:
              self._date = date
    
    @property
    def royalties(self):
         return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
         if not isinstance(royalties, int):
              raise Exception ('royalties must be an integer!')
         else:
              self._royalties = royalties
    
    
    @classmethod
    def contracts_by_date(cls, date):
        dated_contracts = []
        for contract in cls.all:
             if contract.date == date:
                  dated_contracts.append(contract)

        return dated_contracts
    
    