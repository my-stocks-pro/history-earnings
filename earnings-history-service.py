from flask import Flask, render_template
from flask_cors import CORS
from classEarnings import Earnings

server = Flask(__name__)
cors = CORS(server, resources={r"/api/*": {"origins": "*"}})


@server.route("/history/earnings", methods=['GET'])
def range():
    return "test app..."


if __name__ == '__main__':
    earnings = Earnings()
    server.run(host='127.0.0.1', port=8003)
