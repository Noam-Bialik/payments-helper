from datetime import datetime
from data.repository import Repository

def get_before_and_after_readings(counter_name : str, date : datetime, reop : Repository):
    before = None
    after = None
    dates = sorted(list(reop.apartment_counters[counter_name].readings), reverse=True)
    for check_date in dates:
        if check_date >= date:
            after = check_date
        elif check_date <= date:
            before = check_date
            break
    return [{"date" : before, "count" :reop.apartment_counters[counter_name].readings[before]},{"date": after, "count": reop.apartment_counters[counter_name].readings[after]}]

    
# r = Repository(["גז"])
# r.take_data_from_csv("counters.csv")
# print(get_before_and_after_readings("גז" ,datetime(2023,2,1),r))
