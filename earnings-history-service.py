from flask import Flask, render_template, request, flash
from flask_cors import CORS
from classEarnings import Earnings

app = Flask(__name__)
# app.debug = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/history/earnings", methods=['GET'])
def get_data():
    query = request.args
    earnings.start = query.get('start')
    earnings.end = query.get('end')
    earnings.get()
    return ""

# @server.route("/history/earnings", methods=['POS'])
# def range():
#     return


if __name__ == '__main__':
    earnings = Earnings()
    app.run(host='127.0.0.1', port=8003)

