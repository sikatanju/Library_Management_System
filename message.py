# ** This class is to manage all the message we need to make command line interface more interactive

class Message:
    def __init__(self):
        self.messages = [
            "Press `q` anytime to exit the program.",
            "Press `1` to add a book to the library.",
            "Press `2` to show all the book in the library.",
            "Press `3` to search for a book."
        ]
        self.author_msg = 'In case of one author, after entering the author\'s name and press `q`\nIf there are more than one author, enter their name one by one, then press `q` to finish'

    def print_messages(self):
        for message in self.messages:
            print(message)

    def print_author_msg(self):
        print(self.author_msg)