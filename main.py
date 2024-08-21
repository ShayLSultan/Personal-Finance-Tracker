import pandas as pd
import csv 
from datetime import datetime
from data_entry import get_date, get_account, get_amount, get_category, get_description
import matplotlib.pyplot as plt

class CSV:
    csv_file = "finance_data.csv"
    the_columns = ["date", "account", "amount", "category", "description"]
    date_format = "%d-%m-%Y"

    @classmethod
    def init_csv(self):
        try:
            pd.read_csv(self.csv_file) 
        except FileNotFoundError:
            data_frame = pd.DataFrame(columns = self.the_columns)
            data_frame.to_csv(self.csv_file, index = False)
    @classmethod
    def add_entry(self, date, account, amount, category, description):
        new_entry = {
            "date": date,
            "account": account,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(self.csv_file, "a", newline = "") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = self.the_columns)
            writer.writerow(new_entry)
        print("Entry successfully added")
    
    @classmethod
    def get_transactions(self, account, start_date, end_date):
        data_frame = pd.read_csv(self.csv_file)
        data_frame["date"] = pd.to_datetime(data_frame["date"], format = CSV.date_format)
        start_date = datetime.strptime(start_date, CSV.date_format)
        end_date = datetime.strptime(end_date, CSV.date_format)
        
        mask = (data_frame["date"] >= start_date) & (data_frame["date"] <= end_date)
        mask2 = (data_frame["account"] == account)
        half_filtered_data_frame = data_frame.loc[mask2]
        filtered_data_frame = half_filtered_data_frame.loc[mask]

        
        if filtered_data_frame.empty:
            print("No transactions found in this date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.date_format)} to {end_date.strftime(CSV.date_format)}")
            print(filtered_data_frame.to_string(index = False, formatters = {"date": lambda x: x.strftime(CSV.date_format)}))

            total_income = filtered_data_frame[filtered_data_frame["category"] == "Income"]["amount"].sum()
            total_expense = filtered_data_frame[filtered_data_frame["category"] == "Expense"]["amount"].sum()
            print("\nTotals:")
            print(f"Total Income: £{total_income:.2f}")
            print(f"Total Expense: £{total_expense:.2f}")
            print(f"Net Savings: £{(total_income - total_expense):.2f}")
        return filtered_data_frame
    
    
def add(): 
    CSV.init_csv()
    date = get_date("Please enter the date of the transaction as follows: dd-mm-yyyy, or press ENTER for today's date ", allow_default = True)
    account = get_account()
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, account, amount, category, description)

def plot_transactions(data_frame):
    data_frame.set_index("date", inplace = True)

    income_data_frame = data_frame[data_frame["category"] == "Income"].resample("D").sum().reindex(data_frame.index, fill_value = 0)
    expense_data_frame = data_frame[data_frame["category"] == "Expense"].resample("D").sum().reindex(data_frame.index, fill_value = 0)
    plt.figure(figsize = (10, 5))
    plt.plot(income_data_frame.index, income_data_frame["amount"], label = "Income", color = "g")
    plt.plot(expense_data_frame.index, expense_data_frame["amount"], label = "Expense", color = "r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction")
        print("\n2. View your transactions between a certain amount of time")
        print("\n3. Exit")
        choice = input("Please enter 1, 2, or 3 to select the option you would like. ")
        if choice == "1": 
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date in the format dd-mm-yyyy ")
            end_date = get_date("Enter the end date in the format dd-mm-yyyy ") 
            account = get_account()
            data_frame = CSV.get_transactions(account, start_date, end_date)
            if input("Do you want to see this in a graph? Enter 'Y' for yes or 'N' for no ").upper() == "Y":
                plot_transactions(data_frame)
        elif choice == "3":
            print("Exiting Personal Finance Tracker")
            break
        else:
            print("Invalid answer, please enter 1, 2, or 3 ")


if __name__ == "__main__":
    main()
