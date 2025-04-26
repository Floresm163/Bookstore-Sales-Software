class SalesTax: # calculate sales tax
  def __init__(self, tax):
    self.tax = salestax

  def getBookPrice(self): # get the base price of the book
    while True: # start input validation for the price
      try:
        bookPrice = float(input("Enter the base price: $"))
        if bookPrice > 0: # return variable if it is a positive, non-zero integer.
          return bookPrice
        else:
          print("Invalid entry. Base price must be an integer that is positive and non-zero.")
      except ValueError: # catch non-integer entries
          print("Invalid entry. Base price must be an integer.")

  def calculateTax(self, bookPrice): #calculate the sales
    calculatedTax = base_price + (base_price * tax)
    return calculatedTax

  @staticmethod # generate some kind of ID to attach to sale
  def makePurchaseID():
