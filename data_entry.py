from datetime import datetime

date_format = "%d-%m-%Y"
categories = {"I": "Income", "E": "Expense"}
accounts = {"C": "Current", "S": "Savings"}

def get_date(prompt, allow_default = False):
    date_string = input(prompt)
    if allow_default and not date_string:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_string, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date as follows: dd-mm-yyyy ")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be more than zero ")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the Category: 'I' for Income or 'E' for Expense ").upper()
    if category in categories:
        return categories[category]
    else: 
        print("Invalid category, please enter 'I' for Income or 'E' for Expense ")
        return get_category()

def get_account():
    account = input("Enter the account you would like to access: 'C' for Current or 'S' for Savings ").upper()
    if account in accounts:
        return accounts[account]
    else: 
        print("Invalid response, please enter 'C' for Current or 'S' for Savings ")
        return get_account()

def get_description():
    return input("Enter a description (optional) ")