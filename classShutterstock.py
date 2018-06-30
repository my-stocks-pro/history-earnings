

class Shutterstock:
    def __init__(self):
        self.urls = [
            "https://submit.shutterstock.com/earnings/daily?page={}&date={}&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20",
            "https://submit.shutterstock.com/earnings/daily?page={}&date={}&language=en&category=on_demand&sort=desc&sorted_by=count&per_page=20",
            "https://submit.shutterstock.com/earnings/daily?page={}&date={}&language=en&category=enhanced&sort=desc&sorted_by=count&per_page=20",
            "https://submit.shutterstock.com/earnings/daily?page={}&date={}&language=en&category=single_image_and_other&sort=desc&sorted_by=count&per_page=20"]

    def get_earnings(self):
        pass
        # for url in self.urls:
        #     page = 1
        #     while True:
        #         tmp_url = url.format(str(page), str(date_current))
        #         try:
        #             r = request.get_response(tmp_url)
        #         except():
        #             self.to_logger("error in request")
        #         if int(r.url[r.url.index("=") + 1:r.url.index("&")]) < page:
        #             self.to_logger("empty url ->" + tmp_url)
        #             break
        #         self.to_logger(tmp_url)
        #         page += 1
        #         try:
        #             df = pd.read_html(r.content)
        #         except ValueError:
        #             print(ValueError)
        #             break
