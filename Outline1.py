
class BookListing:
    #Constructor to initialize a book listing (added to created book and set values)
    def __init__(self, bookID: int, bookPublishing: str, bookPublishedDate: str, bookPrice: float):
        self.bookID = bookID
        self.bookPublishing = bookPublishing
        self.bookPublishedDate = bookPublishedDate
        self.bookPrice = bookPrice

    #Getter for bookID
    def getBookID(self) -> int:
        return self.bookID

    #Getter for bookPublishing
    def getBookPublishing(self) -> str:
        return self.bookPublishing

    #Getter for bookPublishedDate
    def getPublishingDate(self) -> str:
        return self.bookPublishedDate

    #Setter for bookPrice
    def setPrice(self, newPrice: float):
        self.bookPrice = newPrice

    #Get current price(added for get price)
    def getPrice(self) -> float:
        return self.bookPrice

class Wishlist:
    # Creating an empty wishlist
    def __init__(self):
        self.books = []

    # Displaying your wishlist if you have a wishlist
    def displayWishlist(self) -> None:
        if not self.books:
            print('Your Wishlist is empty.')
        else:
            print('----Your Wishlist-----')
            for book in self.books:
                print(f'{book.getBookPublishing()} - ${book.getPrice():.2f}')

    # Adding a book from the BookListing to the Wishlist
    def addBook(self, Wishlistbook: 'BookListing') -> str:
        self.books.append(Wishlistbook)
        print(f'Book: {Wishlistbook.getBookID()} added to the wishlist.')

    # Removing a book from the Wishlist if the book is in the wishlist
    def removeBook(self, bookID: int) -> str:
        for book in self.books:
            if book.getBookID() == bookID:
                self.books.remove(book)
                print(f'Book: {bookID} was removed from the wishlist.')
                return
        print(f'Book with ID {bookID} was not found in the wishlist.')


class BookListingInterface:

    @staticmethod
    def displayBookListing(book: 'BookListing'):
        # Display the details of a BookListing object
        print("\n--- Book Listing ---")
        print(f"The book ID: {book.getBookID()}")
        print(f"The book was published by: {book.getBookPublishing()}")
        print(f"The date the book was published: {book.getPublishingDate()}")
        print(f"The price of the book: ${book.getPrice():.2f}")

        
class LoginInterface: # create class to handle user login 
    def __init__(self): # initialize function to call other classes to retreive info
        self.UserAccountManager = UserAccountManager()
        self.AdministratorMenu = AdministratorInterface()
        self.StaffMenu = StaffInterface()
        self.CustomerMenu = CustomerInterface()
        self.GuestMenu = GuestInterface()

    def loginUser(self): # display starting log in menu
        print("\n--- Login ---")
        print("1. Enter username and password")
        print("2. Login as guest")
        print("3. Create new account")
        while True:
            try:
                loginChoice = int(input("Enter your choice: ")) # get input for login option
                if loginChoice == 1:
                    break
                elif loginChoice == 2:
                    self.GuestMenu.displayGuestMenu() # if guest login is selected direct to guestmenu class
                elif loginChoice == 3:
                    self.UserAccountManager.createAccount() # if create account is selected direct to 
                else:
                    print("Invalid entry. Enter a choice between 1-3.")
            except ValueError: # catch non-integer entries
                print("Invalid entry. Enter a choice between 1-3.")
                
        while True:
            user_name = input("Enter user name: ")
            password = input("Enter password: ")
            self.authenticateLogin(user_name, password) # pass username and password to the authenticate function to make sure user is available and add password
            if user_name:
                return user_name
            else:
                print("Invalid username or password. Try again.")

        self.designationInterface(user_name)

    def authenticateLogin(self, user_name, password): # authenticate if the username is in user accounts dictionary
        if user_name in self.UserAccountManager.UserAccounts:
            user = self.UserAccountManager.UserAccounts[user_name]
            if user['Password'] == password:
                return user
        else:
            return None

    def designationInterface(self, user_name): # function to direct users to correct display menu
        user = self.UserAccountManager.UserAccounts.get(user_name)

        if user is None:
            print('User not found.')
            return
        #designation = user.UserAccounts['Designation']
        designation = user['Designation']
        #user_name = user.UserAccounts['Username']
        user_name = user['Username']

        if designation == 1:
            self.AdministratorMenu.displayAdministratorMenu()
        elif designation == 2:
            self.StaffMenu.displayStaffMenu()
        elif designation == 3:
            self.CustomerMenu.displayCustomerMenu()
        else:
            print("Unknown designation level.")
          
class AdministratorInterface:
    def __init__(self):
        self.accountManager = UserAccountManager()
        self.bookList = BookListInterface()
        self.preOrders = PreOrderInterface()
        self.ticketSupport = SupportTicket()
        self.manageTicket = ManageSupportTicket()
        self.designation = UserAccountDesignation()
        self.logout = LoginInterface()
    
    def displayAdministratorMenu(self):
        print("\n--- Administrator Menu ---")
        print("1. Manage User Accounts")
        print("2. Manage Book Catalog")
        print("3. Manage Pre-Orders")
        print("4. Manage Support Tickets")
        print("5. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.adminAccountMenu()
                elif choice == 2:
                    self.adminBookCatalogMenu()
                elif choice == 3:
                    self.adminPreOrderMenu()
                elif choice == 4:
                    self.adminSupportTicketMenu()
                elif choice == 5:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-5.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-5.")

    def adminAccountMenu(self):
        print("\n--- Manage User Accounts ---")
        print("1. View User Accounts")
        print("2. Add New Account")
        print("3. Delete Account")
        print("4. Edit Account")
        print("5. Set Account Designation")
        print("6. Return to Administrator Menu")
        print("7. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.accountManager.viewAccounts()
                elif choice == 2:
                    self.accountManager.createAccount()
                elif choice == 3:
                    self.accountManager.deleteAccount()
                elif choice == 4:
                    self.accountManager.editAccount()
                elif choice == 5:
                    self.designation.setDesignation()
                elif choice == 6:
                    self.displayAdministratorMenu()
                elif choice == 7:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-7.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-7.")

    def adminBookListMenu(self):
        print("\n--- Manage Book List ---")
        print("1. View Book List")
        print("2. Search Book List")
        print("3. Add Entry")
        print("4. Delete Entry")
        print("5. Update Entry")
        print("6. Return to Administrator Menu")
        print("7. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.bookList.viewBookList()
                elif choice == 2:
                    self.bookList.searchBookList()
                elif choice == 3:
                    self.bookList.addEntry()
                elif choice == 4:
                    self.bookList.deleteEntry()
                elif choice == 5:
                    self.bookList.updateEntry()
                elif choice == 6:
                    self.displayAdministratorMenu()
                elif choice == 7:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-7.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-7.")
        
    def adminPreOrderMenu(self):
        print("\n--- Manage Pre-Orders ---")
        print("1. View Open Pre-Orders")
        print("2. Add Pre-Order List")
        print("3. Edit Pre-Order List")
        print("4. Calculate Pre-Order Total")
        print("5. Return to Administrator Menu")
        print("6. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.preOrders.viewPreOrderLists()
                elif choice == 2:
                    self.preOrders.addPreOrderList()
                elif choice == 3:
                    self.preOrders.editPreOrderList()
                elif choice == 4:
                    self.preOrders.calculatePreOrderTotal()
                elif choice == 5:
                    self.displayAdministratorMenu()
                elif choice == 6:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-6.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-6.")
        
    def adminSupportTicketMenu(self):
        print("\n--- Manage Support Tickets ---")
        print("1. View Support Tickets")
        print("2. Add Support Ticket")
        print('3. Update Support Ticket Status')
        print('4. Edit Support Ticket')
        print('5. Delete Support Ticket')
        print("6. Return to Administrator Menu")
        print("7. EXIT")
        while True:
            try:
                menuChoice = int(input("Enter selection from the menu above: "))
                if menuChoice == 1:
                    self.ticketSupport.viewSupportTicket() # view a support ticket
                elif menuChoice == 2:
                    self.ticketSupport.addSupportTicket() # create a support ticket
                elif menuChoice == 3:
                    ticket = self.searchTicket()
                    self.manageTicket.updateTicketStatus(ticket) # update ticket status
                elif menuChoice == 4:
                    ticket = self.searchTicket()
                    self.manageTicket.editSupportTicket(ticket) # edit/update the status of a support ticket
                elif menuChoice == 5:
                    ticket = self.searchTicket()
                    self.manageTicket.removeSupportTicket(ticket) # remove ticket
                elif menuChoice == 6:
                    self.displayAdministratorMenu() # return to menu
                elif menuChoice == 7:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-7.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-7.")


    def searchTicket(self): # select a specific ticket to edit or or delete
        while True:
            try:
                ticket_number = int(input("Enter support ticket number: "))
                if ticket_number in self.ticketSupport.tickets:
                    ticket = self.ticketSupport.tickets[ticket_number]
                    return ticket
                else:
                    print(f'{ticket_number} not found.')
            except ValueError:
                print("Invalid entry. Enter a ticket number.")

class StaffInterface:
    def __init__(self):
        self.accountManager = UserAccountManager()
        self.bookList = BookListInterface()
        self.preOrders = PreOrderInterface()
        self.logout = LoginInterface()
    
    def displayStaffMenu(self):
        print("\n--- Staff Menu ---")
        print("1. Manage User Accounts")
        print("2. Manage Book Catalog")
        print("3. Manage Pre-Orders")
        print("4. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.staffAccountMenu()
                elif choice == 2:
                    self.staffBookListMenu()
                elif choice == 3:
                    self.staffPreOrderMenu()
                elif choice == 4:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-4.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-4.")

    def staffAccountMenu(self):
        print("\n--- Manage User Accounts ---")
        print("1. Add New Account")
        print("2. Edit Account")
        print("3. Return to Staff Menu")
        print("4. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.accountManager.createAccount()
                elif choice == 2:
                    self.accountManager.editAccount()
                elif choice == 3:
                    self.displayStaffMenu()
                elif choice == 4:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-4.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-4.")

    def staffBookListMenu(self):
        print("\n--- Manage Book List ---")
        print("1. View Book List")
        print("1. Search Book List")
        print("2. Update Entry")
        print("3. Return to Administrator Menu")
        print("4. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.bookList.viewBookList()
                elif choice == 2:
                    self.bookList.searchBookList()
                elif choice == 3:
                    self.bookList.updateBookList()
                elif choice == 4:
                    self.displayStaffMenu()
                elif choice == 5:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-5.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-5.")
        
    def staffPreOrderMenu(self):
        print("\n--- Manage Pre-Orders ---")
        print("1. View Open Pre-Orders")
        print("2. Edit Pre-Order List")
        print("3. Return to Staff Menu")
        print("4. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.preOrders.viewPreOrderList()
                elif choice == 2:
                    self.preOrders.addEntryPreOrderList()
                elif choice == 3:
                    self.displayStaffMenu()
                elif choice == 4:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-4.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-4.")

class CustomerInterface:
    def __init__(self):
        self.accountManager = UserAccountManager()
        self.bookList = BookListInterface()
        self.preOrders = PreOrderInterface()
        self.supportTickets = SupportTicketInterface()
        self.wishlistManager = Wishlist()
        self.logout = LoginInterface()
    
    def displayCustomerMenu(self):
        print("\n--- User Menu ---")
        print("1. User Account")
        print("2. Wishlists")
        print("3. Book Catalog")
        print("4. Pre-Orders")
        print("5. Support Tickets")
        print("6. EXIT")

        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.accountManager.displayCustomerAccountMenu()
                elif choice == 2:
                    self.wishlistManager.displayWishlistMenu()
                elif choice == 3:
                    self.bookCatalog.displayCustomerBookListMenu()
                elif choice == 4:
                    self.preOrders.displayCustomerPreorderMenu()
                elif choice == 5:
                    self.supportTickets.displayCustomerSupportTicketMenu()
                elif choice == 6:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-6.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-6.")

    def customerAccountMenu(self):
        print("\n--- User Account ---")
        print("1. View Account")
        print("2. Edit Account")
        print("3. Return to Menu")
        print("4. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.accountManager.viewAccount()
                elif choice == 2:
                    self.accountManager.editAccount()
                elif choice == 3:
                    self.displayCustomerMenu()
                elif choice == 4:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                    return
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-4.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-4.")

    def customerBookListMenu(self):
        print("\n--- Book List ---")
        print("1. View Book List")
        print("2. Search Book List")
        print("3. Return to Menu")
        print("4. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.bookList.viewBookList()
                elif choice == 2:
                    self.bookList.searchBookList()
                elif choice == 3:
                    self.displayCustomerMenu()
                elif choice == 4:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-4.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-4.")
        
    def customerPreOrderMenu(self):
        print("\n--- Pre-Orders ---")
        print("1. View Open Pre-Orders")
        print("2. Add to Pre-Order List")
        print("3. Return to Menu")
        print("4. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.preOrders.viewPreOrderList()
                elif choice == 2:
                    self.preOrders.addEntryPreOrderList()
                elif choice == 3:
                    self.displayCustomerMenu()
                elif choice == 4:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-4.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-4.")

    def customerWishList(self):
        print("\n--- WishLists ---")
        print("1. Display Wishlists")
        print("2. Add to Wishlist")
        print("2. Remove from Wishlist")
        print("3. Return to Menu")
        print("4. EXIT")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.wishlistManager.displayWishlist()
                elif choice == 2:
                    self.wishlistManager.addBook()
                elif choice == 2:
                    self.wishlistManager.removeBook()
                elif choice == 3:
                    self.displayCustomerMenu()
                elif choice == 4:
                    print("Thank you for visiting!")
                    self.logout.loginUser()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-4.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-4.")

class GuestInterface:
    def __init__(self):
        self.bookList = BookListInterface()
        self.logout = LoginInterface()

    def displayGuestMenu(self):
        print("\n--- Guest Menu ---")
        print("1. Book Catalog")
        print("2. EXIT")

        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.bookList.displayBookListMenu()
                elif choice == 2:
                    print("Thank you for visiting!")
                    self.logout = LoginInterface()
                else:
                    print("Invalid Entry. Please enter an integer bewtween 1-2.")
            except ValueError:
                print("Invalid Entry. Please enter an integer bewtween 1-2.")

class UserAccountDesignation:
    def __init__(self):
        self.AccountManagement = UserAccountManager()

    def editDesignation(self, user_name, new_designation):
        while True:
            new_designation = int(input("Enter user accounts new designation: "))
            if new_designation not in {1, 2, 3}:
                print("Invalid entry. New designation must be between 1-3.")

        if user_name in self.AccountManagement.UserAccounts:
            self.AccountManagement.UserAccounts[user_name]['Designation'] = new_designation
            return True
        
        print("Account not found.")
        return False

class UserAccountManager:
    def __init__(self):
        self.UserAccounts = {} # create a dictionary to store the users information
        
    def createAccount(self): # create a new account by retrieving the information and storing it in a the UserAccounts dictionary
        name = self.getName()
        user_name = self.getUsername()
        password = self.getPassword()
        email = self.getEmail()
        phone = self.getPhone()
        designation = 3 # administrator = 1, staff = 2, and customer = 3. Designation is set to 3 by default and can only be changed by an administrator

        self.UserAccounts[user_name] = {'Name': name, 'Username': user_name, 'Password': password, 'eMail': email, 'Phone': phone, 'Designation': designation}
        self.UserAccounts[TestAdmin] = {'Name': 'Admin', 'Username': 'TA', 'Password': 'Testadmin', 'eMail': 'testadmin@yahoo.com', 'Phone': '1111111111'., 'Designation': 1}
        # store values in the dictionary with the users user name as the key
        return user_name 

    def deleteAccount(self, user_name): # delete an already existing account
        if user_name in self.UserAccounts:
            del self.UserAccounts[user_name]
            print(f'{user_name} has been succesfully deleted.')
            return True
        else:
            print(f'{user_name} not found.')
            return False

    def editAccount(self, user_name): # edit an account
        if user_name not in self.UserAccounts: # check if the user name is valid
            print(f'{user_name} not found.')
            return False

        user = self.UserAccounts[user_name]
        self.displayAccountInformation(user_name)

        print('\nWhich field would you like to edit?:') # username acts as the key and cannot be changed
        print('1. Name')
        print('2. Password')
        print('3. eMail')
        print('4. Phone')
        print('5. EXIT')
    
        while True:
          try:
            choice = int(input("Enter a choice between 1-5: "))
            if choice == 1:
              user.getName()
            elif choice == 2:
              user.getPassword()
            elif choice == 3:
              user.getEmail()
            elif choice == 4:
              user.getPhone()
            elif choice == 5:
              print("Edit cancelled.")
              return False
            else:
              print("Invalid entry. Enter a number between 1-5.")
          except ValueError:
            print("Invalid entry. Enter a number between 1-5.")
        
        print("User information succesfully updated.")
        return True

    def viewAccounts(self):
        print("\n--- All User Accounts ---")
        for i, (user_name, account_info) in enumerate(self.UserAccounts.items(), 1):
            print(f"\nAccount #{i}")
            print(f'Username: {username}')
            print(f'Name: {account_info["Name"]}')
            print(f'Password: {account_info["Password"]}')
            print(f'Email: {account_info["eMail"]}')
            print(f'Phone: {account_info["Phone"]}')
            print(f'Designation: {account_info["Designation"]}')
            print("\n--------------------")
        
    def getName(self): # get users name
        while True: # start validation loop to make sure name is not empty
            first_name = input("Enter first name: ").upper()
            last_name = input("Enter last name: ").upper()
            full_name = first_name + last_name
            if full_name: # checks if the name has been entered, if not repeat the loop
                return full_name
            else:
                print("Invalid Entry. Enter a valid name.")

    def getUsername(self): # get users username
        while True: 
            user_name = input("Enter user name: ").strip()
            if user_name: 
                if user_name not in self.UserAccounts: # check to make sure the username is not already in use
                    return user_name
                print('Invalid entry. Username already exists')
            else:
                print("Invalid Entry. Enter a valid username.")

    def getPassword(self): # get users password
        while True: 
            password = input("Enter a password (must be at least 8 characters): ").strip() # enter the password
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
                continue
                
            confirm = input('Confirm your password: ').strip() # make users enter password again to confirm match
            if password == confirm:
                return password
            else:
                print("Invalid entry. Passwords do not match.")

    def getEmail(self): # get users email
        while True: 
            email = input("Enter Email address: ")
            if '@' in email: # basic email validation
                return email
            else:
                print('Invalid entry. Enter a valid email.')
                
    def getPhone(self): # get users phone number
        while True:
            phone = (input("Enter phone number: ")).strip()
            if phone.isdigit() and len(phone) == 10:  # basic validation
                return phone
            else:
                print('Invalid entry. Enter a valid phone number.')

    def displayAccountInformation(self, user_name):
        if user_name in self.UserAccounts:
            user = self.UserAccounts[user_name]
            print("\n--- Current Account Information ---")
            print(f'Username: {user_name}')
            print(f'Name: {user["Name"]}')
            print(f'Password: {user["Password"]}')
            print(f'Email: {user["eMail"]}')
            print(f'Phone: {user["Phone"]}')
            print(f'Designation: {user["Designation"]}')
            return user
        else:
            print(f'{user_name} not found.')
            return None

class SupportTicket:
    def __init__(self):
        self.tickets = {} # store tickets in dictionary with the ticket number as the key
        self.ticketAccumulator = 1 # set an accumulator to act as the ticket id and keep track of tickets

    def getTicketNumber(self): # get the current ticket number and increase the accumulator
        ticketNumber = self.ticketNumber
        self.ticketNumber += 1
        return ticketNumber

    def getTicketDescription(self): # get the description of the ticket
        while True:
            description = input("Enter ticket description: ")
            if description: # if input is not empty then return input
                return description
            else:
                print("Invalid entry. Support ticket must contain description.")

    def getCustomerEmail(self): # get the customers email address
        while True:
            email = input("Enter customer email: ")
            if '@' in email: # if email contains '@' then return email
                return email
            else:
                print("Invalid entry. Support ticket must contain a valid email.")

    def getCustomerName(self): # get the customers name
        while True: 
            first_name = input("Enter customer first name: ")
            last_name = input("Enter customer last name: ")
            name = first_name + last_name
            if name: # if name is not empty return the name
                return name
            else:
                print("Invalid entry. Support ticket must contain a valid name.")
  
    def setTicketStatus(self, status='open'):
        validStatus = ['open', 'closed']
        if status.lower() in validStatus:
            return status.lower()
        return 'open'
  
    def addSupportTicket(self): # retrieve all the values and create the ticket
        ticketNumber = self.getTicketNumber()
        customerName = self.getCustomerName()
        customerEmail = self.getCustomerEmail()
        description = self.getTicketDescription()
        status = self.setTicketStatus()
  
        ticket = {'Ticket Number': ticketNumber, 'Customer Name': customerName, 'Customer Email': customerEmail, 'Description': description, 'Status': status}
        self.tickets[ticketNumber] = ticket
        print(f'\nTicket #:{ticketNumber} created successfully.')
        return ticketNumber

class ManageSupportTicket: # create class to manage support tickets
  def __init__(self, supportTickets):
    self.Support = supportTickets

  def editSupportTicket(self, ticketNumber): # edit an already existing ticket
    if ticketNumber not in self.Support.tickets: # if ticket not found print error message
      print(f'Ticket #{ticketNumber} not found.')
      return False

    ticket = self.Support.tickets[ticketNumber]
    print(f'Editing Ticket #:{ticketNumber}')
    print(f'Enter new value or press enter to skip field.')
  
    new_first = input('Enter new first name: ')
    new_last = input('Enter new last name: ')
    newName = new_first + new_last
    if newName: # if name is empty then the field was skipped an will not update
      ticket['customerName'] = newName

    newEmail = input('Enter new eMail address: ')
    if newEmail:
      ticket['customerEmail'] = newEmail

    newDescription = input('Enter new description: ')
    if newDescription:
      ticket['description'] = newDescription

    while True:
      newStatus = input("Set ticket status to 'open' or 'closed'").lower()
      if newStatus == 'open' or newStatus == 'closed':
        ticket['status'] = newStatus
        break
      else:
        print('Invalid entry. Ticket status must be set to open or closed.')

    print(f'Ticket #{ticketNumber} has been succesfully updated.')
    return True

  def updateTicketStatus(self, ticketNumber): # close an already open ticket
    if ticketNumber in self.Support.tickets:
      self.Support.tickets[ticketNumber]['status'] = 'closed'
      print(f'Ticket #{ticketNumber} has been closed.')
      return True
    else:
      print(f'Ticket #{ticketNumber} not found.')
      return False
  
  def removeSupportTicket(self, ticketNumber): # delete a ticket
    if ticketNumber in self.Support.tickets:
      del self.Support.tickets[ticketNumber]
      print(f'Ticket #{ticketNumber} has been removed.')


if __name__ == "__main__":
    login = LoginInterface()
    login.UserLogin()
