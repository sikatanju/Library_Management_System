# This class is to store all the information of our program.

from output_class import Output
from input_class import TakeInput
from message import Message


class Inventory:
    def __init__(self):
        self.take_input = TakeInput()
        self.output_obj = Output()
        self.message_obj = Message()
        self.book_list = self.take_input.load_all_books()
        self.lent_list = []

    def save_a_book(self, book_obj):
        self.book_list.append(book_obj)
        self._update_book_list()

    def print_all_books(self):
        if len(self.book_list) == 0:
            print("\nThere are no books in the library right now.\n")
            return

        print("\nPrinting all the book details: ")
        self.print_book(self.book_list)

    def search_book(self, book_key):
        temp_book_list = self._search_book(book_key)

        if len(temp_book_list) == 0:
            print("There are no matching books. :(")
            return

        print("\nList of matching books: ")
        self.print_book(temp_book_list)

    def _search_book(self, book_key):
        temp_book_list = []
        book_key = book_key.strip()
        book_key = book_key.lower()
        for book in self.book_list:
            for value in book:
                if value == 'author':
                    check = False
                    for temp_author in book[value]:
                        if book_key == temp_author.lower():
                            temp_book_list.append(book)
                            check = True
                            break
                        else:
                            temp_check = False
                            author_name = temp_author.split()
                            for temp_short_author in author_name:
                                if temp_short_author.lower() == book_key:
                                    temp_book_list.append(book)
                                    check = True
                                    temp_check = True
                                    break

                            if temp_check:
                                break

                    if check:
                        break
                elif value == 'book_name':
                    check = False
                    splitted_book_name = book[value].split()
                    for split_book_name in splitted_book_name:
                        if book_key == split_book_name.lower():
                            temp_book_list.append(book)
                            check = True
                            break
                    if check:
                        break
                else:
                    if book_key == book[value].lower():
                        temp_book_list.append(book)
                        break

        return temp_book_list

    def print_book(self, book_list):
        print("--------------------------------")
        i = 1
        for book in book_list:
            print(f"Book no.{i} :")
            self.output_obj.output_book_details(book)
            i += 1
            print("--------------------------------")

        print('\n')

    def get_formatted_book(self, book):
        strr = f"{book['book_name']},q,"
        for temp_author in book['author']:
            strr += f"{temp_author},"

        strr += 'q,'
        strr += f"{book['isbn_number']},{book['publishing_year']},{book['publishing_house']},{book['quantity']}"
        strr += "\n"
        return strr

    def remove_a_book(self, book_key):
        list_of_books = self._search_book(book_key)

        if len(list_of_books) == 0:
            print("\nThere are no matching books. :(\n")
            return

        print("\nList of matching books: ")
        while True:
            try:
                self.print_book(list_of_books)
                book_no = int(input("Enter the book no. to remove the book"))
                if book_no > len(list_of_books) or book_no < 1:
                    print("Enter a valid number from the book list.")
                    continue

                book_obj = list_of_books[book_no-1]
                self.book_list.remove(book_obj)
                self._update_book_list()
                print("\nBook removed succesfully.\n")
                break

            except ValueError:
                print("Please Enter a valid number to remove the book")

    def _update_book_list(self):
        with open('data/book_list.csv', 'w+t') as file:
            for book in self.book_list:
                strr = self.get_formatted_book(book)
                file.write(strr)

    def lent_a_book(self):
        while True:
            try:
                option = int(input(self.message_obj.lend_message))
                if option == 1:

                    temp_book_list = self._search_book(input("\nEnter book name, author name or isbn to search for available books: "))
                    print("All the matching books: ")

                    self.print_book(temp_book_list)
                    book_no = int(input("Enter the book no. to lent: "))

                    book_index = self.book_list.index(temp_book_list[book_no-1])
                    contact_details = self.take_input.get_contact_details()

                    if self.book_list[book_index]['quantity'] >= 1:
                        self.book_list[book_index]['quantity'] -= 1
                        print("Book lent successfully")
                    else:
                        print("Sorry, book isn't available.")

                elif option == 2:
                    pass

            except ValueError:
                print("Please enter a valid number !")

    def save_lented_book(self, lent_info):
        self.lent_list(lent_info)

    def _update_lented_list(self):
        with open('data/lent_list.csv', 'w+t') as lent_file:
            for lent in self.lent_list:
                lent_csv = self.get_formatted_lent_info(lent)
                lent_file.write(lent_csv)

    def get_formatted_lent_info(self, lent):
        pass