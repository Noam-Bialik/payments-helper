from datetime import datetime

from models import BilModel

def period_bills(over_all_price, over_all_usage, apartment_usage, apartment_name, other_apartment_name):
    apartment_price = (over_all_price / over_all_usage) * apartment_usage
    other_apartment_price = over_all_price - apartment_price
    other_apartment_usage = over_all_usage - apartment_price
    result = {apartment_name: {"usage": apartment_usage, "price": apartment_price},
              other_apartment_name: {"usage": other_apartment_usage, "price": other_apartment_price}}
    return result


def calc_approximately_count(a, b, wanted_date):
    if a["date"] > b["date"]:
        help = a
        a = b
        b = help
    return (((wanted_date - a["date"]).days * b["count"]) + ((b["date"] - wanted_date).days * a["count"])) / (
            b["date"] - a["date"]).days


def get_date(d, f='%d-%m-%Y'):
    return datetime.strptime('-'.join(d.split("/")), f)


def calc(bill: BilModel):



# todo: need to calc CALC


a = period_bills(123, 1422, 300, "bialik", "grin")
print(a)

up_first_aprox_count = calc_approximately_count(
    {"date": get_date("07/02/2023"), "count": 6017},
    {"date": get_date("03/02/2023"), "count": 5963},
    get_date("06/02/2023"))
up_last_aprox_count = calc_approximately_count({"date": get_date("07/02/2023"), "count": 6017},
                                               {"date": get_date("03/02/2023"), "count": 5963},
                                               get_date("06/02/2023"))

print(b)
