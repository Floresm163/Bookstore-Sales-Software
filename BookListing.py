class BookListing:

    def __init__(self, bookID: int, bookPublishing: str, bookPublishedDate: str, bookPrice: float):

        self.bookID = bookID
        self.bookPublishing = bookPublishing
        self.bookPublishedDate = bookPublishedDate
        self.bookPrice = bookPrice

    def getBookID(self) -> int:
        """Returns the ID of the book."""
        return self.bookID

    def getBookPublishing(self) -> str:
        """Returns the publisher of the book."""
        return self.bookPublishing

    def getBookPublishedDate(self) -> str:
        """Returns the publication date of the book."""
        return self.bookPublishedDate

    def setPrice(self, newPrice: float) -> None:
        """Sets the price of the book. Ensures price is non-negative."""
        if newPrice >= 0:
            self.bookPrice = newPrice
        else:
            print("Price cannot be negative!")

    def getPrice(self) -> float:
        """Returns the price of the book."""
        return self.bookPrice
