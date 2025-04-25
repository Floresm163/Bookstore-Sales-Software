def userLogin(): # log in users
  print("1. User Login")
  print("2. Guest Login")
  while True: # validate input, keep looping until 1 or 2 is entered
        input = int(input("Select option 1 or 2: "))
        if input == 2:
            displayGuestMenu()
        elif input == 1:
            break
        else:
          print("Invalid entry. Enter 1 or 2.")
          
  while True: # validate input
    try: 
      userLogin = input("Enter UserName: ") # get user name
      userLogin.upper() # convert user name to uppercase
      userPassword = input("Enter Password: ") # get password
      with open('userList.txt', 'r') as userList: # open list of user names, passwords, and designations
        user = userList.readline() 
        password = userList.readline()
        designation = userList.readline()
        user_found = False
        while user != '':
          user = user.rstrip('\n')
          password = password.rstrip('\n')
          designation = designation.rstrip('\n')
          int(designation)
          if userLogin == user and userPassword == password: 
            user_found = True
            break
          else: 
            user = userList.readline()
            password = userList.readline()
            designation = userList.readline()
        if user_found == True:
          designationMenu(designation, user)
        else:
          print("Username or Password invalid.")
      except:
        print("File not found.")

def designationMenu(designation, username):
  if designation == 1:
    displayAdministratorMenu(username)
  elif designation == 2:
    displayStaffMenu(username)
  else:
    displayCustomerMenu(username)
    
def createProfile(): # create user profiles
  user_name = createUserName()
  password = input("Enter Password: ")
  first_name = input("Enter First Name: ")
  last_name = input("Enter Last Name: ")
  full_name = firstname.upper() + '_' + lastname.upper()
  address = input("Enter Address: ")
  email = input("Enter eMail: ")
  phone = input("Enter Phone Number: ")
  
  print("\nAccount Designations")
  print("Assign Account Designation: Administrators = 1, Staff = 2, Customers = 3")
  while True:
    try:
      user_designation = int(input("Enter the designation for account: "))
      if 0 <= user_designation <= 3:
        user_designation = str(userDesignation)
        break
      else:
        print("Designation invalid. Please enter a designation between 1-3.")
    except ValueError:
      print("Designation invalid. Please enter a designation between 1-3.")

  with open('userList.txt', 'a') as userList: # create text file to track usernames, passwords, and designations
    userList.write(f'{user_name}\n')
    userList.write(f'{password}\n')
    userList.write(f'{user_designation}\n')

  filename = (f'{user_name}')
  with open(f'{filename}.txt', 'w') as profile: # create user profile text file
    profile.write(f'{user_name}\n')
    profile.write(f'{password}\n')
    profile.write(f'{full_name}\n')
    profile.write(f'{address}\n')
    profile.write(f'{email}\n')
    profile.write(f'{phone}\n') 

def createUserName(): # this function will get the username, make sure a user with that name doesn't already exist, and convert the user name to uppercase
  while True:
      username = input("Enter username: ")
      try:
        with open('userList.txt', 'w') as userList:
          users = userList.readline()
          userDesignation = userList.readline()
          is_not_found = True
          while users != '':
            users = users.rstrip('\n')
            if username.upper() == users:
              print(f'{username} is not available. Please try another username.')
              is_not_found = False
              break
          if is_not_found:
              return username.upper()
      except:
        print("File not found.")

def displayAdministratorMenu(username):
  print(f'Hello, {username}')
  print("\nAdministrators Menu\n")
  print("1. Profile Options")
  print("2. Book Listings")
  print("3. Sales Report")
        
def displayStaffMenu():

def displayCustomerMenu():
  print("Main Menu")
  print("1. Wish List")
  print("2. Book Listings")
  print("3. Support Tickets")
  print("4. Exit")
  while True:
    try:
        user_input = int(input("Please enter a number between 1-4: "))
        if user_input == 1:
            displayUserMenu()
            break
        elif user_input == 2:
            viewBookListings()
            break
        elif user_input == 3:
            displayCustomerSupportTicketmenu():
            break
      elif user_input == 4:
            print("Goodbye")
            break
        else:
            print("Invalid entry.")
    except ValueError: # if user enters an integer
        print("Invalid entry. Please enter a number between 1-4.")

def displayGuestMenu():
  print("Main Menu")
  print("1. Book Listings")
  print("2. Exit")
  while True:
    try:
        user_input = int(input("Please enter a number between 1-2: "))
        if user_input == 1:
            viewBookListings()
            break
        elif user_input == 2:
            print("Goodbye")
            break
        else:
            print("Invalid entry.")
    except ValueError: # if user enters an integer
        print("Invalid entry. Please enter a number between 1-2.")
  
def displayWishlistMenu():
  print("Wishlist")
  print("1. Create New Wishlist")
  print("2. View Wishlist")
  print("3. Edit Wishlist")
  print("4. Return to Main Menu")
  print("5. Exit")
  while True: # input validation loop
    try:
        user_input = int(input("Please enter a number between 1-5: "))
        if user_input == 1:
            createWishlist()
            break
        elif user_input == 2:
            viewWishlist()
            break
        elif user_input == 3:
            editWishlist()
            break
        elif user_input == 4:
            displayMainMenu()
            break
      elif user_input == 5:
            print("Goodbye")
            break
        else:
            print("Invalid entry.")
    except ValueError: # if user enters an integer
        print("Invalid entry. Please enter a number between 1-5.")
  

def displayBooklisting():
def createWishlist():
def viewWishlist():
def createBookListing():

def setBookID(): # set bookID
def setBookPublisher(): # set publisher for the book
def setPrice(): # set base price for book
def getBookID(): # return book id
def getBookPublisher(): # return publisher name
def getPrice(): # return base price for book

def makePurchaseID():

def getCustomerName():
def getUserName():
def getCustomerAddress():
def getCustomerEmail():
def getCustomerPhone():

def addSupportTicket():
def setTicketNumber():
def setTicketDescription():
def removeSupportTicket():
def editSupportTicket():
def setTicketStatus(): # initially was named updateTicketStatus

def displayStaffSupportTicketMenu():
def displayCustomerSupporTicketMenu():

def calculateTax(): # retrive base price for book and calculate tax
def setDiscount():
def editDiscount():
