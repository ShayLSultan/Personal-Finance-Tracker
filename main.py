import pandas as pd
import csv 
from datetime import datetime

class CSV:
    csv_file = "finance_data.csv"

    @classmethod
    def init_csv(cls):
        try:
            pd.read_csv(cls.csv_file) 
        except FileNotFoundError:
            data_frame = pd.DataFrame(columns = ["date", "amount", "category", "description"])
            data_frame.to_csv(cls.csv_file, index = False)

CSV.init_csv()