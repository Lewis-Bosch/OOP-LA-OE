class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("1922", "Bronny")

book1.display_info()

del book1.author

try:
    print(book1.author)
except AttributeError:
    print("The author attribute has been deleted.")

book2 = Book("Happy Death Day", "Mariah Hill")

book2.display_info()