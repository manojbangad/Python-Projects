from datetime import datetime
import sqlite3
from sqlite3 import Error
from CustomerTransactions.Deposits import Credit

class Debit:

    def __init__(self, connection):
        self.connection = connection

    def withdraw(self, account_id, amount):
        try:
            # ifTrue = self.withdrawFromCustomerBalance(account_id, amount)
            #
            # if ifTrue:
            #     conn = sqlite3.connect(self.db_path)
            #     connection = conn.cursor()
            #
            #     currentDT = datetime.now()
            #     connection.execute("Insert into CustomerTransactions Values(?, ?, ?, ?)",(account_id, 'Debit', amount, currentDT.strftime("%Y-%m-%d %H:%M:%S")))
            #     print("Transaction performed : ")
            #     print("Transaction : Debit \t Account : ", account_id, "\tAmount : ", amount, "\tTime : ", currentDT.strftime("%Y-%m-%d %H:%M:%S"))
            #     print("Transaction successful !")
            #     conn.commit()
            #     conn.close()

            #
            ifTrue = self.withdrawFromCustomerBalance(account_id, amount)

            if ifTrue:
                currentDT = datetime.now()
                self.connection.execute("Insert into CustomerTransactions Values(?, ?, ?, ?)",
                                   (account_id, 'Debit', amount, currentDT.strftime("%Y-%m-%d %H:%M:%S")))
                print("Transaction performed : ")
                print("Transaction : Debit \t Account : ", account_id, "\tAmount : ", amount, "\tTime : ",
                      currentDT.strftime("%Y-%m-%d %H:%M:%S"))
                print("Transaction successful !")

        except Error as e:
            print(" Error :: Inside Debit >> withdraw method of credit class..")
            print(e)

    def withdrawFromCustomerBalance(self, account_id, amount):
        try:
            # cred = Credit()
            # current_balance = int(cred.getCustomerBalance(account_id))
            #
            # if int(amount) > current_balance:
            #     print(" Insufficient balance. cannot withdraw more than current balance of " + str(current_balance))
            # else:
            #     new_balance = int(current_balance) - int(amount)
            #
            #     conn = sqlite3.connect(self.db_path)
            #     connection = conn.cursor()
            #     connection.execute("Update CustomerBalance set amount = ? where account_id = ?", (new_balance, account_id))
            #     print("Updated balance in account ", account_id, " is : " + str(new_balance))
            #     conn.commit()
            #     conn.close()
            #     return True
            # return False

        #
            cred = Credit(self.connection)
            current_balance = int(cred.getCustomerBalance(account_id))

            if int(amount) > current_balance:
                print(" Insufficient balance. cannot withdraw more than current balance of " + str(current_balance))
            else:
                new_balance = int(current_balance) - int(amount)

                self.connection.execute("Update CustomerBalance set amount = ? where account_id = ?",
                                   (new_balance, account_id))
                print("Updated balance in account ", account_id, " is : " + str(new_balance))
                return True
            return False

        except Error as e:
            print(" Error :: Inside Credit >> updateBalanceDeposited method of credit class..")
            print(e)
            return False

# ca = Credit()
# ca.initiateCustomerBalance(1006)
# # ca.deleteCustomerBalance(1006)