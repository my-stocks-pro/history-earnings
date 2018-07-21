from classRequest import Requester
from classLogger import Logger
from classConfiger import Configer
from dateutil.rrule import rrule, MONTHLY, DAILY
import pandas as pd


class Earnings(Requester, Logger, Configer):
    def __init__(self, conf_path, log_path):
        Configer.__init__(self, conf_path)
        Requester.__init__(self, self.config.get('hosts'), self.config.get('ports'))
        Logger.__init__(self, self.config.get('service'), log_path)
        self.start = None
        self.end = None
        self.categories = self.config.get('categories')
        self.base_url = self.config.get('base_url')

    def date_list(self):
        if self.start is None or self.end is None:
            return None
        return [dt for dt in rrule(DAILY, dtstart=self.start, until=self.end)]

    def get(self):
        dl = self.date_list()
        if dl is None:
            print("Dates are not set...")
        else:
            for date in dl:
                self.get_by_date(date)

    def get_by_date(self, curr_date):
        curr_date = curr_date.strftime('%Y-%m-%d')
        for category_base, category_name in self.categories.items():
            page = 1
            while True:
                tmp_url = self.base_url.format(str(page), curr_date, category_base)
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
                        list_id, list_ernings, list_downloads = self.get_new_data(df, category_name)
                    except ValueError:
                        # self.to_logger(ValueError)
                        print(ValueError)
                        break
                    self.processing_dataframe(list_id, list_ernings, list_downloads, curr_date, category_name)
                except():
                    print("error in request")

    @staticmethod
    def get_new_data(df, category):
        print(category)
        df = df[0]
        list_id = df[df.columns[1]].tolist()  # ID
        list_ernings = df[df.columns[2]].tolist()  # Earnings
        list_downloads = df[df.columns[3]].tolist()  # Downloads
        return list_id, list_ernings, list_downloads

    def processing_dataframe(self, list_idi, list_erns, list_dls, curr_date, category):
        for idi, erns, dls in zip(list_idi, list_erns, list_dls):
            country, city = None, None
            self.post_to_api_postgres(curr_date, idi, dls, erns, country, city, category)
