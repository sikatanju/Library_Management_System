# This class is to store all the information of our program.

from output_class import Output
from input_class import TakeInput
from message import Message


class Inventory:
    def __init__(self):
        self.take_input = TakeInput()
        self.output_obj = Output()
        self.message_obj = Message()
        self.book_list = self.take_input.load_book_list()
        self.lent_list = self.take_input.load_lent_list()

    def save_a_book(self, book_obj):
        self.book_list.append(book_obj)
        self._update_book_list()

    def print_all_books(self):
        if len(self.book_list) == 0:
            print("\nThere are no books in the library right now.\n")
            return

        print("\nPrinting all the book details: ")
        self._print_book_list(self.book_list)

    def _print_book_list(self, book_list):
        print("--------------------------------")
        i = 1
        for book in book_list:
            print(f"Book no.{i} :")
            self.output_obj.print_book_details(book)
            i += 1
            print("--------------------------------")

        print('\n')

    def print_all_lent_list(self):
        if len(self.lent_list) == 0:
            print("\nCurrently, the lent list is empty. :(\n")
            return

        print("\nPrinting lent list with contact details: ")
        self._print_lent_list(self.lent_list)

    def _print_lent_list(self, lent_list):
        print("--------------------------------")
        i = 1
        for lent in lent_list:
            print(f"Lent no.{i} :")
            self.output_obj.print_lent_details(lent)
            i += 1
            print("--------------------------------")

        print("\n")

    def search_book(self, book_key):
        temp_book_list = self._search_book(book_key)

        if len(temp_book_list) == 0:
            print("There are no matching books. :(")
            return

        print("\nList of matching books: ")
        self._print_book_list(temp_book_list)

    def _search_book(self, book_key):
        temp_book_list = []
        book_key = book_key.strip()
        # * If searched with isbn number, then look for that specific book only, since isbn number is unique.
        if book_key.isnumeric():
            for book in self.book_list:
                if book['isbn_number'] == book_key:
                    temp_book_list.append(book)
        else:
            book_key = book_key.lower()
            for book in self.book_list:
                for value in book:
                    # If only a part of the author's name is given as input, we'll search for that book.
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
                    # Similarly, even a part of the book's name is give, we'll search for that book.
                    elif value == 'book_name':
                        if book_key == book[value].lower():
                            temp_book_list.append(book)
                            break
                        else:
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
                        if book_key == book[value]:
                            temp_book_list.append(book)
                            break

        return temp_book_list

    def remove_a_book(self, book_key):
        list_of_books = self._search_book(book_key)

        if len(list_of_books) == 0:
            print("\nThere are no matching books. :(\n")
            return

        print("\nMatched book: ")
        while True:
            try:
                self.print_book(list_of_books)
                book_no = int(input("Enter the book no. to remove the book: "))
                if book_no > len(list_of_books) or book_no < 1:
                    print("Enter a valid number from the book list.")
                    continue

                book_obj = list_of_books[book_no-1]
                self.book_list.remove(book_obj)
                self._update_book_list()
                print("\nBook removed successfully.\n")
                break

            except ValueError:
                print("Please enter a valid book no. from the above list to remove the book.")

    def lent_a_book(self):
        print("\nLent a book:\n-----------------\n")
        while True:
            try:

                option = int(input(self.message_obj.lent_message))
                if option == 1:
                    temp_book_list = self._search_book(input("\nEnter book name, author name or isbn to search books: "))
                    print("All the matching books: ")
                    self._print_book_list(temp_book_list)
                    check = self._handle_lent_book(temp_book_list)
                    if check:
                        break
                elif option == 2:
                    self.print_all_books()
                    check = self._handle_lent_book(self.book_list)
                    if check:
                        break
                elif option == 3:
                    print('\n\n')
                    return
            except ValueError:
                print("Please enter a valid number !")

    def _handle_lent_book(self, book_list):
        book_no = -1
        while True:
            try:
                book_no = int(input("Enter the book no. to lent: "))
                if book_no < 1 or book_no > len(book_list):
                    print("Enter a valid book no from above list: ")
                else:
                    break
            except ValueError:
                print("Enter a valid book no from above list: ")

        book_index = self.book_list.index(book_list[book_no-1])
        if self.book_list[book_index]['quantity'] < 1:
            print("\nSorry, the selected book isn't available for lent.\nPlease search for another book.")
            return False
        else:
            book_details = self.book_list[book_index]
            contact_details = self.take_input.get_contact_details()
            self.book_list[book_index]['quantity'] -= 1
            self._update_book_list()
            self.save_lented_book(book_details, contact_details)
            print("\nBook lent successfully.\n")
            return True

    def save_lented_book(self, book_details, contact_details):
        lent_info = {}
        lent_info['book_name'] = book_details['book_name']
        lent_info['author'] = book_details['author']
        lent_info['isbn_number'] = book_details['isbn_number']
        lent_info['contact_name'] = contact_details['contact_name']
        lent_info['contact_email'] = contact_details['contact_email']

        self.lent_list.append(lent_info)
        self._update_lent_list()

    def _update_book_list(self):
        with open('data/book_list.csv', 'w+t') as file:
            for book in self.book_list:
                strr = self.get_formatted_book(book)
                file.write(strr)

    def _update_lent_list(self):
        with open('data/lent_list.csv', 'w+t') as lent_file:
            for lent in self.lent_list:
                lent_csv = self.get_formatted_lent_info(lent)
                lent_file.write(lent_csv)

    def get_formatted_book(self, book):
        strr = f"{book['book_name']},q,"
        for temp_author in book['author']:
            strr += f"{temp_author},"

        strr += 'q,'
        strr += f"{book['isbn_number']},{book['publishing_year']},{book['price']},{book['publishing_house']},{book['quantity']}"
        strr += "\n"
        return strr

    def get_formatted_lent_info(self, lent):
        strr = f"{lent['book_name']},q,"
        for temp_author in lent['author']:
            strr += f"{temp_author},"

        strr += 'q,'
        strr += f"{lent['isbn_number']},{lent['contact_name']},{lent['contact_email']}\n"
        return strr