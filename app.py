from flask import Flask, jsonify

from resources.reports import reports


import models

from flask_cors import CORS

from flask_login import LoginManager

import os

from dotenv import load_dotenv

load_dotenv()

DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_APP_SECRET")

login_manager = LoginManager()

# login_manager.init_app()

@login_manager.user_loader
def load_user(user_id):
    return models.User.get(models.User.id == user_id)

#==== C O R S stuff goes here =====



# ======= use blueprint controllers here ========

app.register_blueprint(reports, url_prefix='/api/v1/reports')




@app.route('/')
def test_csv():

    print('Hit test route')
    return "testing testing... 123"




if __name__ == '__main__':
    models.init()
    app.run(debug=DEBUG, port=PORT)
