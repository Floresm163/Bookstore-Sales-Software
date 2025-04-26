class SupportTicket: # create and edit support tickets
  def __init__(self):
    self.tickets = {} # store tickets in dictionary with number as the key and the value a combination of the customers name + email + description
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

def addSupportTicket(self): # retrieve all the values and create the ticket
  ticketNumber = self.getTicketNumber()
  customerName = self.getCustomerName()
  customerEmail = self.getCustomerEmail()
  description = self.getTicketDescription()

  ticket = {'Ticket Number': ticketNumber, 'Customer Name': customerName, 'Customer Email': customerEmail, 'Description': description, 'Status': 'Open'}
  self.tickets[ticketNumber] = ticket
  print(f'\nTicket #:{ticketNumber} created successfully.')
  return ticketNumber

def removeSupportTicket(self): # delete a ticket

def editSupportTicket(self): # edit an already existing ticket

def updateTicketStatus(self): # update the status of the ticket
  
  
  
    
