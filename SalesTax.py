import datetime # import datetime module to retrieve date of sale and generate unique purchase id

class SalesTax: # calculate sales tax
  def __init__(self):
    self.taxRate = 0.0625 # set taxRate to 0.625
    self.bookPrice = 0.0
    self.customerName = ''
    self.salesDate = ''
    self.purchaseID = ''

  def getBookPrice(self):
    while True: # validation loop to get price
      try:
        self.bookPrice = float(input("Enter item price: $"))
        if price >= 0.0: # return price if it is positive
          return bookPrice
        else:
          print("Invalid entry. Please try again")
      except ValueError: # catch non-float entries
        print("Price must be numeric. Please try again.")

  def calculateTax(self): # calculate sales tax, this does NOT calculate the total price, just the price of the tax itself
    return self.bookPrice * self.taxRate

  def makePurchaseID(self):
    self.customerName = input("Enter customers first and last name: ").strip()
    now = datetime.datetime.now()
    self.salesDate = '%02d%02d%02d%02d%02d%02d' %(now.hour, now.minute, now.second, now.month, now.day, now.year) # generate the sales date
    self.purchaseID = self.salesDate + self.customerName # combine the sales date and the customers name to make a unique purchase id
    return self.purchaseID
