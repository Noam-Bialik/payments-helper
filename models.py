from datetime import datetime
class BilModel:
    def __init__(self, date_start : datetime, date_end : datetime, price : float, count_use : float):
        self.date_start = date_start
        self.date_end = date_end
        self.price = price
        self.count_use = count_use

class ResultModel:
    def __init__(self, overall_price, overall_usage, aprox_price, aprox_usage):
        self.overall_price = overall_price
        self.overall_usage = overall_usage
        self.aprox_price = aprox_price
        self.aprox_usage =aprox_usage
