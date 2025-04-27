class UserInterface:

    # Sample book list (drop when database is made)
    books = [
        BookListing(101, "Penguin Random House", "2020-09-01", 24.99),
        BookListing(102, "HarperCollins", "2019-03-15", 18.50),
        BookListing(103, "Simon & Schuster", "2021-07-22", 29.95)
    ]

    def __init__(self):
        self.wishlist = Wishlist()  # Initialize the wishlist for the user

    @staticmethod
    def pressEnter():
        input("\nPress Enter to continue...")

    @staticmethod
    def clearScreen():
        input("\nPress Enter to clear the screen...")
        print("\n" * 50)
        print("Screen Cleared")

    @staticmethod
    def displayMainMenu():
        print("\n--- Main Menu ---")
        print("A. User Menu")
        print("B. Book Catalog")
        print("C. Wishlist")
        print("D. EXIT")

        choice = input("Select the letter of your choice: ").strip().upper()

        if choice == "A":
            UserInterface.displayUserMenu()
        elif choice == "B":
            UserInterface.displayBookCatalog()
        elif choice == "C":
            UserInterface.displayWishlist()
        elif choice == "D":
            print("Thank you for visiting!")
        else:
            print("You inputted an invalid choice")
            UserInterface.pressEnter()
            UserInterface.displayMainMenu()

    @staticmethod
    def displayUserMenu():
        print("\n--- User Menu ---")
        print("1. View Your Profile")
        print("2. Edit Your Profile")
        print("3. Go Back to Main Menu")

        decision = input("Select the number of your choice: ").strip()

        if decision == "1":
            UserInterface.displayProfile()
        elif decision == "2":
            UserInterface.editProfile()
        elif decision == "3":
            UserInterface.displayMainMenu()
        else:
            print("You inputted an invalid choice")
            UserInterface.pressEnter()
            UserInterface.displayUserMenu()

    @staticmethod
    def displayBookCatalog():
        print("\n--- Book Catalog ---")
        # Loop through the sample books and display each one
        for book in UserInterface.books:
            UserInterface.displayBookListing(book)
            print("-" * 30)  # Divider between books

        choice = input("\nEnter the book ID to add to your wishlist or press Enter to go back: ").strip()
        if choice:
            try:
                bookID = int(choice)
                book = next((b for b in UserInterface.books if b.getBookID() == bookID), None)
                if book:
                    UserInterface.addToWishlist(book)
                else:
                    print("Invalid book ID. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid book ID.")
        else:
            UserInterface.displayMainMenu()

    @staticmethod
    def displayWishlist():
        print("\n--- Wishlist ---")
        UserInterface.wishlist.displayWishList()

        choice = input("\n1. Add Book to Wishlist\n2. Remove Book from Wishlist\n3. Go Back to Main Menu\nChoice: ").strip()

        if choice == "1":
            UserInterface.displayBookCatalog()  # Re-display catalog to choose a book to add
        elif choice == "2":
            bookID = input("Enter the book ID to remove from your wishlist: ").strip()
            try:
                bookID = int(bookID)
                UserInterface.removeFromWishlist(bookID)
            except ValueError:
                print("Invalid input. Please enter a valid book ID.")
        elif choice == "3":
            UserInterface.displayMainMenu()
        else:
            print("Invalid choice. Please try again.")
            UserInterface.displayWishlist()

    @staticmethod
    def displayBookListing(book: BookListing):
        """Displays details of a single book."""
        print(f"Book ID: {book.getBookID()}")
        print(f"Publisher: {book.getBookPublishing()}")
        print(f"Published Date: {book.getBookPublishedDate()}")
        print(f"Price: ${book.getPrice()}")

    @staticmethod
    def addToWishlist(book: BookListing):
        """Adds a book to the wishlist."""
        UserInterface.wishlist.addToWishlist(book)
        UserInterface.pressEnter()
        UserInterface.displayMainMenu()

    @staticmethod
    def removeFromWishlist(bookID: int):
        """Removes a book from the wishlist."""
        UserInterface.wishlist.removeBook(bookID)
        UserInterface.pressEnter()
        UserInterface.displayMainMenu()

    # --- Placeholder methods for User Profile and Wishlist ---
    @staticmethod
    def displayProfile():
        print("Displaying user profile...")
        UserInterface.pressEnter()
        UserInterface.displayUserMenu()

    @staticmethod
    def editProfile():
        print("Editing user profile...")
        UserInterface.pressEnter()
        UserInterface.displayUserMenu()


# Entry point 
if __name__ == "__main__":
    ui = UserInterface()
    ui.displayMainMenu()
