# defining own exceptions

class BookNotAvailable(Exception):
    pass


class DuplicateBook(Exception):
    pass


def findBook():
    print("finding book")
    raise BookNotAvailable

def addBook():
    print("Adding book")
    raise DuplicateBook

try :

    #findBook()
    addBook()

except BookNotAvailable:
    print("Book you are trying to find is not available")

except DuplicateBook:
    print("Trying to add a book that is already available")

