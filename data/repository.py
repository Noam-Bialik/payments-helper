import csv
from colorama import Fore, Style
from datetime import datetime

date_format = '%d-%m-%Y %H:%M:%S'
counter_name_index = 1
time_index_in_row = 0
count_index_in_row = 2

class Repository:
    def __init__(self, counters_names):
        self.apartment_counters = {}
        for name in counters_names:
            self.apartment_counters[name] = ApartmentCounter(name)

    def take_data_from_csv(self, file_path):
        rows = get_csv_as_list(file_path)
        for row in rows:
            if row[counter_name_index] in self.apartment_counters:
                date = datetime.strptime(row[time_index_in_row].replace("/", "-"), date_format)
                count = float(row[count_index_in_row])
                self.apartment_counters[row[counter_name_index]].readings[date] = count

    def __str__(self):
        return str(self.apartment_counters)

    def print(self):
        for k in self.apartment_counters:
            self.apartment_counters[k].print()


class ApartmentCounter:
    
    def __init__(self, name):
        self.name = name
        self.readings = {}

    def __str__(self):
        return str(self.readings)
    
    def __repr__(self):
        return str(self.readings)

    def print(self):
        print(Fore.GREEN, end="")
        print(self.name)
        print(Style.RESET_ALL, end = "")
        print(self.readings)
    
def get_csv_as_list(file_path):
    with open(file_path, 'r', encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        list_of_csv = list(csv_reader)
        return list_of_csv