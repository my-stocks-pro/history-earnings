from flask import Flask, render_template, request, flash
from flask_cors import CORS
from classEarnings import Earnings
import pandas as pd



# app = Flask(__name__)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#
#
# @app.route("/history/earnings", methods=['GET'])
def get_data():
    # query = request.args
    # earnings.start = query.get('start')
    # earnings.end = query.get('end')
    earnings.start = pd.to_datetime("2018-05-01")
    earnings.end = pd.to_datetime("2018-06-01")
    earnings.get()
    return ""




if __name__ == '__main__':
    earnings = Earnings()
    # test()
    get_data()
    # app.run(host='127.0.0.1', port=8003)
