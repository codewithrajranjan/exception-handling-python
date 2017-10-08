# defining own exceptions

class BookNotAvailable(Exception):
    def __init__(self,bookId):
        self.bookId = bookId 


def findBook(bookId):
    print("finding book")
    raise BookNotAvailable(bookId)


try :

    findBook(12345)

except BookNotAvailable as e:
    print("Book with id : {}  is not available".format(e.bookId))

