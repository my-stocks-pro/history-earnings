from flask import Flask, render_template
from flask_cors import CORS


class ServerAPI:
    def __init__(self):
        self.api = Flask(__name__)
        self.cors = CORS(self.api, resources={r"/api/*": {"origins": "*"}})

    def init_routing(self):
        pass