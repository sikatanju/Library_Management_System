# ** Main program to run the `Library Management System`
from message import Message
# from book import Book
from input_class import TakeInput
from inventory import Inventory


class LibraryManagementSystem:

    def __init__(self):
        self.message_obj = Message()
        self.take_input_obj = TakeInput()
        self.inventory = Inventory()

    def run_program(self):
        print("\n### Welcome to Library Management System.")
        while True:
            self.message_obj.print_messages()
            msg: str = input("Enter the number: ")
            if msg == "q":
                print("Program Exiting...")
                break
            try:
                msg = int(msg)
                if msg == 1:
                    book_obj = self.take_input_obj.add_a_book()
                    self.inventory.save_a_book(book_obj)
                elif msg == 2:
                    self.inventory.print_all_books()
                elif msg == 3:
                    self.inventory.search_a_book(input("Enter the book name or ISBN number: "))
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Input is invalid, enter a number or 'q' to exit.")


if __name__ == '__main__':
    lms = LibraryManagementSystem()
    lms.run_program()