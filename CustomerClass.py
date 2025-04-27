class Customer: # get customer information and store in dictionary
  def __init__(self): # set all variables to empty by default
    self.customerName = ''
    self.customerAddress = ''
    self.customerDateofBirth = ''
    self.customerEmail = ''
    self.customerphone = ''

def getName(self): # get customers name
  while True: # start validation loop to make sure name is not empty
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = first_name + last_name
    if name: # checks if the name has been entered, if not repeat the loop
      self.customerName = full_name
      break
    print("Invalid Entry. Please enter a valid name.")

def getAddress(self): # get customers address
  while True: 
    address = input("Enter address: ")
    if address: 
      self.customerAddress = address
      break
    print("Invalid Entry. Please enter a valid address.")
    
def getDateofBirth(self): # get customers date of birth
  while True: 
    try:
      dob = int(input("Enter date of birth in MMDDYYYY format: ")).strip()
      if len(dob) == 8: # set variable if entry is approriate length
        self.customerDateofBirth = dob
        break
      else:
        print("Invalid Entry. Please enter a valid date of birth.")
    except ValueError: # catch non-integer entries
      print("Invalid Entry. Please enter a valid date of birth.")

def getEmail(self): # get customers email
  while True: 
    email = input("Enter eMail address: ")
    if '@' in email: # basic email validation
      self.cutomerEmail = email
      break
    print("Invalid Entry. Please enter a valid email address.")
  
def getPhone(self): # get customers phone number
  while True: 
    try:
      phone = int(input("Enter phone number: ")).strip()
      if len(phone) == 10: # set variable if entry is approriate length
        self.customerPhone = phone
        break
      else:
        print("Invalid Entry. Please enter a valid phone number.")
    except ValueError: # catch non-integer entries
      print("Invalid Entry. Please enter a valid phone number.")

def addCustomer(self): # this can be removed if we want but just for the sake of convenience probably easier to get info all at once
  print('\nPlease enter customer information: ')
  self.getName
  self.getAddress
  self.getDateofBirth
  self.getEmail
  self.getPhone

