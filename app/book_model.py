library = []


class Book:
    """
    This inputs, manipulates and stores data of the book(s)
    """
    def __init__(self):
        self.library = library
        self.book_info = {}

    def delete_book(self, id):
        for book in library:
            if book['ID'] == id:
                library.remove(book)

        return "book removed successfully, {} books remaining".format(len(library))

    def add_book(self, title, author, id, publisher, number_of_books):
        self.book_info['Title'] = title
        self.book_info['Author'] = author
        self.book_info['ID'] = id
        self.book_info['Publisher'] = publisher
        self.book_info['Number of books available'] = number_of_books
        library.append(self.book_info)
        return self.book_info

    def view_all_available_books(self):
        if len(library) == 0:
            return "No books available for now, please\n check back latter"
        else:
            return library

    def modify_book_information(self, value):
        for book in library:
            if book['ID'] == value:
                option = input("Enter t, a, p or n to change title, author, publisher or number of books respectively")
                if option == 't':
                    new_title = input("Please enter a new book name")
                    book["Title"] = new_title
                elif option == 'a':
                    new_author_name = input("You can now enter a new book name")
                    book["Author"] = new_author_name
                elif option == 'p':
                    new_publisher = input("You can now enter a new publisher name for the book")
                    book["Publisher"] = new_publisher
                elif option == 'n':
                    new_number_of_books = input("You can now enter a new book name")
                    book["Number of books available"] = new_number_of_books
                else:
                    return "Wrong input option for change"
            else:
                return "Book to change is not available in the library"

    def get_a_particular_book(self, id):
        for book in library:
            if book['ID'] == id:
                return book
            else:
                return "The book you want is not in the library, try another one"








