class PreOrder:
    # Creating a new PreOrder object when called
    def __init__(self):
        self.bookID = 0
        self.customerName = ""
        self.customerEmail = ""

    # Getting the book's ID number
    def getBookId(self) -> int:
        return self.bookID

    # Getting the name of the customer
    def getCustomerName(self) -> str:
        return self.customerName

    # Getting the customer's email
    def getCustomerEmail(self) -> str:
        return self.customerEmail

    # Customer inputting their pre-order details
    def addPreorder(self) -> str:
        try:
            self.bookID = int(input("Enter book ID to Pre-Order: "))
        except ValueError:
            return "Invalid Book ID. Pre-Order failed."
        self.customerName = input("Enter customer name: ").strip()
        self.customerEmail = input("Enter customer email: ").strip()
        return "Pre-Order placed successfully."
