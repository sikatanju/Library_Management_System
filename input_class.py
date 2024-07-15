# This class is to take input from the user
# from book import Book
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
        # self.message.print_author_msg()
        self.output_obj.print_a_message(self.message.author_msg)
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
        book_details['quantity'] = input("6. Enter the quantity of the book: ")

        return book_details

    def load_all_books(self):
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
                temp_book['publishing_house'] = split_line[index]
                index += 1
                temp_book['quantity'] = split_line[index]

                book_list.append(temp_book)

        return book_list

    def get_contact_details(self):
        contact = {}
        print("Enter contact details: ")
        contact['full_name'] = input("Enter full name: ")
        contact['age'] = input("Enter the age: ")
        contact['email'] = input("Enter email: ")
        return contact
