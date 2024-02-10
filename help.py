from datetime import datetime
from data.repository import *
from models import BilModel

def create_bill_model (user_date_format : str = '%d %m %Y') -> BilModel :
    print("enter beginning date (dd mm yyyy): ", end="")

    # date_start = datetime.strptime(input(), user_date_format)
    date_start = datetime.strptime("22 10 2023", user_date_format)

    print("enter end date (dd mm yyyy): ", end="")
    # date_end = datetime.strptime(input(), user_date_format)
    date_end = datetime.strptime("05 12 2023", user_date_format)
    
    print("enter price: ", end="")
    # price = float(input())
    price = float(526) # without the suldeir discount
    
    print("enter amount of usage: ", end="")
    # count_use = float(input())
    count_use = float(1088)
    
    return BilModel(date_start, date_end, price, count_use)

def create_repo( counters_types : list[str] = ["גז", "חשמל", "מים"] , directory : str = r'C:\Users\nobia\Downloads\counters.csv'):
    repo = Repository(counters_names=counters_types)
    repo.take_data_from_csv(directory)
    return repo