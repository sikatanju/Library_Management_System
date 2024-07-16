# This class is to take input from the user

from message import Message
from output_class import Output


class TakeInput:
    def __init__(self):
        self.message = Message()
        self.output_obj = Output()

    def add_a_book(self):
        print("Please enter the details of the book.")
        book_details = {}
        book_details['book_name'] = input("1. Please enter the name of the book : ")
        authors = []
        self.output_obj.print_a_message(self.message.author_msg)
        while True:
            msg: str = input("Enter author's name (press 'q' to stop): ")
            if msg == "q":
                break
            else:
                authors.append(msg)

        book_details['author'] = authors
        book_details['isbn_number'] = input("3. Enter the isbn number of the book: ")
        book_details['publishing_year'] = input("4. Enter the publishing year: ")
        while True:
            try:
                book_details['price'] = float(input("5. Enter the price of the book: "))
                break
            except ValueError:
                print("Book price should be a floating number")
        book_details['publishing_house'] = input("6. Enter the name of the publishing house: ")
        while True:
            try:
                book_details['quantity'] = int(input("7. Enter the quantity of the book: "))
                break
            except ValueError:
                print("The quantity of the book should be a number.")

        return book_details

    def load_book_list(self):
        book_list = []
        with open('data/book_list.csv', 'r') as load_file:
            for line in load_file.readlines():
                temp_book = {}
                split_line = line.strip().split(',')
                index = 0
                temp_book['book_name'] = ""
                while split_line[index] != 'q':
                    temp_book['book_name'] += split_line[index]
                    index += 1

                index += 1
                temp_book['author'] = []
                while split_line[index] != 'q':
                    temp_book['author'].append(split_line[index])
                    index += 1

                index += 1
                temp_book['isbn_number'] = split_line[index]
                index += 1
                temp_book['publishing_year'] = split_line[index]
                index += 1
                temp_book['price'] = float(split_line[index])
                index += 1
                temp_book['publishing_house'] = split_line[index]
                index += 1
                temp_book['quantity'] = int(split_line[index])

                book_list.append(temp_book)

        return book_list

    def load_lent_list(self):
        return self._load_lent_list('data/lent_list.csv')

    def lead_returned_lent_list(self):
        return self._load_lent_list('data/returned_lent_book_list.csv')

    def _load_lent_list(self, data_path):
        lent_list = []
        with open(data_path, 'r') as lent_file:
            for line in lent_file.readlines():
                temp_lent = {}
                split_line = line.strip().split(',')
                index = 0
                temp_lent['book_name'] = ""
                while split_line[index] != 'q':
                    temp_lent['book_name'] += split_line[index]
                    index += 1

                index += 1
                temp_lent['author'] = []
                while split_line[index] != 'q':
                    temp_lent['author'].append(split_line[index])
                    index += 1

                index += 1
                temp_lent['isbn_number'] = split_line[index]
                index += 1
                temp_lent['contact_name'] = split_line[index]
                index += 1
                temp_lent['contact_email'] = split_line[index]
                lent_list.append(temp_lent)

        return lent_list

    def get_contact_details(self):
        contact = {}
        print("Enter contact details: ")
        contact['contact_name'] = input("Enter full name: ")
        contact['contact_email'] = input("Enter contact email: ")
        return contact
