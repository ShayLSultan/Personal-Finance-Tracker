import pandas as pd
import csv 
from datetime import datetime

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


CSV.init_csv()
CSV.add_entry("19-08-24", 100, "Expense", "Perfume")