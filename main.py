from help import *
from data.repository import *
from logic.repo_search import *


user_date_format : str = '%d %m %Y'
types = {
    1: "מים",
    2: "חשמל",
    3: "גז"
    }
dir = r'C:\PythonProjects\payments\counters.csv'

def main():
    print_types()
    chosen_type : int = int(input())
    # chosen_type : int = 2
    while types.__contains__(chosen_type):
        preform_calc(chosen_type=types[chosen_type])
        print_types()
        chosen_type = int(input())

def preform_calc(chosen_type: str):
    bill : BilModel = create_bill_model(user_date_format=user_date_format)
    repo = create_repo(directory=dir)
    start = get_before_and_after_readings(chosen_type, bill.date_start, repo)
    aprox_start = calc_approximately_count(start[0], start[1], bill.date_start)
    end = get_before_and_after_readings(chosen_type, bill.date_end, repo)
    aprox_end = calc_approximately_count(end[0], end[1], bill.date_end)
    result = period_bills(bill.price, bill.count_use, aprox_end - aprox_start, "bialik", "green")
    print (result)


def calc_approximately_count(a, b, wanted_date):
    if a["date"] > b["date"]:
        help = a
        a = b
        b = help
    a_to_w_days = (wanted_date.date() - a["date"].date()).days
    w_to_b_days = (b["date"].date() - wanted_date.date()).days
    a_to_b_days = (b["date"].date() - a["date"].date()).days
    return ((a_to_w_days * b["count"]) + (w_to_b_days * a["count"])) / a_to_b_days

def period_bills(over_all_price, over_all_usage, apartment_usage, apartment_name, other_apartment_name):
    apartment_price = (over_all_price / over_all_usage) * apartment_usage
    other_apartment_price = over_all_price - apartment_price
    other_apartment_usage = over_all_usage - apartment_usage
    result = {apartment_name: {"usage": apartment_usage, "price": apartment_price},
              other_apartment_name: {"usage": other_apartment_usage, "price": other_apartment_price}}
    return result

def print_types():
    print("please enter the counter type: ")
    print(types)

    
main()