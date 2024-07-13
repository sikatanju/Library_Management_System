# This class is to take input from the user
from book import Book
from message import Message


class TakeInput:
    def __init__(self):
        self.message = Message()

    def add_a_book(self):
        print("Please enter the details of the book.")
        book_details = {}
        book_details['book_name'] = input("1. Please enter the name of the book : ")
        authors = []
        self.message.print_author_msg()
        while True:
            msg: str = input("Enter author's name (press 'q' to stop): ")
            if msg == "q":
                break
            else:
                authors.append(msg)

        book_details['author'] = authors
        book_details['isbn_number'] = input("4. Enter the isbn number of the book: ")
        book_details['publishing_year'] = input("3. Enter the publishing year: ")
        book_details['publishing_house'] = input("5. Enter the name of the publishing house: ")

        return book_details

