class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        return f"Item ID: {self.item_id}\nTitle: {self.title}\nStatus: {'Checked out' if self.checked_out else 'Available'}"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out successfully."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        return f"{super().display_info()}\nType: Book\nAuthor: {self.author}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director):
        super().__init__(title, item_id)
        self.director = director

    def display_info(self):
        return f"{super().display_info()}\nType: DVD\nDirector: {self.director}"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_info(self):
        return f"{super().display_info()}\nType: Magazine\nIssue Number: {self.issue_number}"


book = Book("The Great Gatsby", 1, "F. Scott Fitzgerald")
print(book.display_info())
print(book.check_out())
print(book.return_item())

dvd = DVD("Inception", 2, "Christopher Nolan")
print(dvd.display_info())
print(dvd.check_out())

magazine = Magazine("National Geographic", 3, 250)
print(magazine.display_info())
