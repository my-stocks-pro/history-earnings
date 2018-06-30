from __future__ import print_function
import requests
# import browser_cookie3
import time


class NetworkError(RuntimeError):
    pass


class Requester:
    def __init__(self):
        # self.cookies = browser_cookie3.chrome()
        self.cookies = {"session": "s%3AFLsDQ0KkRmbbHJSFijJz_5VxQPCQI7Ol.t5LQWhFeOPA9qV2S0fqa6JBsFB0Rq%2BrxMDPc1URXyHE"}
        print("LOGIN to Shutterstock...")

    def retryer(max_retries=10, timeout=5):
        def wraps(func):
            request_exceptions = (
                requests.exceptions.Timeout,
                requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError)

            def inner(*args, **kwargs):
                for i in range(max_retries):
                    try:
                        result = func(*args, **kwargs)
                    except request_exceptions:
                        time.sleep(timeout)
                        continue
                    else:
                        return result
                else:
                    raise NetworkError

            return inner

        return wraps

    @retryer(max_retries=10, timeout=2)
    def get_response(self, url):
        return requests.get(url, cookies=self.cookies)

    def get_data_frame(self, url):
        return self.get_response(self, url).text.split("\n")

    def get_request(self):
        pass
