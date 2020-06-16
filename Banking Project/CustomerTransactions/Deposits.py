from datetime import datetime
import sqlite3
from sqlite3 import Error

class Credit:

    def __init__(self, connection):
        self.connection = connection

    def initiateCustomerBalance(self, account_id):
        try:
            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            # connection.execute("Insert into CustomerBalance Values(?, ?)", (account_id, 0))
            # print("Customer Balance Initiated for transactions !")
            # conn.commit()
            # conn.close()

            self.connection.execute("Insert into CustomerBalance Values(?, ?)", (account_id, 0))
            print("Customer Balance Initiated for transactions !")


        except Error as e:
            print(" Error :: Inside Credit >> initiateCustomerBalance method of credit class..")
            print(e)

    def deposit(self, account_id, amount):
        try:
            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            #
            # currentDT = datetime.now()
            # connection.execute("Insert into CustomerTransactions Values(?, ?, ?, ?)",(account_id, 'Credit', amount, currentDT.strftime("%Y-%m-%d %H:%M:%S")))
            # print("Transaction Performed : ")
            # print("Transaction : Credit \t Account : ", account_id, "\tAmount : ", amount, "\tTime : ", currentDT.strftime("%Y-%m-%d %H:%M:%S"))
            # conn.commit()
            # conn.close()
            #
            # self.updateCustomerBalance(account_id, amount)
            # print("Transaction successful !")

            currentDT = datetime.now()
            self.connection.execute("Insert into CustomerTransactions Values(?, ?, ?, ?)",
                               (account_id, 'Credit', amount, currentDT.strftime("%Y-%m-%d %H:%M:%S")))
            print("Transaction Performed : ")
            print("Transaction : Credit \t Account : ", account_id, "\tAmount : ", amount, "\tTime : ",
                  currentDT.strftime("%Y-%m-%d %H:%M:%S"))

            self.updateCustomerBalance(account_id, amount)
            print("Transaction successful !")

        except Error as e:
            print(" Error :: Inside Credit >> deposit method of credit class..")
            print(e)

    def updateCustomerBalance(self, account_id, amount):
        try:
            # new_amount = int(self.getCustomerBalance(account_id)) + int(amount)
            #
            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            # connection.execute("Update CustomerBalance set amount = ? where account_id = ?", (new_amount, account_id))
            # print("Total balance in account ", account_id, " is : " + str(new_amount))
            # conn.commit()
            # conn.close()


#


            new_amount = int(self.getCustomerBalance(account_id)) + int(amount)

            self.connection.execute("Update CustomerBalance set amount = ? where account_id = ?", (new_amount, account_id))
            print("Total balance in account ", account_id, " is : " + str(new_amount))

        except Error as e:
            print(" Error :: Inside Credit >> updateBalanceDeposited method of credit class..")
            print(e)

    def getCustomerBalance(self, account_id):
        try:
            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            # connection.execute("select * from CustomerBalance where account_id = ?", (account_id, ))
            # customer = connection.fetchone()
            # amount = customer[1]
            # conn.commit()
            # conn.close()
            # return amount

            self.connection.execute("select * from CustomerBalance where account_id = ?", (account_id,))
            customer = self.connection.fetchone()
            amount = customer[1]

            return amount

        except Error as e:
            print(" Error :: Inside Credit >> getCustomerBalance method of credit class..")
            print(e)




# ca = Credit()
# ca.initiateCustomerBalance(1003)
# ca.deleteCustomerBalance(1006)
# ca.getCustomerBalance(1003)
# ca.updateCustomerBalance(1006, 4500)