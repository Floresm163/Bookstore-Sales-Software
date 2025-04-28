class ManageSupportTicket: # create class to manage support tickets
 def __init__(self, supportTickets=None):
        if supportTickets is None:
            self.Support = SupportTicket()
        else:
            self.Support = supportTickets

  def editSupportTicket(self, ticketNumber): # edit an already existing ticket
    if ticketNumber not in self.Support.tickets: # if ticket not found print error message
      print(f'Ticket #{ticketNumber} not found.')
      return False

    ticket = self.Support[ticketNumber]
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
      print(f'Ticket #{ticketnumber} not found.')
      return False
  
  def removeSupportTicket(self, ticketNumber): # delete a ticket
    if ticketNumber in self.Support.tickets:
      del self.Support.tickets[ticketNumber]
      print(f'Ticket #{ticketNumber} has been removed.')
