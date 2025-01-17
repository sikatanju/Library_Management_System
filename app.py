# ** Main program to run the `Library Management System`

from message import Message
from output_class import Output
from input_class import TakeInput
from inventory import Inventory


class LibraryManagementSystem:

    def __init__(self):
        self.message_obj = Message()
        self.output_obj = Output()
        self.take_input_obj = TakeInput()
        self.inventory = Inventory()

    def run_program(self):
        print("\n### Welcome to Library Management System.")
        while True:
            self.output_obj.print_messages(self.message_obj.get_main_messages())
            try:
                msg =  int(input("Enter the number: "))
                if msg == 1:
                    book_obj = self.take_input_obj.add_a_book()
                    self.inventory.save_a_book(book_obj)
                elif msg == 2:
                    self.inventory.print_all_books()
                elif msg == 3:
                    self.inventory.search_book_by_book_name_isbn(input("Enter the book title or ISBN number: "))
                elif msg == 4:
                    self.inventory.search_book_by_author(input("Enter the author's name: "))
                elif msg == 5:
                    self.inventory.remove_a_book(input("Enter the book title, author or isbn to search and remove the book: "))
                elif msg == 6:
                    self.inventory.lent_a_book()
                elif msg == 7:
                    self.inventory.print_all_lent_list()
                elif msg == 8:
                    self.inventory.return_lent_book()
                elif msg == 9:
                    self.inventory.print_all_returned_lent_list()
                elif msg == 0:
                    break
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("\nInput is invalid, enter a valid number.\n")

# * Learned this bit for Python Crash course book.
if __name__ == '__main__':
    lms = LibraryManagementSystem()
    lms.run_program()