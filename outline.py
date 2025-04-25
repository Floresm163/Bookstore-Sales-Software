# adding functions: createWishlist, createBooklisting, viewWishlist, viewBooklistings, displayCustomerSupportTicketMenu, displayStaffSupportTicketMenu, userLogin, createLogin, displayAdminstratorMenu, displayStaffMenu, displayGuestMenu, displayCustomerMenu, getUserName, createUserName - MB
# going to have to add functions to make user profiles for staff, admin, customer, and guest accounts then adjust user display menus to only be accesible to correct profile types (i.e. guests can set wishlists or access user menu...) - MB
# creating two separate display menus for support tickets. - MB
# displayCustomerSupportTicketMenu will allow customers to submit and view their pending/completed tickets without being able to edit or change their status. - MB
# displayStaffSupportTicketMenu will allow employees to create tickets on customers behalf, edit tickets, update ticket status etc - MB
# going to create 2 separate text files. userList.txt will keep track of all usernames with the users designation listed directly under it. profile.txt will be unique to each user account and have their various information listed. - MB
# removed date of birth variable from user accounts - MB

def userLogin():
  while True:
    try:
      userLogin = input("Enter UserName: ")
      userLogin.upper()
      userPassword = input("Enter Password: ")
      with open('userList.txt', 'r') as userList:
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
          designationMenu(designation)
        else:
          print("Username or Password invalid.")
      except:
        print("File not found.")

def createLogin():
  user_name = createUserName()
  password = input("Enter Password: ")
  first_name = input("Enter First Name: ")
  last_name = input("Enter Last Name: ")
  full_name = firstname.upper() + '_' + lastname.upper()
  address = input("Enter Address: ")
  email = input("Enter eMail: ")
  phone = input("Enter Phone Number: ")
  
  print("Account Designations")
  print("Assign Account Designation: Administrators = 1, Staff = 2, Customers = 3, Guests = 4")
  while True:
    try:
      user_designation = int(input("Enter the designation for account: "))
      if 0 <= user_designation <= 4:
        user_designation = str(userDesignation)
        break
      else:
        print("Designation invalid. Please enter a designation between 1-4.")
    except ValueError:
      print("Designation invalid. Please enter a designation between 1-4.")

  with open('userList.txt', 'a') as userList:
    userList.write(f'{user_name}\n')
    userList.write(f'{password}\n')
    userList.write(f'{user_designation}\n')

  filename = (f'{full_name}_{user_name}')
  with open(f'{filename}.txt', 'w') as profile:
    profile.write(f'{user_name}\n')
    profile.write(f'{password}\n')
    profile.write(f'{full_name}\n')
    profile.write(f'{address}\n')
    profile.write(f'{email}\n')
    profile.write(f'{phone}\n') 

def createUserName(): # this function will get the username and make sure a user with that name doesn't already exist
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


def displayAdminMenu():
def displayStaffMenu():

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
  
def displayCustomerMenu():
  print("Main Menu")
  print("1. User Menu")
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
  

def displayWishlist():
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
