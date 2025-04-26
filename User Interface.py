
class UserInterface:

    # Sample book list (drop when database is made)
    books = [
        BookListing(101, "Penguin Random House", "2020-09-01", 24.99),
        BookListing(102, "HarperCollins", "2019-03-15", 18.50),
        BookListing(103, "Simon & Schuster", "2021-07-22", 29.95)
    ]

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
            BookListingInterface.displayBookListing(book)
            print("-" * 30)  # Divider between books

        UserInterface.pressEnter()
        UserInterface.displayMainMenu()

    @staticmethod
    def displayWishlist():
        print("\n--- Wishlist ---")
        print("1. View your wishlist")
        print("2. Edit your wishlist")
        print("3. Go back to Main Menu")

        decision = input("Select the number of your choice: ").strip()

        if decision == "1":
            UserInterface.displayWishList()
        elif decision == "2":
            UserInterface.editWishList()
        elif decision == "3":
            UserInterface.displayMainMenu()
        else:
            print("You inputted an invalid choice")
            UserInterface.pressEnter()
            UserInterface.displayWishlist()

    @staticmethod
    def getChar() -> str:
        return input("Enter a character: ").strip()

    @staticmethod
    def getString() -> str:
        return input("Enter a string: ").strip()

    @staticmethod
    def getInt() -> int:
        while True:
            try:
                return int(input("Enter an integer: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")

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

    @staticmethod
    def displayWishList():
        print("Displaying wishlist...")
        UserInterface.pressEnter()
        UserInterface.displayWishlist()

    @staticmethod
    def editWishList():
        print("Editing wishlist...")
        UserInterface.pressEnter()
        UserInterface.displayWishlist()


# Entry point of the program
if __name__ == "__main__":
    UserInterface.displayMainMenu()
