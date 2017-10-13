import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
from flask import Flask
load_dotenv(dotenv_path)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

if __name__ == '__main__':

    handler = RotatingFileHandler(os.environ.get("ERRORLOG_FILENAME"), maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.run(
            host=os.environ.get("HTTP_HOST"),
            port=int(os.environ.get("HTTP_PORT")),
            debug=os.environ.get("HTT_DEBUG")
            )