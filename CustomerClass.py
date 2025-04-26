class Customer: # get customer information
  customerName = getName()
  customerAddress = getAddress()
  customerDateofBirth = getDateofBirth()
  customerEmail = getEmail()
  customerPhone = getPhone()
      
  def getName(): # get customers name
    name = input("Enter name: ")
    return name

  def getAddress(): # get customers address
    address = input("Enter address: ")
    return address
    
  def getDateofBirth(): # get customers date of birth
    dateofBirth = input("Enter date of birth: ")
    return dateofBirth
    
  def getEmail(): # get customers email
    email = input("Enter eMail: ")
    return email
  
  def getPhone(): # get customers phone number
    customerPhone = int(input("Enter phone number: "))
    return customerPhone

