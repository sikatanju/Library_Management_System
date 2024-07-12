# ** A class to create & manage book

class Book:
    def __init__(self, book_name, author, isbn, year, house):
        self.book_name = book_name
        self.author = author
        self.isbn_number = isbn
        self.publishing_year = year
        self.publishing_house = house


    def print_book(self):
        print("Book name: ", self.book_name)
        print("Author(s): ", end='')
        # i = 1
        author_len = len(self.author)
        for i in range(author_len):
            if i == author_len-1:
                print(f'{self.author[i]}.')
            else:
                print(f'{self.author[i]}, ', end='')

        print("ISBN Number: ", self.isbn_number)
        print("Publishing Year: ", self.publishing_year)
        print("Publishing House: ", self.publishing_house)
        print('----------------------------------')


