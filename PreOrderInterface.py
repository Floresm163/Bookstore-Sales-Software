class PreOrderInterface:
    def __init__(self):
        self.preOrders = []

    def viewPreOrderLists(self):
        if not self.preOrders:
            print("No pre-orders available.")
        else:
            print("\n--- Pre-Orders ---")
            for preorder in self.preOrders:
                print(f"Book ID: {preorder.getBookId()}, Customer: {preorder.getCustomerName()}, Email: {preorder.getCustomerEmail()}")

    def addPreOrderList(self):
        preorder = PreOrder()
        if preorder.addPreorder() == "Pre-Order placed successfully.":
            self.preOrders.append(preorder)
            print("Pre-order successfully added.")

    def editPreOrderList(self):
        print("Feature coming soon: Edit Pre-Order List.")

    def calculatePreOrderTotal(self):
        print("Feature coming soon: Calculate Pre-Order Total.")