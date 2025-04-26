class SalesTax: # calculate sales tax
  basePrice = getBookPrice()

  def getBookPrice():
    bookPrice = float(input("Enter price: "))
    return bookPrice

  def calculateTax(): #calculate the sales
    base_price = getBookPrice()
    tax = .0625
    calculatedTax = base_price + (base_price * tax)
    return calculatedTax

  @staticmethod # generate some kind of ID to attach to sale
  def makePurchaseID():
