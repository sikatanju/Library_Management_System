# This class is to store all the information of our program.
# from book import Book


class Inventory:
    def __init__(self):
        self.book_list = []

    def save_a_book(self, book_obj):
        self.book_list.append(book_obj)

    def print_all_books(self):
        print("Printing all the books from Library...")

        i = 1
        print('\n----------------------------------')
        for book in self.book_list:
            print(f'Book no. {i}:')
            i += 1
            book.print_book()
