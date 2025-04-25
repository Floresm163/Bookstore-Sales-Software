class UserInterface:
    #Pause program until Enter is pressed
    @staticmethod
    def pressEnter():
        input("Press Enter to continue...")

    #Clear screen by printing multiple newlines
    @staticmethod
    def clearScreen():
        input("Press Enter to clear the screen...")
        print("\n" * 50)
        print("Screen Cleared")

    #Display main menu with options
    @staticmethod
    def displayMainMenu():
        print("\n--- Main Menu ---")
        print("A. User Menu")
        print("B. Book Catalog")
        print("C. Wishlist")
        print("D. EXIT")

        #Convert to uppercase to handle lowercase input
        choice = input("Select the letter of your choice: ").strip().upper()

        #Navigate to the selected menu
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

    #Display user-related menu
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

    #Method to show book catalog
    @staticmethod
    def displayBookCatalog():
        print("\n--- Book Catalog ---")
        print("[Book list would go here]")
        UserInterface.pressEnter()
        UserInterface.displayMainMenu()

    #Display wishlist menu
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

    #Gets a single character from user
    @staticmethod
    def getChar() -> str:
        return input("Enter a character: ").strip()

    #Gets a full string from user
    @staticmethod
    def getString() -> str:
        return input("Enter a string: ").strip()

    #Safely gets an integer input from user + validation
    @staticmethod
    def getInt() -> int:
        while True:
            try:
                return int(input("Enter an integer: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    #Displays a fake user profile - [laceholder
    @staticmethod
    def displayProfile():
        print("Displaying user profile...")
        UserInterface.pressEnter()
        UserInterface.displayUserMenu()

    #Editing the user's profile - placeholder
    @staticmethod
    def editProfile():
        print("Editing user profile...")
        UserInterface.pressEnter()
        UserInterface.displayUserMenu()

    # Displays a wishlist - placeholder
    @staticmethod
    def displayWishList():
        print("Displaying wishlist...")
        UserInterface.pressEnter()
        UserInterface.displayWishlist()

    #editing the wishlist -placeholder
    @staticmethod
    def editWishList():
        print("Editing wishlist...")
        UserInterface.pressEnter()
        UserInterface.displayWishlist()


# starts the application by showing main menu
if __name__ == "__main__":
    UserInterface.displayMainMenu()