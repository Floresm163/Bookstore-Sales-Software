"""--- Inventory Management System ---"""
#     by Milly Flores, Mary Brannon, Elisa Mujica, and Douglas Henriquez

import datetime
from enum import Enum, auto
from typing import Dict, List, Optional, Union

#     This  defines the different types of user roles in the system.
#     Each role corresponds to a specific level of access and functionality:
#
#     - Admin: Full administrative privileges across the system.
#     - Staff: Limited access to manage books, tickets, and pre-orders.
#     - Customer: Access to personal account features like wishlist and orders.
#     - Guest: Temporary or non-registered user with read-only access.
#     Mary Brannon, 4/27/25

class UserType(Enum): 
    Admin = 1      # administrator designation with full system access
    Staff = 2      # staff designation with limited system access
    Customer = 3   # customer designation
    Guest = 4      # guest designation for users without an account

#     Represents a book in the inventory system. This class stores essential
#     data about a book, including its identifier, title, author,
#     genre, and the quantity available in stock. It also records the date the
#     book was added to the system.
#     Elisa Mujica, 4/26/25

class Book: # collect the information for a book
    def __init__(self, book_id: str, title: str, author: str, genre: str, quantity: int = 0): # initialize book class
        self.id = book_id          
        self.title = title         
        self.author = author       
        self.genre = genre         
        self.quantity = quantity   
        self.date_added = datetime.date.today()  
    
    def __str__(self): # retrieve information
        display = (f"\nBook ID: {self.id}\n Title: {self.title}\n Author: {self.author}\n Genre: {self.genre}\n Date Added: {self.date_added}\n Quantity: {self.quantity}")     
        return display

#     Represents a customer support ticket submitted by a user. This class
#     captures the key details of a support request including who submitted it,
#     the issue description, current status, and relevant timestamps.
#     Milly Flores, 4/27/25

class SupportTicket: # create customer support tickets
    def __init__(self, ticket_id: str, username: str, issue: str):
        self.id = ticket_id           
        self.username = username                   # user who created ticket
        self.issue = issue               
        self.status = "Open"                       # current status
        self.created_date = datetime.date.today()  # date created
        self.resolved_date = None                  # date resolved
    
    def __str__(self): # ticket display 
        resolved = f", Resolved: {self.resolved_date}" if self.resolved_date else ""
        display = (f"{self.id}: {self.issue} (Status: {self.status}{resolved})")
        return display
        
#     Represents a user account within the system. This class holds personal
#     information, contact details, and role designation of a user. It supports
#     administrators, staff, and customers through their account data.
#     Used by the account manager and interfaces to manage user access and
#     provide role-based interaction throughout the system.
#     Mary Brannon, 4/28/25

class UserAccount: # represent a users account
    def __init__(self, username: str, name: str, email: str, phone: int, password: str, designation: UserType):
        self.username = username      # unique username
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password      
        self.designation = designation  # user designation with enum value
        self.date_created = datetime.date.today()  
    
    def __str__(self): # account display
        display = (f'\nUsername: {self.username}\n Name: {self.name}\n eMail: {self.email}\n Phone: {self.phone}\n Designation: {self.designation.name}') 
        return display

#     Implements a  class responsible for managing all user accounts in
#     the system. This includes creating new accounts, editing user details,
#     deleting accounts, and handling user input validation. It maintains an
#     internal dictionary of UserAccount objects, keyed by username.
#     Mary Brannon, 4/26/25

class UserAccountManager: # class to manage user accounts
    _instance = None # create a new instance and set it to none by default
    UserAccounts: Dict[str, UserAccount] = {}  # stores all accounts
    
    def __new__(cls): #create new class method
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.testAccounts()
        return cls._instance
    
    @classmethod
    def testAccounts(cls): # create a testAccounts class to populate in test accounts for presentation
        cls.UserAccounts = {"admin": UserAccount("admin", "Admin", "admin@admin.com", "1234567891", "admin123", UserType.Admin),
                            "staff": UserAccount("staff", "Staff", "staff@staff.com", "3457891011", "staff123", UserType.Staff),
                            "customer": UserAccount("customer", "Customer", "customer@customer.com", "1213141516", "customer123", UserType.Customer)}
    
    def createAccount(self) -> bool: # create a new account with validation
        print("\n--------------- Create New Account ---------------")
        print("Type 'QUIT' at any time to cancel account creation\n")
        
        designation = UserType.Customer
        username = self.getUsername()  # use getUsername method to check for avaiable usernames
        if username is None: # if 'quit' is entered during getUsername the method will return none and cancel
            print("Account Creation Cancelled.")
            return False

        email = self.getEmail(username) # email validation loop method
        if email is None: # if 'quit' is entered during getUsername the method will return none and cancel
            print("Account Creation Cancelled.")
            return False
            
        name = input("Enter Name: ").strip() # get the users name
        if name.lower() == 'quit': # if user enters quit cancel creation
            print("Account Creation Cancelled.")
            return False
        if not name:
            print("Name cannot be empty.")
            return False
    
        phone = self.getPhone(username) # phone number validation loop
        if phone is None: # if 'quit' is entered during getUsername the method will return none and cancel
            print("Account Creation Cancelled.")
            return False
            
        password = input("Enter Password: ").strip() # get the password
        if password.lower() == 'quit':
            print("Account Creation Cancelled.")
            return False
            
        self.UserAccounts[username] = UserAccount(username, name, email, phone, password, designation) # create the account
        print("Account Created Successfully.")
        return True

    def getUsername(self): # user name validation. will continue to loop until valid username or 'quit' is entered
        while True:
            username = input("Enter Username: ").strip()
            if username.lower() == 'quit':
                return None
            if not username:
                print("Username cannot be empty.")
                continue
            if username not in self.UserAccounts:
                return username
            else:
                print(f"Username '{username}' is already taken. Please try another.")

    def getEmail(self, username): # email account validation, will continue looping until valid email is entered
        while True:
            email = input("Enter eMail Address: ").strip()
            if email.lower() == 'quit':
                print("Account Creation Cancelled.")
                return False
            if '@' not in email: # basic email validation
                print("Invalid eMail Address.")
            else:
                return email

    def getPhone(self, username): # phone number validation, will continue looping until valid email is entered
        while True:
            try:
                phone = input("Enter Phone Number: ").strip() # get the users phone number
                if phone.lower() == 'quit':
                    print("Account Creation Cancelled.")
                    return False
                if len(phone) != 10 or not phone.isdigit(): # check for valid phone number entry must 10 digits in length
                    print("Phone number must be 10 digits.")
                else:
                    return phone
            except ValueError:
                print("Invalid phone number.")
                return False
        
    def viewAccounts(self) -> None: # display all accounts
        print("\n--- User Accounts ---")
        for account in self.UserAccounts.values():
            print(account)
    
    def deleteAccount(self, username: str) -> bool: # delete user account
        if username in self.UserAccounts:
            del self.UserAccounts[username]
            print(f"Account {username} deleted successfully.")
            return True
        print("Account Not Found.")
        return False
    
    def editAccount(self, username: str) -> bool: # edit existing account
        if username not in self.UserAccounts:
            print("Account Not Found.")
            return False 
            
        print(f"\nEditing Account: {username}")
        print("Press enter to skip field.")
        account = self.UserAccounts[username]
        
        newName = input(f"Enter New Name (current: {account.name}): ").strip()
        if newName:
            account.name = newName

        newPassword = input(f"Enter New Password (current: {account.password}): ").strip()
        if newPassword:
            account.password = newPassword
            
        editDesignation = input("Would you like to change the designation? (Y/N): ").strip().lower()
        if editDesignation == 'y':
            self.editDesignation(username)

        newEmail = self.editEmail(username) # get new email
        account.email = newEmail
        
        newPhone = self.editPhone(username) # get new phone
        account.phone = newPhone

        print("Account Succesfully Updated")

    def editEmail(self, username: str): # create a method to validate updated email information
        account = self.UserAccounts[username]
        while True:
            newEmail = input(f"Enter New eMail Address (current: {account.email}): ").strip()
            if newEmail:
                if '@' not in newEmail: # basic email validation
                    print("Invalid eMail Address.")
                else:
                    return newEmail
            else:
                break

    def editPhone(self, username: str): # create a method to validate updated phone information
        account = self.UserAccounts[username]
        while True:
            try:
                newPhone = input(f"Enter New Phone Number (current: {account.phone}): ").strip() # get the users phone number
                if newPhone:
                    if len(newPhone) != 10 or not newPhone.isdigit(): # check for valid phone number entry must 10 digits in length
                        print("Phone number must be 10 digits.")
                    else:
                        return newPhone
                else:
                    break

            except ValueError:
                print("Invalid phone number.")

    def editDesignation(self, username: str) -> bool: # allow administrators to update account designations
        if username not in self.UserAccounts:
            print("Account Not Found.")
            return False
        try:
            designation_input = input("Enter New Designation (1-Admin, 2-Staff, 3-Customer): ").strip()
            designation = int(designation_input)
            if designation not in {ut.value for ut in UserType if ut != UserType.Guest}:
                raise ValueError
                
            self.UserAccounts[username].designation = UserType(designation)
            print("Designation Updated Successfully.")
            return True
            
        except ValueError:
            print("Invalid Designation. Must be 1, 2, or 3.")
            return False

#     Manages the book collection within the inventory system. This class allows
#     for adding, updating, deleting, and viewing books. It also supports basic
#     search functionality and initializes the inventory with sample books for
#     demonstration purposes.
#     Elisa Mujica, 4/28/25
            
class BookInventory: # manage inventory
    def __init__(self):
        self.books: Dict[str, Book] = {}  # stores books by ID
        self.testBooks()
    
    def testBooks(self): # add sample books for presentation
        sample_books = [Book("B001", "Batman", "Scott Snyder", "Horror", 5),
                        Book("B002", "Superman", "Mark Waid", "Drama", 3),
                        Book("B003", "Wonder Woman", "Kelly Thompson", "Action", 2)]
        
        for book in sample_books:
            self.books[book.id] = book
    
    def addBook(self) -> bool: # adds a new book with validation
        print("\n--- Add New Book ---")
        bookID = input("Enter Book ID: ").strip()
        
        if bookID in self.books: # check if book already exists to prevent duplication 
            print("Book ID already exists.")
            return False
        
        title = input("Enter Title: ").strip()
        author = input("Enter Author: ").strip()
        genre = input("Enter Genre: ").strip()
        
        try:
            quantity = int(input("Enter Quantity: ").strip())
        except ValueError:
            print("Invalid Quantity.")
            return False
        
        # Add new book
        self.books[bookID] = Book(bookID, title, author, genre, quantity)
        print(f"Book '{title}' Added Successfully.")
        return True
    
    def updateBook(self, bookID: str) -> bool: # edit existing book
        if bookID not in self.books:
            print("Book Not Found.")
            return False
        
        book = self.books[bookID]
        
        print(f"\nCurrent Book Details: {book}")
        print("Press enter to skip field.")
        title = input(f"Enter New Title [{book.title}]: ").strip() # Get updated values (empty string means keep current)
        author = input(f"Enter New Author [{book.author}]: ").strip()
        genre = input(f"Enter New Genre [{book.genre}]: ").strip()
        quantity = input(f"Enter New Quantity [{book.quantity}]: ").strip()
        
        if title: book.title = title # Update only changed fields
        if author: book.author = author
        if genre: book.genre = genre
        if quantity: book.quantity = int(quantity)
        
        print("Book Updated Successfully.")
        return True
    
    def deleteBook(self, bookID: str) -> bool: # removes a book from the inventory
        if bookID in self.books:
            del self.books[bookID]
            print("Book Deleted Successfully.")
            return True
        print("Book Not Found.")
        return False
    
    def searchBooks(self, searchTerm: str) -> List[Book]: # searches books by title, author, genre, or id
        results = []
        searchTerm = searchTerm.lower()
        for book in self.books.values():
            if (searchTerm in book.title.lower() or 
                searchTerm in book.author.lower() or
                searchTerm in book.genre.lower() or 
                searchTerm in book.id.lower()):
                results.append(book)
        return results
    
    def viewBooks(self) -> List[Book]: # return books in inventory
        return list(self.books.values())
        
#     Handles the creation, management, and resolution of customer support
#     tickets. This class allows users to report issues and enables staff to
#     track, update, and resolve those tickets. Each ticket is stored and
#     identified by a unique ID.
#     Milly Flores, 4/27/25

class SupportTicketSystem: # manage customer support tickets
    def __init__(self):
        self.tickets: Dict[str, SupportTicket] = {}  # Stores tickets by ID
        self.nextTicketID = 1  # Auto-incrementing ID
    
    def createTicket(self, username: str) -> Optional[SupportTicket]: # create new support ticket
        print("\n--- Create Support Ticket ---")
        issue = input("Issue Description: ").strip()
        if not issue:
            print("Issue Description Cannot Be Empty.")
            return None
        
        ticketID = f"T{self.nextTicketID:04d}" # Generate ticket ID and create ticket
        self.nextTicketID += 1
        ticket = SupportTicket(ticketID, username, issue)
        self.tickets[ticketID] = ticket
        print(f"Ticket {ticketID} created successfully!")
        return ticket
    
    def updateTicketStatus(self, ticketID: str) -> bool: # updates ticket status
        if ticketID not in self.tickets:
            print("Ticket not found!")
            return False
        
        print(f"\nCurrent status: {self.tickets[ticketID].status}")
        newStatus = input("Enter New Status: ").strip()
        if not newStatus:
            print("Status Cannot Be Empty")
            return False
        
        self.tickets[ticketID].status = newStatus # ppdate status and resolution date
        if newStatus.lower() == "resolved":
            self.tickets[ticketID].resolved_date = datetime.date.today()
        print("Ticket Status Updated.")
        return True
    
    def viewTickets(self, username: Optional[str] = None, current_user: Optional[UserAccount] = None) -> List[SupportTicket]:
        if current_user and current_user.designation in [UserType.Admin, UserType.Staff]: # Staff and admins can see all tickets
            return list(self.tickets.values())
        elif username:
            return [t for t in self.tickets.values() if t.username == username] # Customers can only see their own tickets
        return []
    
    def delete_ticket(self, ticketID: str) -> bool:
        if ticketID in self.tickets:
            del self.tickets[ticketID]
            print("Ticket Deleted Successfully.")
            return True
        print("Ticket Not Found.")
        return False

#     Manages customer wishlists within the system. Each user can maintain a
#     personal list of books they are interested in. The class provides methods
#     for adding, removing, and viewing wishlist items, and relies on the main
#     BookInventory to validate book existence.
#     Elisa Mujica, 4/27/25

class WishlistManager:
    def __init__(self):
        self.wishlists: Dict[str, List[Book]] = {}  # {username: [book1, book2]}
        self.bookInventory = BookInventory() 
    
    def addWishlist(self, username: str, bookID: str) -> bool: # adds book to wishlist
        if username not in self.wishlists:
            self.wishlists[username] = []
        
        book = self.bookInventory.books.get(bookID) # get book from the book inventory
        if not book:
            print("Book not found in inventory.")
            return False
            
        if book in self.wishlists[username]:  # check if already in wishlist
            print("Book Already in Wishlist.")
            return False
        
        self.wishlists[username].append(book)
        print(f"Added '{book.title}' to Wishlist.")
        return True
    
    def removeWishlist(self, username: str, bookID: str) -> bool: #removes a book from users wishlist
        if username not in self.wishlists:
            print("No Wishlist Found.")
            return False
      
        for book in self.wishlists[username]: # find and remove book
            if book.id == bookID:
                self.wishlists[username].remove(book)
                print("Book Removed.")
                return True
        
        print("Book Not Found.")
        return False
    
    def viewWishlist(self, username: str) -> List[Book]: # returns wishlist
        return self.wishlists.get(username, [])

#     Manages book preorders placed by customers. Allows users to reserve books
#     in advance, track the status of their orders, and cancel them if needed.
#     Orders are stored per user and contain key details like the book, order
#     date, and current status.
#     Milly Flores, 4/27/25

class PreorderSystem: # manages preorders
    def __init__(self):
        self.Preorders: Dict[str, List[Dict]] = {}  # {username: [order1, order2]}
    
    def createPreorder(self, username: str, book: Book) -> bool: # creates a new preorder
        if username not in self.Preorders:
            self.Preorders[username] = []
        order = { # create dictionary for orders
            'Book': book,
            'Date': datetime.date.today(),
            'Status': 'Pending'}

        self.Preorders[username].append(order)
        print(f"Pre-order created for '{book.title}'!")
        return True
    
    def cancelPreorder(self, username: str, order_index: int) -> bool: # cancel preorder
        if username not in self.Preorders or not self.Preorders[username]:
            print("No Pre-order Found.")
            return False
        
        try:  # remove order by index
            order = self.Preorders[username].pop(order_index - 1)
            print(f"Cancelled Pre-order for '{order['Book'].title}'.")
            return True
        except IndexError:
            print("Invalid Order Index.")
            return False
    
    def updateOrderStatus(self, username: str, order_index: int) -> bool: # updates an orders status
        if username not in self.Preorders or not self.Preorders[username]:
            print("No Pre-orders Found.")
            return False
        
        try:
            order = self.Preorders[username][order_index - 1]
            print(f"\nCurrent status: {order['Status']}")
            new_status = input("Enter new status: ").strip()
            if not new_status:
                print("Status Cannot be empty.")
                return False
            self.Preorders[username][order_index - 1]['Status'] = new_status
            print("Order Status Updated.")
            return True
        except IndexError:
            print("Invalid Order Index.")
            return False
    
    def viewOrders(self, username: Optional[str] = None, current_user: Optional[UserAccount] = None) -> List[Dict]:
        if current_user and current_user.designation in [UserType.Admin, UserType.Staff]: # Return all orders with username information
            all_orders = []
            for user, orders in self.Preorders.items():
                for order in orders:
                    order_with_user = order.copy()
                    order_with_user['Username'] = user
                    all_orders.append(order_with_user)
            return all_orders
        elif username:
            return self.Preorders.get(username, []) # Return only the specified user's orders
        return []

#     Serves as the foundational user interface class from which all role-specific
#     interfaces (Administrator, Staff, Customer, Guest) inherit. It provides shared
#     utility methods for displaying menus and printing lists of items.
#     Mary Brannon, 4/26/25
        
class BaseInterface: # base interface to prevent 
    def __init__(self):
        self.running = True  # Controls interface loop
    
    def displayMenu(self, title: str, options: List[str]) -> int: # displays a menu and returns the users choice
        print(f"\n----- {title} -----")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print(f"{len(options)+1}. Back\n")
        if title == "Main Menu":
            print(f"{len(options)+2}. Exit\n")
        
        while True: # get and validate user input
            try:
                choice = input("Enter your choice: ").strip()
                if not choice:
                    raise ValueError
                choice = int(choice)
                max_option = len(options)+2 if title == "Main Menu" else len(options)+1
                if 1 <= choice <= max_option:
                    return choice
                print(f"Please enter a number between 1-{max_option}")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def printList(self, items: List[Union[Book, SupportTicket, UserAccount]], title: str) -> None:
        print(f"\n--- {title} ---")
        if not items:
            print("No Items Found.")
            return
        
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")

#     Provides a full-featured interface for administrators to manage the system.
#     Admins have access to user account management, book inventory, support tickets,
#     and preorder workflows. Inherits shared methods from BaseInterface for
#     menu display and list formatting.
#     Mary Brannon, 4/26/25

class AdministratorInterface(BaseInterface):
    def __init__(self, accountManager, bookInventory, ticketSystem, preorderSystem):
        super().__init__()
        self.accountManager = accountManager
        self.bookInventory = bookInventory
        self.ticketSystem = ticketSystem
        self.preorderSystem = preorderSystem
    
    def run(self, username: str) -> None:
        self.currentUser = username
        while self.running:
            choice = self.displayMenu(
                "Administrator Menu",
                    ["Manage User Accounts",
                    "Manage Book Inventory",
                    "Manage Support Tickets",
                    "Manage Pre-orders",
                    "Logout"])

            if choice == 1:
                self.manageAccounts()
            elif choice == 2:
                self.manageBooks()
            elif choice == 3:
                self.manageTickets()
            elif choice == 4:
                self.managePreorders()
            elif choice == 5:
                print("Logging out...")
                self.running = False

    def manageAccounts(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "User Account Management",
                    ["View All Accounts",
                    "Create New Account",
                    "Delete Account",
                    "Edit Account",
                    "Search Accounts"])
            
            if choice == 1:
                self.accountManager.viewAccounts()
            elif choice == 2:
                self.accountManager.createAccount()
            elif choice == 3:
                username = input("Enter Username to Delete: ").strip()
                self.accountManager.deleteAccount(username)
            elif choice == 4:
                username = input("Enter Username to Edit: ").strip()
                self.accountManager.editAccount(username)
            elif choice == 5:
                term = input("Enter Search Term: ").strip()
                results = [acc for acc in self.accountManager.UserAccounts.values() 
                          if term.lower() in acc.username.lower()]
                self.printList(results, "Search Results")
            elif choice == 6:
                break

    def manageTickets(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "Support Ticket Management",
                ["View All Tickets",
                 "Update Ticket Status",
                 "Delete Ticket"])
    
            if choice == 1:
                current_user = self.accountManager.UserAccounts.get(self.currentUser)
                tickets = self.ticketSystem.viewTickets(current_user=current_user)
                self.printList(tickets, "All Tickets")
            elif choice == 2:
                ticket_id = input("Enter Ticket ID to Update: ").strip()
                self.ticketSystem.updateTicketStatus(ticket_id)
            elif choice == 3:
                ticket_id = input("Enter Ticket ID to Delete: ").strip()
                self.ticketSystem.delete_ticket(ticket_id)
            elif choice == 4:
                break

    def managePreorders(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "Pre-order Management",
                ["View All Pre-orders",
                 "Update Pre-order Status",
                 "Cancel Pre-order"])
    
            if choice == 1:
                current_user = self.accountManager.UserAccounts.get(self.currentUser)
                orders = self.preorderSystem.viewOrders(current_user=current_user)
                if not orders:
                    self.printList(orders, "All Pre-orders")
                else:
                    for i, order in enumerate(orders, 1):
                        print(f"{i}. {order['Book'].title} - {order['Status']} (Date: {order['Date']}, User: {order['Username']})")
            elif choice == 2:
                username = input("Enter Username: ").strip()
                orders = self.preorderSystem.viewOrders(username=username)
                if not orders:
                    print(f"No pre-orders found for user {username}.")
                else:
                    for i, order in enumerate(orders, 1):
                        print(f"{i}. {order['Book'].title} - {order['Status']}")
                    try:
                        order_index = int(input("Enter Order Number to Update: "))
                        self.preorderSystem.updateOrderStatus(username, order_index)
                    except ValueError:
                        print("Invalid Order Number.")
            elif choice == 3:
                username = input("Enter Username: ").strip()
                orders = self.preorderSystem.viewOrders(username=username)
                if not orders:
                    print(f"No pre-orders found for user {username}.")
                else:
                    for i, order in enumerate(orders, 1):
                        print(f"{i}. {order['Book'].title} - {order['Status']}")
                    try:
                        order_index = int(input("Enter Order Number to Cancel: "))
                        self.preorderSystem.cancelPreorder(username, order_index)
                    except ValueError:
                        print("Invalid Order Number.")
            elif choice == 4:
                break

    def manageBooks(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "Book Inventory Management",
                ["View All Books",
                 "Add Book",
                 "Update Book",
                 "Delete Book",
                 "Search Book"])

            if choice == 1:
                books = self.bookInventory.viewBooks()
                self.printList(books, "Available Books")
            elif choice == 2:
                self.bookInventory.addBook()
            elif choice == 3:
                book_id = input("Enter Book ID to Update: ").strip()
                self.bookInventory.updateBook(book_id)
            elif choice == 4:
                book_id = input("Enter Book ID to Delete: ").strip()
                self.bookInventory.deleteBook(book_id)
            elif choice == 5:
                term = input("Enter Search Term: ").strip()
                results = self.bookInventory.searchBooks(term)
                self.printList(results, "Search Results")
            elif choice == 6:
                break
                
#     Provides the interface for staff users who assist with book management,
#     support ticket handling, and preorder processing. Inherits from BaseInterface
#     to maintain consistent menu and display behavior.
#     Mary Brannon, 4/26/25

class StaffInterface(BaseInterface):
    def __init__(self, accountManager, bookInventory, ticketSystem, preorderSystem):
        super().__init__()
        self.accountManager = accountManager
        self.bookInventory = bookInventory
        self.ticketSystem = ticketSystem
        self.preorderSystem = preorderSystem
    
    def run(self, username: str) -> None: # main staff interface
        self.currentUser = username
        while self.running:
            choice = self.displayMenu(
                "Staff Menu",
                    ["Manage Book Inventory",
                    "Manage Pre-Orders",
                    "Manage Support Tickets",
                    "Logout"])
            
            if choice == 1:
                self.manageBooks()
            elif choice == 2:
                self.managePreorders()
            elif choice == 3:
                self.manageTickets()
            elif choice == 4:
                print("Logging out...")
                self.running = False

    def manageBooks(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "Book Inventory Management",
                ["View All Books",
                 "Update Book",
                 "Search Book"])

            if choice == 1:
                books = self.bookInventory.viewBooks()
                self.printList(books, "Available Books")
            elif choice == 2:
                book_id = input("Enter Book ID to Update: ").strip()
                self.bookInventory.updateBook(book_id)
            elif choice == 3:
                term = input("Enter Search Term: ").strip()
                results = self.bookInventory.searchBooks(term)
                self.printList(results, "Search Results")
            elif choice == 4:
                break
    
    def managePreorders(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "Pre-order Management",
                ["View All Pre-orders",
                 "Update Pre-order Status"])
    
            if choice == 1:
                current_user = self.accountManager.UserAccounts.get(self.currentUser)
                orders = self.preorderSystem.viewOrders(current_user=current_user)
                if not orders:
                    self.printList(orders, "All Pre-orders")
                else:
                    for i, order in enumerate(orders, 1):
                        print(f"{i}. {order['Book'].title} - {order['Status']} (Date: {order['Date']}, User: {order['Username']})")
            elif choice == 2:
                username = input("Enter Username: ").strip()
                orders = self.preorderSystem.viewOrders(username=username)
                if not orders:
                    print(f"No pre-orders found for user {username}.")
                else:
                    for i, order in enumerate(orders, 1):
                        print(f"{i}. {order['Book'].title} - {order['Status']}")
                    try:
                        order_index = int(input("Enter Order Number to Update: "))
                        self.preorderSystem.updateOrderStatus(username, order_index)
                    except ValueError:
                        print("Invalid Order Number.")
            elif choice == 3:
                break

    def manageTickets(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "Support Ticket Management",
                ["View All Tickets",
                 "Update Ticket Status"])
    
            if choice == 1:
                current_user = self.accountManager.UserAccounts.get(self.currentUser)
                tickets = self.ticketSystem.viewTickets(current_user=current_user)
                self.printList(tickets, "All Tickets")
            elif choice == 2:
                ticket_id = input("Enter Ticket ID to Update: ").strip()
                self.ticketSystem.updateTicketStatus(ticket_id)
            elif choice == 3:
                break
                
#     Provides a user-friendly interface for customers to interact with the system.
#     Customers can browse and search for books, manage their wishlist, place and
#     cancel preorders, and submit or review support tickets. 
#     Elisa Mujica, 4/27/25

class CustomerInterface(BaseInterface):
    def __init__(self, accountManager, bookInventory, ticketSystem, preorderSystem):
        super().__init__()
        self.accountManager = accountManager
        self.bookInventory = bookInventory
        self.ticketSystem = ticketSystem
        self.preorderSystem = preorderSystem
        self.wishlistManager = WishlistManager() 
    
    def run(self, username: str) -> None:
        self.currentUser = username
        while self.running:
            choice = self.displayMenu(
                "User Menu",
                    ["Browse Books",
                    "My Wishlist",
                    "My Pre-orders",
                    "Support Tickets",
                    "Logout"])
            if choice == 1:
                self.manageBooks()
            elif choice == 2:
                self.manageWishlist()
            elif choice == 3:
                self.managePreorders()
            elif choice == 4:
                self.manageTickets()
            elif choice == 5:
                print("Logging out...")
                self.running = False

    def manageBooks(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "Browse Book Inventory",
                ["View All Books",
                 "Search Book"])
            if choice == 1:
                books = self.bookInventory.viewBooks()
                self.printList(books, "Available Books")
            elif choice == 2:
                term = input("Enter Search Term: ").strip()
                results = self.bookInventory.searchBooks(term)
                self.printList(results, "Search Results")
            elif choice == 3:
                break

    def manageWishlist(self) -> None:  
        while self.running:
            choice = self.displayMenu(
                "Wish List Management",
                ["View My Wish list",
                 "Add to Wish list",
                 "Remove from Wish list"])
            
            if choice == 1:
                wishlist = self.wishlistManager.viewWishlist(self.currentUser) 
                self.printList(wishlist, "My Wish List")
            elif choice == 2:
                bookID = input("Enter Book ID to Add: ").strip()
                self.wishlistManager.addWishlist(self.currentUser, bookID) 
            elif choice == 3:
                bookID = input("Enter Book ID to Remove: ").strip()
                self.wishlistManager.removeWishlist(self.currentUser, bookID)  
            elif choice == 4:
                break

    def managePreorders(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "My Pre-orders",
                ["View My Pre-orders",
                 "Place New Pre-order",
                 "Cancel Pre-order"])

            if choice == 1:  # Only show pre-orders for the current customer
                orders = self.preorderSystem.viewOrders(username=self.currentUser)
                if not orders:
                    print("You have no pre-orders.")
                else:
                    for i, order in enumerate(orders, 1):
                        print(f"{i}. {order['Book'].title} - Status: {order['Status']} (Date: {order['Date']})")
            elif choice == 2:
                books = self.bookInventory.viewBooks()
                self.printList(books, "Available Books")
                bookID = input("Enter Book ID to Pre-order: ").strip()
                book = self.bookInventory.books.get(bookID)
                if book:
                    self.preorderSystem.createPreorder(self.currentUser, book)
                else:
                    print("Book not found.")
            elif choice == 3:
                orders = self.preorderSystem.viewOrders(username=self.currentUser) # Only allow canceling own pre-orders
                if not orders:
                    print("You have no pre-orders to cancel.")
                else:
                    for i, order in enumerate(orders, 1):
                        print(f"{i}. {order['Book'].title} - Status: {order['Status']}")
                    try:
                        order_num = int(input("Enter pre-order number to cancel: "))
                        if 1 <= order_num <= len(orders):
                            self.preorderSystem.cancelPreorder(self.currentUser, order_num)
                        else:
                            print("Invalid order number.")
                    except ValueError:
                        print("Please enter a valid number.")
            elif choice == 4:
                break

    def manageTickets(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "My Support Tickets",
                ["View My Tickets",
                 "Create New Ticket",
                 "Delete My Ticket"])
    
            if choice == 1:
                tickets = self.ticketSystem.viewTickets(username=self.currentUser)
                self.printList(tickets, "My Tickets")
            elif choice == 2:
                self.ticketSystem.createTicket(self.currentUser)
            elif choice == 3:
                ticket_id = input("Enter Ticket ID to Delete: ").strip() # Verify ticket belongs to current user before deletion
                ticket = self.ticketSystem.tickets.get(ticket_id)
                if ticket and ticket.username == self.currentUser:
                    self.ticketSystem.delete_ticket(ticket_id)
                else:
                    print("Ticket not found or you don't have permission to delete it.")
            elif choice == 4:
                break

#     Provides limited, read-only access for unregistered or unauthenticated users.
#     Guests can browse and search the book inventory, log in to an existing account,
#     or create a new one. Inherits basic menu and display utilities from BaseInterface.
#     Milly Flores, 4/28/25

class GuestInterface(BaseInterface):
    def __init__(self, accountManager, bookInventory):
        super().__init__()
        self.accountManager = accountManager
        self.bookInventory = bookInventory
    
    def run(self) -> None: # main guest interface
        while self.running:
            choice = self.displayMenu(
                "Guest Menu",
                    ["View Books",
                    "Search Books",
                    "Login",
                    "Create Account"])
            
            if choice == 1:
                books = self.bookInventory.viewBooks()
                self.printList(books, "Available Books")
            elif choice == 2:
                term = input("Enter search term: ").strip()
                results = self.bookInventory.searchBooks(term)
                self.printList(results, "Search Results")
            elif choice == 3:
                return "login" # Signal to go back to login
            elif choice == 4:
                self.accountManager.createAccount()
            elif choice == 5:
                break

#     Acts as the main entry point and controller for the entire application.
#     Handles system startup, user authentication, interface routing based on
#     user role, and manages components such as account management and
#     user interfaces (Admin, Staff, Customer, Guest).
#     Mary Brannon, 4/26/25

class InventoryManagementSystem:
    def __init__(self):
        self.accountManager = UserAccountManager()
        self.ticketSystem = SupportTicketSystem()
        self.preorderSystem = PreorderSystem()
        self.bookInventory = BookInventory()
        
        self.administratorInterface = AdministratorInterface(
            self.accountManager, 
            self.bookInventory,
            self.ticketSystem,
            self.preorderSystem)
        
        self.staffInterface = StaffInterface(
            self.accountManager,
            self.bookInventory,
            self.ticketSystem,
            self.preorderSystem)
        
        self.customerInterface = CustomerInterface(
            self.accountManager,
            self.bookInventory,
            self.ticketSystem,
            self.preorderSystem)
        
        self.guestInterface = GuestInterface(
            self.accountManager,
            self.bookInventory)
    
    def run(self) -> None:
        while True:
            choice = self.displayMainMenu()
            if choice == 1:
                self.handleLogin()
            elif choice == 2:
                result = self.guestInterface.run()
                if result == "login":
                    self.handleLogin()
            elif choice == 3:
                self.accountManager.createAccount()
            elif choice == 4:
                print("Thank you for using our system. Goodbye!")
                exit()

    def displayMainMenu(self) -> int:
        print("\n--- Inventory Management System ---")
        print("1. Log In")
        print("2. Continue as Guest")
        print("3. Create Account")
        print("4. EXIT")
        
        while True:
            try:
                choice = input("Enter Your Choice: ").strip()
                if not choice:
                    raise ValueError
                choice = int(choice)
                if 1 <= choice <= 4:
                    return choice
                print("Please enter a number between 1-4")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def handleLogin(self) -> None:
        while True:
            username = input("Enter Username: ").strip()
            if username not in self.accountManager.UserAccounts: # check for existing account
                print("Username not found. Please try again.")
                continue  # continue on to password prompt if user is found
                
            password = input("Enter Password: ").strip()
            user = self.authenticate(username, password)
            if user:
                self.redirectDesignation(username)
                return
            else:
                print("Invalid password. Please try again.")

    def authenticate(self, username: str, password: str) -> Optional[UserAccount]: # check whether the user exists and if the password matches the name
        userData = self.accountManager.UserAccounts.get(username)
        if userData and userData.password == password:
            return userData
        return None
    
    def redirectDesignation(self, username: str) -> None:
        user = self.accountManager.UserAccounts.get(username)
        if not user:
            print("User Not Found.")
            return
        try:
            if user.designation == UserType.Admin:
                self.administratorInterface.run(username)
            elif user.designation == UserType.Staff:
                self.staffInterface.run(username)
            elif user.designation == UserType.Customer:
                self.customerInterface.run(username)
            else:
                print("Invalid User Type. Please Contact Support.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    system = InventoryManagementSystem()
    system.run()
