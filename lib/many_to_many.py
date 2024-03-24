class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.all_books.append(self)


class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.all_contracts = []
        self.all_authors.append(self)

    def contracts(self):
        return self.all_contracts

    def books(self):
        return [contract.book for contract in self.all_contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        new_contract = Contract(self, book, date, royalties)
        self.all_contracts.append(new_contract)
        return new_contract

    def total_royalties(self):
        total = 0
        for contract in self.all_contracts:
            total += contract.royalties
        return total


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
