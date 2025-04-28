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

# Getting the customers email
  def getCustomerEmail(self) -> str:
    return self.customerEmail

# Customer Inputting their pre-order details
  def addPreorder(self) -> str:
    self.bookID = int(input("Enter book ID to Pre-Order: "))
    self.customerName = input("Enter customer name: ")
    self.customerEmail = input ("Enter customer email: ")
    return "Pre-Order placed succeeefully"
