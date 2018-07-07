from classRequest import Requester
import json
import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY
import pandas as pd


class Earnings(Requester):
    def __init__(self):
        Requester.__init__(self)
        self.start = ""
        self.end = ""
        self.urls = [
            "https://submit.shutterstock.com/earnings/daily?page={}&date={}&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20",
            "https://submit.shutterstock.com/earnings/daily?page={}&date={}&language=en&category=on_demand&sort=desc&sorted_by=count&per_page=20",
            "https://submit.shutterstock.com/earnings/daily?page={}&date={}&language=en&category=enhanced&sort=desc&sorted_by=count&per_page=20",
            "https://submit.shutterstock.com/earnings/daily?page={}&date={}&language=en&category=single_image_and_other&sort=desc&sorted_by=count&per_page=20"]

    def date_list(self):
        return [dt for dt in rrule(MONTHLY, dtstart=self.start, until=self.end)]

    def get(self):
        dl = self.date_list()
        for date in dl:
            self.get_by_date(date)

    def get_by_date(self, date):
        for url in self.urls:
            page = 1
            while True:
                tmp_url = url.format(str(page), str(date.strftime('%Y-%m-%d')))
                try:
                    r = self.get_response(tmp_url)
                    if int(r.url[r.url.index("=") + 1:r.url.index("&")]) < page:
                        print("empty url ->" + tmp_url)
                        # self.to_logger("empty url ->" + tmp_url)
                        break
                    # self.to_logger(tmp_url)
                    print(tmp_url)
                    page += 1
                    try:
                        df = pd.read_html(r.content)
                        self.processing_dataframe(df)
                    except ValueError:
                        # self.to_logger(ValueError)
                        print(ValueError)
                        break
                except():
                    print("error in request")
                    # self.to_logger("error in request")

    def processing_dataframe(self, df):
        pass