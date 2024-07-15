# ** This class is to manage all the message we need to make command line interface more interactive

class Message:
    def __init__(self):
        self.messages = [
            "Press `1` to add a book to the library.",
            "Press `2` to show all the book in the library.",
            "Press `3` to search for a book.",
            "Press `4` to remove a book.",
            "Press `5` to lend a book.",
            "Press `0` anytime to exit the program."
        ]
        self.author_msg = 'In case of one author, after entering the author\'s name and press `q`\nIf there are more than one author, enter their name one by one, then press `q` to finish'
        self.lent_message = "Press `1` to search for a book.\nPress `2` to show all books."

    # def print_messages(self):
    #     for message in self.messages:
    #         print(message)

    # def print_author_msg(self):
    #     print(self.author_msg)