# ** This class is to manage all the message we need to make command line interface more interactive

class Message:
    def __init__(self):
        self.messages = [
            "Press `1` to add a book to the library.",
            "Press `2` to print all the books in the library.",
            "Press `3` to search for a book by `book name` or `isbn`.",
            "Press `4` to search for a book by `author`.",
            "Press `5` to remove a book.",
            "Press `6` to lend a book.",
            "Press `7` to print all lent books.",
            "Press `8` to return a lent book.",
            "Press `9` to print all returned lent book.",
            "Press `0` to exit the program."
        ]
        self.author_msg = 'In case of one author, after entering the author\'s name and press `q`\nIf there are more than one author, enter their name one by one, then press `q` to finish'
        self.lent_message = "Press `1` to search for a book.\nPress `2` to show all books.\nPress `3` to cancel.\nEnter the number: "