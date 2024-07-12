# This class is to take input from the user
from book import Book
from message import Message


class TakeInput:
    def __init__(self):
        self.message = Message()

    def add_a_book(self) -> Book:
        print("Please enter the details of the book.")
        book_name = input("1. Please enter the name of the book : ")
        authors = []
        self.message.print_author_msg()
        while True:
            msg: str = input("Enter author's name (press 'q' to stop): ")
            if msg == "q":
                break
            else:
                authors.append(msg)

        isbn = input("4. Enter the isbn number of the book: ")
        year = int(input("3. Enter the publishing year: "))
        genre = input("5. Enter the name of the publishing house: ")

        return Book(book_name, authors, isbn, year, genre)

