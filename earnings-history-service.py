from flask import Flask, render_template, request, flash
from flask_cors import CORS
from classEarnings import Earnings
import pandas as pd
import json


app = Flask(__name__)
cors = CORS(app, resources={r"/api-server/*": {"origins": "*"}})
app.debug = True


@app.route("/history/earnings", methods=['GET'])
def get_data():
    date = json.loads(request.data)
    print(date)
    print(type(date))
    earnings.start = pd.to_datetime(date.get('Start'))
    earnings.end = pd.to_datetime(date.get('End'))

    # earnings.start = pd.to_datetime("2018-05-01")
    # earnings.end = pd.to_datetime("2018-06-01")
    earnings.get()
    return ""


if __name__ == '__main__':
    conf_path = "./config.yaml"
    log_path = "./app_logs"
    earnings = Earnings(conf_path, log_path)
    app.run(host='127.0.0.1', port=8003)
