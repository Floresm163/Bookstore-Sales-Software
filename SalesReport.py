class SalesReport:
# This prints out all of the information from a sale 
  def printReport(self, sale:SalesTax) -> None:
    print(f' Sales Report for Purchase ID: {sale.purchaseID}')
    print(f' Customer: {sale.customerName}')
    print(f' Item Price: ${sale.bookPrice}')
    print(f' Sales Tax: ${sale.calculateTax()')
    print(f'Total Price (inculind tax): ${sale.bookPrice + sale.calculateTax()}')
