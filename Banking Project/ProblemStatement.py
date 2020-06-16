# --Show below Options at start-
# 1. Add New Customer
# 2. Add Credit Entry
# 3. Add debit Entry
# 4. Search
# 5. Reports
#
# User can select option from above to proceed.
# ----------------------------------------------
# Requirements -
#
# 1. Add New Customer - save to Cust_Details.csv
#    Auto generate Cust id
# 2. Credit function -
#    write to transactions.csv
#    Add credit transaction and update balance in Cust_Details.csv
#    auto generate transaction id
# 3. Debit function -
#    write to transactions.csv
#    Add debit transaction and update balance in Cust_Details.csv
#    auto generate transaction id
# 4. Show all transactions function
#    pass customer id/name and print all transactions as per date (recent first)
# 5. Search Customer
#    Use RE to search customer
# 6. use lambda or map somewhere for calculations
# 7. Create Class for debit, credit and customer mgmt
# 8. Use decorators for credit and debit functions for logging purpose. Save this logging details with time.
# 9. create few function whichs will be like reports.
#    try to use tuples, dict, set here
# 10.Function to chose and correct data for any customer or any transaction
# 11.All code to be done in pycharm
# 12.use print formatting while displaying outputs.
# 13.try to create function with * arguments
#
#
#
#
# import csv
#
# # Create New file and write data into it
# buffer = [
#           ['First_Name', 'Last_Name', 'Age', 'Address', 'Gender'],
#           ['Ravi', 'Patel', '30', 'Poladpur', 'Male'],
#           ['Manoj', 'Bangad', '31', 'Ichalkaranji', 'Male']
#           ]
#
# with open('Cust_Details.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(buffer)
#
#
#
# # Read csv data into List
# with open('Cust_Details.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)
#
#
#
# #Append data to existing file
# buffer = [
#           ['Shashank', 'Nigade', '29', 'Pune', 'Male']
#           ]
#
# with open('Cust_Details.csv', 'a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(buffer)
#
#
