# This class is to store all the information of our program.

from output_class import Output
from input_class import TakeInput


class Inventory:
    def __init__(self):
        self.take_input = TakeInput()
        self.book_list = self.take_input.load_all_books()
        self.output_obj = Output()

    def save_a_book(self, book_obj):
        self.book_list.append(book_obj)
        with open('data/book_list.csv', 'a') as file:
            strr = self.get_formatted_book(book_obj)
            file.write(strr)



    def print_all_books(self):
        if len(self.book_list) == 0:
            print("\nThere are no books in the library right now.\n")
            return

        print("\nPrinting all the book details: ")
        self.print_book(self.book_list)

    def search_a_book(self, book_key):
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
                else:
                    if book_key == book[value].lower():
                        temp_book_list.append(book)
                        break

        if len(temp_book_list) == 0:
            print("There are no matching books. :(")
            return

        print("\nList of matching books: ")
        self.print_book(temp_book_list)

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