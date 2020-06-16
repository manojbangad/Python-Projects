from CustomerRegistration.Registration import Register
from CustomerTransactions.Deposits import Credit
from CustomerTransactions.Withdrawals import Debit
from DatabaseOperations.Reports import Report
from DatabaseOperations.DeleteCustomerData import DeleteCustomerData
import sqlite3
from sqlite3 import Error
import atexit

class StartApp:

    conn = None
    connection = None

    def __init__(self):
        db_path = "E:\Python Class\Pycharm HandsOn\BankingDemoProject\Data Files\ProjectDB.db"
        try:
            self.conn = sqlite3.connect(db_path)
            self.connection = self.conn.cursor()

            self.reg = Register(self.connection)
            self.cred = Credit(self.connection)
            self.deb = Debit(self.connection)
            self.rep = Report(self.connection)
            self.deleteCust = DeleteCustomerData(self.connection)
        except Error as e:
            print(e)
            print("Error faced in establishing the connection!")

    def menu(self):

        print("\nStarted the banking application\n")

        user_input = ''
        # while(user_input == 'Y' or user_input == 'y'):
        while user_input != 'N' and user_input != 'n':

            print(" MENU : ")
            print(" 1 : Register New Customer")
            print(" 2 : Add Credit Entry")
            print(" 3 : Add Debit Entry")
            print(" 4 : Customer Search")
            print(" 5 : Reports")
            print(" 6 : Delete Customer")

            user_transaction_input = input("Enter transaction number to be performed : ")
            # if int(user_transaction_input) not in range(1, 7):
            #     print("Incorrect input entered.")
            #     continue

            if int(user_transaction_input) == 1:
                acc_id = self.reg.initiateCustomerRegistration()
                self.cred.initiateCustomerBalance(acc_id)

            elif int(user_transaction_input) == 2:
                account_id = input("Enter account number : ")
                if account_id.isdigit():
                    amount = input("Enter amount : ")
                    if amount.isdigit():
                        self.cred.deposit(account_id, amount)
                    else:
                        print("\n Incorrect format for amount !")
                else:
                    print("\n Incorrect account ID entered !")

            elif int(user_transaction_input) == 3:
                account_id = input("Enter account number : ")
                if account_id.isdigit():
                    amount = input("Enter amount : ")
                    if amount.isdigit():
                        self.deb.withdraw(account_id, amount)
                    else:
                        print("\n Incorrect format for amount !")
                else:
                    print("\n Incorrect account ID entered !")

            elif int(user_transaction_input) == 4:
                account_id = input("Enter account number : ")
                if account_id.isdigit():
                    self.rep.getCustomerByAccountID(int(account_id))
                else:
                    print("\n Incorrect account ID entered !")

            elif int(user_transaction_input) == 5:
                self.rep.reportingMenu()

            elif int(user_transaction_input) == 6:
                account_id = input("Enter account number : ")
                if account_id.isdigit():
                    self.deleteCust.deleteCustomerDetails(int(account_id))
                else:
                    print("\n Incorrect account ID entered !")
            else:
                print("Incorrect input entered.")

            self.commitData()
            # user_input = input("\n Do you want to perform any transaction ? (y/n) : ")
            user_input = input("\n Do you want to continue with next transaction ? (y/n) : ")

        atexit.register(self.closeConnection)

    def commitData(self):
        self.conn.commit()

    def closeConnection(self):
        self.commitData()
        self.conn.close()


SA = StartApp()
SA.menu()
