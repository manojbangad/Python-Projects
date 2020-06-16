import sqlite3
from sqlite3 import Error

class Report:

    def __init__(self, connection):
        self.connection = connection

    def reportingMenu(self):
        user_input = ''
        # while(user_input == 'Y' or user_input == 'y'):
        while user_input != 'N' and user_input != 'n':

            print("\n\n Reporting MENU : ")
            print(" 1 : All Customer Data")
            print(" 2 : Customer Transaction Details")

            user_transaction_input = input("Enter report ID from above menu : ")
            if int(user_transaction_input) not in range(1, 3):
                print("Incorrect input entered.")
                continue

            if int(user_transaction_input) == 1:
                self.allCustomerDetails()

            elif int(user_transaction_input) == 2:
                account_id = input("Enter account number : ")
                if account_id.isdigit():
                    self.getCustomerTransactions(account_id)
                else:
                    print("\n Incorrect account ID entered !")

            else:
                pass
            user_input = input("\n Do you want to fetch another report ? (y/n) : ")
        print('\n\nRedirecting to Home Menu..')

    def allCustomerDetails(self):
        try:
            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            # connection.execute("select cd.account_id, cd.first_name, cd.last_name, cd.pan_number, cb.amount, cd.age, cd.gender, cd.city from CustomerDetails cd, CustomerBalance cb where cd.account_id = cb.account_id")
            # customer_details = connection.fetchall()
            #
            # print("\nAcc_ID\tPAN_ID\tF_Name\tL_Name\t Balance\tAge\tGender\tCity")
            # for customer in customer_details:
            #     print(f'{customer[0]}\t{customer[1]}\t{customer[2]}\t{customer[3]}\t{customer[4]}\t\t{customer[5]}\t{customer[6]}\t\t{customer[7]}')
            # conn.commit()
            # conn.close()

            self.connection.execute(
                "select cd.account_id, cd.first_name, cd.last_name, cd.pan_number, cb.amount, cd.age, cd.gender, cd.city from CustomerDetails cd, CustomerBalance cb where cd.account_id = cb.account_id")
            customer_details = self.connection.fetchall()

            print("\nAcc_ID\tPAN_ID\tF_Name\tL_Name\t Balance\tAge\tGender\tCity")
            for customer in customer_details:
                print(f'{customer[0]}\t{customer[1]}\t{customer[2]}\t{customer[3]}\t{customer[4]}\t\t{customer[5]}\t{customer[6]}\t\t{customer[7]}')

        except Error as e:
            print(" Error :: Inside Credit >> initiateCustomerBalance method of credit class..")
            print(e)


    def getCustomerTransactions(self, account_id):
        try:
            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            # connection.execute("select * from CustomerTransactions where account_id = ?", (account_id,))
            # transaction_details = connection.fetchall()
            #
            # for transaction in transaction_details:
            #     print(transaction)
            #     # print(f'{customer[0]}\t{customer[1]}\t{customer[2]}\t{customer[3]}\t{customer[4]}\t\t{customer[5]}\t{customer[6]}\t\t{customer[7]}')
            # conn.commit()
            # conn.close()

            #
            self.connection.execute("select * from CustomerTransactions where account_id = ?", (account_id,))
            transaction_details = self.connection.fetchall()

            for transaction in transaction_details:
                print(transaction)
                # print(f'{customer[0]}\t{customer[1]}\t{customer[2]}\t{customer[3]}\t{customer[4]}\t\t{customer[5]}\t{customer[6]}\t\t{customer[7]}')

        except Error as e:
            print(" Error :: Inside Credit >> initiateCustomerBalance method of credit class..")
            print(e)


    def getCustomerByAccountID(self, account_number):
        try:
            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            # connection.execute("Select * from CustomerDetails where account_id = (?)", (account_number,))
            # customer = connection.fetchall()
            # print("Customer details : ", customer)
            # conn.close()
            #
            # return customer

            self.connection.execute("Select * from CustomerDetails where account_id = (?)", (account_number,))
            customer = self.connection.fetchall()
            print("Customer details : ", customer)

            return customer


        except Error as e:
            print(" Error :: Inside View_table >> ViewCustomer method of Register class..")
            print(e)



# r = Report()
# # r.allCustomerDetails()
# r.getCustomerTransactions(1003)