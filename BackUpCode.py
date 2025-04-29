"""--- Inventory Management System ---"""

import datetime
from enum import Enum, auto
from typing import Dict, List, Optional, Union

class UserType(Enum): # use the enum module to set the account designations to constants
    Admin = 1      # administrator designation with full system access
    Staff = 2      # staff designation with limited system access
    Customer = 3   # customer designation
    Guest = 4      # guest designation for users without an account

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
        display = (f"{self.id}: {self.issue} (Status: {self.status}{resolved}")
        return display

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

class UserAccountManager: # class to manage user accounts
    _instance = None # create a new instance and set it to none by default
    UserAccounts: Dict[str, UserAccount] = {}  # stores all accounts
    
    def __new__(cls): #create new class method
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.testAccounts()
        return cls._instance
    
    @classmethod
    def testAccounts(cls):
        cls.UserAccounts = {"admin": UserAccount("admin", "Admin", "admin@admin.com", "7778889999", "admin123", UserType.Admin),
                            "staff": UserAccount("staff", "Staff", "admin@admin.com", "7778889999", "staff123", UserType.Staff),
                            "customer": UserAccount("customer", "Customer", "admin@admin.com", "7778889999", "customer123", UserType.Customer)}
    
    def createAccount(self) -> bool: # creates a new account with validation
        print("\n--- Create New Account ---")
        username = input("Enter Username: ").strip()
        if username in self.UserAccounts: # check if username exists
            print("Username already exists.")
            return False

         name = input("Enter Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                return False

        email = input("Enter eMail Address: ")
        if '@' not in email: # basic email validation
            return False
            
        try: # get and validate phone number
            phone = input("Enter Phone Number: ").strip()
            if len(phone) != 10:
                return False
        except ValueError:
            print("Invalid designation. Must be 1, 2, or 3.")
            return False
        
        password = input("Enter Password: ").strip()
        try: # get and validate account designation
            designation = int(input("Enter Designation (1-Admin, 2-Staff, 3-Customer): "))
            if designation not in {ut.value for ut in UserType if ut != UserType.Guest}:
                raise ValueError
            designation = UserType(designation)
        except ValueError:
            print("Invalid designation. Must be 1, 2, or 3.")
            return False
        
        self.UserAccounts[username] = UserAccount(username, name, email, phone, password, designation) # create and store new account
        print("Account Created Successfully.")
        return True
    
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
        if username in self.UserAccounts:
            print(f"\nEditing Account: {username}")
            new_password = input("Enter New Password (press enter to skip): ").strip()
            if new_password:
                self.UserAccounts[username].password = new_password
            print("Account Updated Successfully.")
            return True
        print("Account Not Found.")
        return False

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
            quantity = int(input("Enter quantity: ").strip())
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
        
        # Generate ticket ID and create ticket
        ticketID = f"T{self.nextTicketID:04d}"
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
        
        # Update status and resolution date if applicable
        self.tickets[ticketID].status = newStatus
        if newStatus.lower() == "resolved":
            self.tickets[ticketID].resolved_date = datetime.date.today()
        print("Ticket Status Updated.")
        return True
    
    def viewTickets(self, username: Optional[str] = None) -> List[SupportTicket]:
        if username:
            return [t for t in self.tickets.values() if t.username == username]
        return list(self.tickets.values())
    
    def delete_ticket(self, ticketID: str) -> bool:
        if ticketID in self.tickets:
            del self.tickets[ticketID]
            print("Ticket Deleted Successfully.")
            return True
        print("Ticket Not Found.")
        return False

class WishlistManager:
    def __init__(self):
        self.wishlists: Dict[str, List[Book]] = {}  # {username: [book1, book2]}
    
    def addWishlist(self, username: str, book: Book) -> bool: # adds book to wishlist
        if username not in self.wishlists:
            self.wishlists[username] = []
        
        if book in self.wishlists[username]:  # Check if already in wishlist
            print("Book Already in Wishlist.")
            return False
        
        self.wishlists[username].append(book)
        print(f"Added '{book.title}' to Wishlit.")
        return True
    
    def removeWishlist(self, username: str, book_id: str) -> bool: #removes a book from users wishlist
        if username not in self.wishlists:
            print("No Wishlist Found.")
            return False
      
        for book in self.wishlists[username]: # find and remove book
            if book.id == book_id:
                self.wishlists[username].remove(book)
                print("Book Removed.")
                return True
        
        print("Book Not Found.")
        return False
    
    def viewWishlist(self, username: str) -> List[Book]: # returns wishlist
        return self.wishlists.get(username, [])

class PreorderSystem: # manages preorders
    def __init__(self):
        self.Preorders: Dict[str, List[Dict]] = {}  # {username: [order1, order2]}
    
    def createPreorder(self, username: str, book: Book) -> bool: # creates a new preorder
        if username not in self.Preorders:
            self.Preorders[username] = []
        
        # Create order dictionary
        order = {
            'book': book,
            'date': datetime.date.today(),
            'status': 'Pending'
        }
        self.Preorders[username].append(order)
        print(f"Preorder created for '{book.title}'!")
        return True
    
    def cancelPreorder(self, username: str, order_index: int) -> bool: # cancel preorder
        if username not in self.Preorders:
            print("No Preorder Found.")
            return False
        
        try:  # remove order by index
            order = self.Preorders[username].pop(order_index - 1)
            print(f"Cancelled Preorder for '{order['book'].title}'.")
            return True
        except IndexError:
            print("Invalid Order Index.")
            return False
    
    def updateOrderStatus(self, username: str, order_index: int) -> bool: # updates an orders status
        if username not in self.Preorders:
            print("No Preorders Found.")
            return False
        
        try:
            print(f"\nCurrent status: {self.Preorders[username][order_index - 1]['status']}")
            new_status = input("Enter new status: ").strip()
            if not new_status:
                print("Status Cannot be empty.")
                return False
            self.Preorders[username][order_index - 1]['status'] = new_status
            print("Order Status Updated.")
            return True
        except IndexError:
            print("Invalid Order Index.")
            return False
    
    def viewOrders(self, username: Optional[str] = None) -> List[Dict]:
        if username:
            return self.Preorders.get(username, [])
        else:
            print("No Preorders Available.")
        return [order for user_orders in self.Preorders.values() for order in user_orders]
      

class BaseInterface: # base interface to prevent 
    def __init__(self):
        self.running = True  # Controls interface loop
    
    def displayMenu(self, title: str, options: List[str]) -> int: # displays a menu and returns the users choice
        print(f"\n--- {title} ---")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print(f"{len(options)+1}. Back")
        if title == "Main Menu":
            print(f"{len(options)+2}. Exit")
        
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

class AdministratorInterface(BaseInterface):
    def __init__(self):
        super().__init__()
        self.accountManager = UserAccountManager()
        self.bookInventory = BookInventory()
        self.ticketSystem = SupportTicketSystem()
        self.preorderSystem = PreorderSystem()
    
    def run(self, username: str) -> None: # main administrative interface
        self.currentUser = username
        while self.running:
            choice = self.displayMenu(
                "Administrator Menu",
                    ["Manage User Accounts",
                    "Manage Book Inventory",
                    "Manage Support Tickets",
                    "Manage Preorders",
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
                "Manage Support Tickets",
                ["View All Tickets",
                 "Update Ticket Status",
                 "Delete Ticket"])
            if choice == 1:
                tickets = self.ticketSystem.viewTickets()
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
                "Manage Preorders",
                ["View All Preorders",
                 "Update Preorder Status"])

            if choice == 1:
                orders = self.preorderSystem.viewOrders()
                for i, order in enumerate(orders, 1):
                    print(f"{i}. {order['book'].title} - {order['status']} (Date: {order['date']})")
            elif choice == 2:
                username = input("Enter Username: ").strip()
                try:
                    order_index = int(input("Enter Order Number to Update: "))
                    self.preorderSystem.updateOrderStatus(username, order_index)
                except ValueError:
                    print("Invalid Order Number.")
            elif choice == 3:
                break

    def manageBooks(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "Manage Books",
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


class StaffInterface(BaseInterface):
    def __init__(self):
        super().__init__()
        self.accountManager = UserAccountManager()
        self.bookInventory = BookInventory()
        self.preorderSystem = PreorderSystem()
        self.ticketSystem = SupportTicketSystem()
    
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
                "Manage Books",
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
                "Manage Preorders",
                ["View All Preorders",
                 "Update Preorder Status"])

            if choice == 1:
                orders = self.preorderSystem.viewOrders()
                for i, order in enumerate(orders, 1):
                    print(f"{i}. {order['book'].title} - {order['status']} (Date: {order['date']})")
            elif choice == 2:
                username = input("Enter Username: ").strip()
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
                "Manage Support Tickets",
                ["View All Tickets",
                 "Update Ticket Status"])
            if choice == 1:
                tickets = self.ticketSystem.viewTickets()
                self.printList(tickets, "All Tickets")
            elif choice == 2:
                ticket_id = input("Enter Ticket ID to Update: ").strip()
                self.ticketSystem.updateTicketStatus(ticket_id)
            elif choice == 3:
                break

class CustomerInterface(BaseInterface):
    def __init__(self):
        super().__init__()
        self.bookInventory = BookInventory()
        self.wishlistManager = WishlistManager()
        self.preorderSystem = PreorderSystem()
        self.ticketSystem = SupportTicketSystem()
    
    def run(self, username: str) -> None: # main customer loop
        self.currentUser = username
        while self.running:
            choice = self.displayMenu(
                "Customer Menu",
                    ["Browse Books",
                    "My Wishlist",
                    "My Preorders",
                    "Support Tickets",
                    "Logout"])

            
            if choice == 1:
                self.browseBooks()
            elif choice == 2:
                self.manageWishlist()
            elif choice == 3:
                self.managePreorders()
            elif choice == 4:
                self.manageTickets()
            elif choice == 5:
                print("Logging out...")
                self.running = False

    def manageTickets(self) -> None:
        while self.running:
            choice = self.displayMenu(
                "Support Ticket Management",
                ["View My Tickets",
                 "Create New Ticket",
                 "Delete My Ticket"])

            if choice == 1:
                tickets = self.ticketSystem.viewTickets(self.currentUser)
                self.printList(tickets, "My Tickets")
            elif choice == 2:
                self.ticketSystem.createTicket(self.currentUser)
            elif choice == 3:
                ticket_id = input("Enter Ticket ID to Delete: ").strip()
                self.ticketSystem.delete_ticket(ticket_id)
            elif choice == 4:
                break

class GuestInterface(BaseInterface):
    def __init__(self):
        super().__init__()
        self.bookInventory = BookInventory()
    
    def run(self) -> None: # main guest interface
        while self.running:
            choice = self.displayMenu(
                "Guest Menu",
                    ["Browse Books",
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
                self.running = False  # Signal to go back to login
            elif choice == 4:
                accountManager = UserAccountManager()
                accountManager.createAccount()
            elif choice == 5:
                break

class InventoryManagementSystem:
    def __init__(self):
        self.accountManager = UserAccountManager()
        self.administratorInterface = AdministratorInterface()
        self.staffInterface = StaffInterface()
        self.customerInterface = CustomerInterface()
        self.guestInterface = GuestInterface()
        self.maxAttempts = 3  # Max login attempts
    
    def run(self) -> None:
        while True:
            choice = self.displayMainMenu()
            if choice == 1:
                self.handleLogin()
            elif choice == 2:
                self.guestInterface.run()
            elif choice == 3:
                self.accountManager.createAccount()
            elif choice == 4:
                print("Thank you for using our system. Goodbye!")
                exit()

    def displayMainMenu(self) -> int:
        print("\n--- Inventory Management System ---")
        print("1. Login")
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
        attempts = 0
        while attempts < self.maxAttempts:
            username = input("Enter Username: ").strip()
            password = input("Enter Password: ").strip()
            user = self.authenticate(username, password)
            if user:
                self.redirectDesignation(username)
                return
            
            attempts += 1
            remaining = self.maxAttempts - attempts
            print(f"Invalid credentials. {remaining} attempts remaining.")
        
        print("Maximum Login Attempts Reached.")

    def authenticate(self, username: str, password: str) -> Optional[UserAccount]:
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
