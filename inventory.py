# This class is to store all the information of our program.
# from book import Book
import json
from output_class import Output


class Inventory:
    def __init__(self):
        self.book_list = []
        self.output_obj = Output()

    def save_a_book(self, book_obj):
        self.book_list.append(book_obj)

    def print_all_books(self):
        print("Printing all the book details: ")
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
        print("\n--------------------------------")
        i = 1
        for book in book_list:
            print(f"Book no.{i} :")
            self.output_obj.output_book_details(book)
            i += 1
            print("--------------------------------\n")