class SupportTicketInterface:
    def __init__(self):
        self.tickets = []

    def displayCustomerSupportTicketMenu(self):
        print("\n--- Customer Support Menu ---")
        print("1. Create a Support Ticket")
        print("2. View Your Tickets")
        print("3. Return to Customer Menu")
        while True:
            try:
                choice = int(input("Select the number of your choice: "))
                if choice == 1:
                    self.addSupportTicket()
                elif choice == 2:
                    self.viewSupportTickets()
                elif choice == 3:
                    break
                else:
                    print("Invalid Entry. Please enter 1-3.")
            except ValueError:
                print("Invalid Entry. Please enter 1-3.")

    def addSupportTicket(self):
        ticket = SupportTicket()
        ticketNumber = ticket.addSupportTicket()
        self.tickets.append(ticketNumber)

    def viewSupportTickets(self):
        if not self.tickets:
            print("No tickets found.")
        else:
            print("\n--- Your Support Tickets ---")
            for ticketNumber in self.tickets:
                print(f"Ticket #{ticketNumber}")