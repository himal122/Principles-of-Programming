class Book:
    def __init__(self, title, pages):
        self.__title = title
        self.__pages = pages

    def set_title(self, title):
        if 1 <= len(title) <= 100:
            self.__title = title
        else:
            print("Title must be between 1 to 100 characters.")

    def get_title(self):
        return self.__title

    def set_pages(self, pages):
        if 1 <= pages <= 10000:
            self.__pages = pages
        else:
            print("Number of pages must be between 1 and 10000.")

    def get_pages(self):
        return self.__pages

    def display(self):
        print(f"Book Title: {self.__title}, Pages: {self.__pages}")

# User input for book title
is_valid_title = False
while not is_valid_title:
    book_title = input("Enter book title: ")
    if 1 <= len(book_title) <= 100:
        is_valid_title = True
    else:
        print("Title must be between 1 to 100 characters.")

# User input for number of pages
is_valid_pages = False
while not is_valid_pages:
    try:
        book_pages = int(input("Enter number of pages: "))
        if 1 <= book_pages <= 10000:
            is_valid_pages = True
        else:
            print("Number of pages must be between 1 to 10000.")
    except ValueError:
        print("Please enter a valid number for the number of pages.")

# Create object
my_book = Book(book_title, book_pages)


print("\nInitial book information:")
my_book.display()


my_book.set_title("New Title")
my_book.set_pages(300)


print("\nUpdated book information:")
my_book.display()

