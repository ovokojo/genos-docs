import time
from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS, cross_origin

load_dotenv()

# loading variables from the .env file
FLASK_APP_PORT = os.getenv("FLASK_APP_PORT")

app = Flask(__name__)
cors = CORS(appresources={"*": {"origins": "http://localhost:3000"}})
# app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/time')
@cross_origin()
def get_current_time():
    print(time.time())
    return {'time': time.time()}


@app.route('/')
def get_default():
    return "<p> hi this is genos docs<p>"

if __name__ == "__main__":
    app.run(debug=False, port=FLASK_APP_PORT)