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
        self.map = ""
        self.url_map = "https://submit.shutterstock.com/api/user/downloads/map"
        self.categories = {"25_a_day": "subscription",
                           "on_demand": "onDemand",
                           "enhanced": "enhanced",
                           "single_image_and_other": "single&other"}
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
                    map = self.get_response(self.url_map)
                    self.map = json.loads(map.content)
                    print(tmp_url)
                    page += 1
                    try:
                        df = pd.read_html(r.content)
                        self.processing_dataframe(df, tmp_url)
                    except ValueError:
                        # self.to_logger(ValueError)
                        print(ValueError)
                        break
                except():
                    print("error in request")
                    # self.to_logger("error in request")

    def processing_dataframe(self, df, tmp_url):
        df = df[0]
        list_id = df[df.columns[1]].tolist()  # ID
        list_downloads = df[df.columns[3]].tolist()  # Downloads
        category = self.get_category(tmp_url)
        for idi, dow in zip(list_id, list_downloads):
            location = self.get_location(idi)
            print(idi, dow, location, category)

    def get_category(self, url):
        for category in self.categories.keys():
            if category in url:
                return self.categories.get(category)

    def get_location(self, idi):
        for location in self.map:
            media_id = location.get('media_id')
            if str(media_id) == idi:
                country = location.get('country')
                city = location.get('city')
                if country is None and city is not None:
                    country = city
                return "{}/{}".format(country, city)
