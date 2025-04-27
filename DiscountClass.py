class Discount:
# Creating a new Dicsount object when called
  def _init_(self,price:float):
    self.bookPrice = price
    self.discount = 0.0

# Setting the new discount 
  def setDiscount(self, newDiscount:float) -> str:
    if 0 <= newDiscount <= 1:
      self.discount = newDiscount
      print (f'Discount set to {newDiscount * 100} %')
    else:
      print ('Total discount cannot exceed 100%')

# Adding discount 
  def addDiscount(self,addDiscount:float) -> str:
    if(self.discount + self.additionalDiscount) <= 1:
      self.discount += self.additionalDiscount
      print(f'Discount increased by {additionalDiscount *100} %')
    else:
      print('Total discount cannot exceed 100%')
    

# Removes the amount of the discount 
  def removeDiscount(self, removalDiscount:float) -> str:
    if (self.discount - self.removalDiscount) >= 0:
      self.discount -= removalDiscount
      print (f'Discount decreased by {removalDiscount *100} %')
    else:
      print('Discount cannot be less then 0%')

# Calculating the final price after applying the discount
  def calculateDiscount(self)-> str:
    return self.bookPrice - (self.bookPrice * self.discount)
      
