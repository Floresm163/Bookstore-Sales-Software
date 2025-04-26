import datetime # import datetime module to retrieve date of sale and generate unique purchase id

class SalesTax: # calculate sales tax
  def __init__(self):
    self.taxRate = 0.0625
    self.bookPrice = bookPrice
    self.customerName = ''
    self.salesDate = ''
    self.purchaseID = ''

  def getBookPrice(self):
    while True: # validation loop to get price
      try:
        self.bookPrice = float(input("Enter item price: $"))
        if price >= 0.0:
          return bookPrice
        else:
          print("Invalid entry. Please try again")
      except ValueError:
        print("Price must be numeric. Please try again.")

  def calculateTax(self):
    return self.bookPrice * self.taxRate

  def makePurchaseID(self):
    self.customerName = input("Enter customers first and last name: ").strip()
    now = datetime.datetime.now()
    self.salesDate = '%02d%02d%02d%02d%02d%02d' %(now.hour, now.minute, now.second, now.month, now.day, now.year)
    self.purchaseID = self.salesDate + self.customerName
    return self.purchaseID
