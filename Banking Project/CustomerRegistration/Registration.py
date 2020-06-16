from sqlite3 import Error
import sqlite3

class Register:

    def __init__(self, connection):
        self.connection = connection

    # Get the customer details - PAN card
    def getCustomerPanCard(self):
        customer_pan_card = input("Enter PAN card for user : ")
        return customer_pan_card

    def initiateCustomerRegistration(self):
        # Get the PAN card number first
        customer_pan_card = self.getCustomerPanCard()
        while (len(customer_pan_card) < 5):
            print("Enter correct PAN Card number!")
            customer_pan_card = self.getCustomerPanCard()

        # Check if customer already exists
        # self.checkPANcard(customer_pan_card)

        # Get other customer details
        customer_first_name = input("Enter customer first name : ")
        customer_last_name = input("Enter customer last name : ")
        customer_age = input("Enter customer Age : ")
        customer_city = input("Enter customer City : ")
        customer_gender = input("Enter customer Gender : ")
        acc_id = self.addNewCustomer(100, customer_pan_card, customer_first_name, customer_last_name, customer_gender, customer_age, customer_city)
        return acc_id

    def addUniqueNewCustomer(self, func):
        # use this method for decorator
        func()
    # also handle setting balance to 0 here
    # can remove above return acc_id in initiateCustomerRegistration


    def addNewCustomer(self, account_number, PAN_card, first_name, last_name, gender, age, city):
        try:
            account_number = int(self.getMaxAccountID())+1

            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            # connection.execute("Insert into CustomerDetails(account_id,first_name,last_name,pan_number,gender,age,city) values (?,?,?,?,?,?,?)", (account_number,PAN_card,first_name,last_name,gender,age,city))
            # conn.commit()
            # conn.close()

            # customer = self.getCustomerByRowID(connection.lastrowid)
            # # acc = connection.lastrowid
            # print("Account ID created : ", customer[0])
            # return int(customer[0])


            self.connection.execute("Insert into CustomerDetails(account_id,first_name,last_name,pan_number,gender,age,city) values (?,?,?,?,?,?,?)", (account_number,PAN_card,first_name,last_name,gender,age,city))

            customer = self.getCustomerByRowID(self.connection.lastrowid)
            print("Account ID created : ", customer[0])
            return int(customer[0])

        except Error as e:
            print(" Error :: Inside create_table >> AddNewCustomer method of Register class..")
            print(e)

    def getCustomerByRowID(self, row_id):
        try:
            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            # connection.execute("Select * from CustomerDetails where rowid = (?)", (row_id,))
            # customer = connection.fetchone()
            # # print("Account created : ", connection.fetchall())
            # # print("Customer details : ", customer)
            # conn.close()
            #
            # return customer


            self.connection.execute("Select * from CustomerDetails where rowid = (?)", (row_id,))
            customer = self.connection.fetchone()
            # print("Account created : ", connection.fetchall())
            # print("Customer details : ", customer)
            return customer

        except Error as e:
            print(" Error :: Inside View_table >> ViewCustomer method of Register class..")
            print(e)

    def getMaxAccountID(self):
        try:
            # conn = sqlite3.connect(self.db_path)
            # connection = conn.cursor()
            # connection.execute("Select max(account_id) from CustomerDetails")
            # max_account_id = connection.fetchone()
            # # print("Max Account ID : ", max_account_id[0])
            # conn.close()
            #
            # return max_account_id[0]


            self.connection.execute("Select max(account_id) from CustomerDetails")
            max_account_id = self.connection.fetchone()
            # print("Max Account ID : ", max_account_id[0])

            return max_account_id[0]

        except Error as e:
            print(" Error :: Inside View_table >> ViewCustomer method of Register class..")
            print(e)





# r = Register()
# r.getMaxAccountID()