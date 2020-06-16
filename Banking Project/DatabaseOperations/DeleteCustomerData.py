from sqlite3 import Error

class DeleteCustomerData:

    def __init__(self, connection):
        self.connection = connection

    def deleteCustomerDetails(self, account_id):
        try:
            self.deleteCustomerTransactions(account_id)
            self.deleteCustomerBalance(account_id)

            self.connection.execute("Delete from CustomerDetails where account_id = ?", (account_id,))
            print("All customer details deleted for account_id : ", account_id)

        except Error as e:
            print(" Error :: Inside DeleteCustomerData >> deleteCustomerDetails method ..")
            print(e)

    def deleteCustomerBalance(self, account_id):
        try:
            self.connection.execute("Delete from CustomerBalance where account_id = ?", (account_id,))
            print("Customer Balance entries removed from DB!")

        except Error as e:
            print(" Error :: Inside DeleteCustomerData >> deleteCustomerBalance method ..")
            print(e)

    def deleteCustomerTransactions(self, account_id):
        try:
            self.connection.execute("Delete from CustomerTransactions where account_id = ?", (account_id,))
            print("Customer Transaction entries removed from DB!")

        except Error as e:
            print(" Error :: Inside DeleteCustomerData >> deleteCustomerTransactions method ..")
            print(e)
