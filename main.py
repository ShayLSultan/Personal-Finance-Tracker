import pandas as pd
import csv 
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

class CSV:
    csv_file = "finance_data.csv"
    the_columns = ["date", "amount", "category", "description"]

    @classmethod
    def init_csv(cls):
        try:
            pd.read_csv(cls.csv_file) 
        except FileNotFoundError:
            data_frame = pd.DataFrame(columns = cls.the_columns)
            data_frame.to_csv(cls.csv_file, index = False)
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.csv_file, "a", newline = "") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = cls.the_columns)
            writer.writerow(new_entry)
        print("Entry successfully added")
    
def add(): 
    CSV.init_csv()
    date = get_date("Please enter the date of the transaction as follows: dd-mm-yyyy, or press ENTER for today's date", allow_default = True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


add()