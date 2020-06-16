

import csv

def registerCustomer():
    source_cust_data_file = r"E:\Python Class\Pycharm HandsOn\BankingDemoProject\Data Files\CustomerData.csv"
    with open(source_cust_data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['a','b','c','d'])

registerCustomer()


def addNewCustomer(self, account_number, PAN_card, first_name, last_name, gender, age, city):
    source_cust_data_file = r"E:\Python Class\Pycharm HandsOn\BankingDemoProject\Data Files\CustomerData.csv"
    with open(self.source_cust_data_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows([account_number, PAN_card, first_name, last_name, gender, age, city])

if __name__ == '__main__':
    # addNewCustomer(source_cust_data_file, "Manoj", "b", "a", "b", "a", "b", "a", "KL")
    addNewCustomer("Manoj", "b", "a", "b", "a", "b", "a", "KL")