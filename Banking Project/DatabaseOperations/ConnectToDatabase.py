import sqlite3
from sqlite3 import Error

class DatabaseActions:

    conn = None

    def __init__(self, db_file):
        ## create/connect a database connection to a SQLite database
        try:
            self.db_file = db_file
            self.conn = sqlite3.connect(self.db_file)
            print("\nCreated the database instance : " , sqlite3.version)
        except Error as e:
            print("Error :: In constructor of Database Actions class..")
            print(e)
        # finally:
        #     if conn:
        #         conn.close()

    def create_table_CustomerDetails(self):
        # conn = sqlite3.connect(self.db_file)
        try:
            self.conn.execute("CREATE TABLE CustomerDetails(account_id INTEGER PRIMARY KEY,first_name TEXT NOT NULL,last_name TEXT NOT NULL,pan_number TEXT NOT NULL,gender TEXT,age INTEGER NOT NULL,city TEXT NOT NULL)")
            print("\nCustomerDetails table created successfully..")
        except Error as e:
            print(" Error :: Inside create_table method of Database Actions class..")
            print(e)

    def create_table_CustomerTransactions(self):
        # conn = sqlite3.connect(self.db_file)
        try:
            self.conn.execute(
                "CREATE TABLE CustomerTransactions(account_id INTEGER,transaction_type TEXT NOT NULL,amount INTEGER NOT NULL,date_time TEXT)")
            print("\nCustomerTransactions table created successfully..")
        except Error as e:
            print(" Error :: Inside create_table method of Database Actions class..")
            print(e)

    def create_table_CustomerBalance(self):
        # conn = sqlite3.connect(self.db_file)
        try:
            self.conn.execute(
                "CREATE TABLE CustomerBalance(account_id INTEGER, amount Numeric NOT NULL)")
            print("\nCustomerBalance table created successfully..")
        except Error as e:
            print(" Error :: Inside create_table method of Database Actions class..")
            print(e)

    def drop_table(self):
        try:
            self.conn.execute("Drop TABLE CustomerDetails")
            print("\nCustomerDetails table dropped successfully..")
        except Error as e:
            print(" Error :: Inside drop_table method of Database Actions class..")
            print(e)


##############

db_file = "E:\Python Class\Pycharm HandsOn\BankingDemoProject\Data Files\ProjectDB.db"
da = DatabaseActions(db_file)
# da.create_table_CustomerDetails()
# da.create_table_CustomerTransactions()
da.create_table_CustomerBalance()
# da.drop_table()