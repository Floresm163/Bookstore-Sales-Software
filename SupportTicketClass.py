class SupportTicket: # create and edit support tickets
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

class ManageSupportTicket:
  def __init__(self, supportTickets):
    self.Support = supportTickets

  def editSupportTicket(self, ticketNumber): # edit an already existing ticket
    if ticketNumber not in self.Support.tickets: # if ticket not found print error message
      print(f'Ticket #{ticketNumber} not found.')
      return False

    ticket = self.supportTickets[ticketNumber]
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
    
  def removeSupportTicket(self): # delete a ticket
    
  
  
  def updateTicketStatus(self): # update the status of the ticket
  
  
  
    
