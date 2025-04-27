class UserAccounts: # create user accounts
  def __init__(self): # create a dictionary to store account information. Set all variables to empty by default except account type which is set to customer
    self.UserAccount = {'Name': None,
                        'User Name': None,
                        'Password': None,
                        'eMail': None,
                        'Phone Number': None,
                        'Date of Birth': None,
                        'Address': None,
                        'Account Type': 1}

def getName(self): # get account owners name
  while True: # start validation loop to make sure name is not empty
    first_name = input("Enter first name: ").upper()
    last_name = input("Enter last name: ").upper()
    full_name = first_name + last_name
    if name: # checks if the name has been entered, if not repeat the loop
      self.UserAccount['Name'] = full_name
      break
    else:
      print("Invalid Entry. Enter a valid name.")

def getUserName(self): # get account users user name for login
  while True: 
    userName = input("Enter user name: ").upper()
    if userName: 
      self.UserAccount['User Name'] = userName
      break
    else:
      print("Invalid Entry. Enter a valid user name.")

def getPassword(self): # get account users password
  while True: 
    password = input('Enter a password (must be at least 8 characters): ').strip()
    if len(password) < 8:
      print("Password must be at least 8 characters long.")
      continue

    confirm = input('Confirm your password: ').strip() # make users enter password again 
    if password == confirm:
      self.UserAccount['Password'] = password
      break
    else:
      print('Invalid entry. Passwords do not match.')

def getEmail(self): # get account users email
  while True: 
    email = input("Enter eMail address: ")
    if '@' in email: # basic email validation
      self.UserAccount['eMail'] = email
      break
    print("Invalid Entry. Enter a valid email address.")

def getPhone(self): # get account users phone number
  while True: 
    phone = int(input("Enter phone number: ")).strip()
    if len(phone) == 10 and phone.isdigit(): # set variable if entry is approriate length and only numbers
      self.UserAccount['Phone'] = phone
      break
    else:
      print("Invalid Entry. Enter a valid phone number.")

def getDateofBirth(self): # get account users date of birth
  while True: 
    dob = int(input("Enter date of birth in MMDDYYYY format: ")).strip()
    if len(dob) == 8 and dob.isdigit(): # set variable if entry is approriate length
      self.UserAccount['Date of Birth'] = dob
      break
    else:
      print("Invalid Entry. Enter a valid date of birth.")

def getAddress(self): # get account users address
  while True: 
    address = input("Enter address: ")
    if address: 
      self.UserAccount['Address'] = address
      break
    print("Invalid Entry. Enter a valid address.")

def setAccountType(self): # assign the profiles designation, 1 = administrator, 2 = staff, 3 = customer
  while True: 
    try:
      accountType = int(input("Enter Account Designation (1 = Administrator, 2 = Staff, 3 = Customer): "))
      if 1 <= accountType <= 3:
        self.UserAccount['Account Type'] = accountType
        break
      else:
        print("Invalid entry. Account designation must be between 1 and 3.")
        

class ManageUserAccounts:
  def __init__(self):
    self.users = {}

  def addUserAccount(self):
    newAccount = UserAccounts()
    newAccount = UserAccounts()
    newAccount.getName()
    newAccount.getUserName()
    newAccount.getPassword()
    newAccount.getEmail()
    newAccount.getPhone()
    newAccount.getDateofBirth()
    newAccount.getAddress()

    username = newAccount.
    
    
