class BookListing:
    #Constructor to initialize a book listing (added to created book and set values)
    def __init__(self, bookID: int, bookPublishing: str, bookPublishedDate: str, bookPrice: float):
        self.bookID = bookID
        self.bookPublishing = bookPublishing
        self.bookPublishedDate = bookPublishedDate
        self.bookPrice = bookPrice

    #Getter for bookID
    def getBookID(self) -> int:
        return self.bookID

    #Getter for bookPublishing
    def getBookPublishing(self) -> str:
        return self.bookPublishing

    #Getter for bookPublishedDate
    def getPublishingDate(self) -> str:
        return self.bookPublishedDate

    #Setter for bookPrice
    def setPrice(self, newPrice: float):
        self.bookPrice = newPrice

    #Get current price(added for get price)
    def getPrice(self) -> float:
        return self.bookPrice
