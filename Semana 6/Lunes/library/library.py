class Book:

    def __init__(self, id, name,quantity):
        self.id = id 
        self.name = name
        self.quantity = quantity

    def show(self):
        print(f"Id: {self.id} - Name: {self.name} - Quantity: {self.quantity}")

class Library:

    def __init__(self, id, name, books):
        self.id = id
        self.name = name 
        self.books = books

    def sell_books(self, id):
        book = self.search_book(id)
        if book:
            print("The book selected is:")
            book.show()

    def loan_books(self):
        pass

    def add_book(self):
        pass

    def show_books(self):
        for book in self.books:
            book.show()

    def remove_book(self):
        pass

    def search_book(self, id):
        for book in self.books:
            if id == book.id:
                return book
        return None
