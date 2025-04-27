class ThirdPartyPayment:

# Creating an empty list to add customer's payment method
  def_init_(self):
    self.paymentMethods = []

# Includes a new payment method if valid
  def addPaymentMethod(self,paymentType: str) -> str:
    if paymentType:
      self.paymentMethods.append(paymentType)
      print ( f'Payment method {paymentType} added succesfully')
    else:
      print('Invalid Payment method')


# Removes an existing payment method if found
  def removePaymentMethod(self,paymentType: str) -> str:
    if paymentType in self.paymentMethods:
      self.paymentMethods.remove(paymentType)
      print( f'Payment method {paymentType} removed successfully')
    else:
      print('Payment method not found')


# Shows the list of existant payment methods 
  def listPaymentMethods(self):
    if not self.paymentMethods:
      print('No payment methods added')
    else:
      return self.paymentMethods


# Validating if the payment method exists
  def validatePayment(self,paymentType:str) -> bool:
    if paymentType in self.paymentMethods:
      return True
    else:
      return False


# Provides processing of payment 
  def preocessPayement(self,paymentType:str, among: float) -> str:
    if self.validatePayment(paymentType):
      print(f'Payment of ${amount:.2f} processed successfully with {paymentType}')
    else:
      print('Invalid payment method. Please choose a valid method')
    
      
