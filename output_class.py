# This class is to manage all the output for the project.

class Output:
    def __init__(self):
        pass

    def print_messages(self, messages):
        for message in messages:
            print(message)

    def print_a_message(self, message):
        print(message)

    def print_book_details(self, book):
        for value in book:
            if value == 'book_name':
                print('Book name        : ', book[value])
            elif value == 'author':
                print("Author(s)        :  ", end='')
                author_len = len(book[value])
                for i in range(author_len):
                    if book[value][i] == 'q':
                        pass
                    if i == author_len-1:
                        print(f'{book[value][i]}')
                    else:
                        print(f'{book[value][i]}, ', end='')

            elif value == 'isbn_number':
                print("ISBN number      : ", book[value])
            elif value == 'price':
                print("Price            : ", book[value])
            elif value == 'publishing_year':
                print("Publishing Year  : ", book[value])
            # elif value == 'quantity':
            #     print("Quantity         : ", book[value])
            elif value == 'publishing_house':
                print("Publishing House : ", book[value])

    def print_lent_details(self, lent):
        print('Book name        : ', lent['book_name'])
        print("Author(s)        :  ", end='')
        for i in range(len(lent['author'])):
            if lent['author'][i] == 'q':
                continue
            elif i == len(lent['author'])-1:
                print(f'{lent['author'][i]}')
            else:
                print(f'{lent['author'][i]},', end='')

        print("ISBN number      : ", lent['isbn_number'])
        print("Contact Name     : ", lent['contact_name'])
        print("Contact Email    : ", lent['contact_email'])