from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello():
    return 'Good Morning , Everyone!!!! from Manpreet .....//...001'
