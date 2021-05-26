from flask import Flask, jsonify, after_this_request

from resources.reports import reports

from resources.users import users

import models

from flask_cors import CORS

from flask_login import LoginManager

import os

from dotenv import load_dotenv

load_dotenv()

DEBUG=True
PORT=8000

app = Flask(__name__)

# app.config['CORS_HEADERS'] = 'Content-Type'

app.secret_key = os.environ.get("FLASK_APP_SECRET")

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return models.User.get(models.User.id == user_id)



#==== C O R S stuff goes here =====
CORS(reports, origins=['http://localhost:3000'], supports_credentials=True)

CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

# ======= use blueprint controllers here ========

app.register_blueprint(reports, url_prefix='/api/v1/reports')

app.register_blueprint(users, url_prefix='/api/v1/users')


# we don't want to hog up the SQL connection pool
# so we should connect to the DB before every request
# and close the db connection after every request

@app.before_request # use this decorator to cause a function to run before reqs
def before_request():

    """Connect to the db before each request"""
    print("you should see this before each request") # optional -- to illustrate that this code runs before each request -- similar to custom middleware in express.  you could also set it up for specific blueprints only.
    models.DATABASE.connect()

    @after_this_request # use this decorator to Executes a function after this request
    def after_request(response):
        """Close the db connetion after each request"""
        print("you should see this after each request") # optional -- to illustrate that this code runs after each request
        models.DATABASE.close()
        return response # go ahead and send response back to client
                      # (in our case this will be some JSON)


@app.route('/')

def test_csv():

    print('Hit test route')
    return "testing testing... 123"




if __name__ == '__main__':
    models.init()
    app.run(debug=DEBUG, port=PORT)

# ADD THESE THREE LINES -- because we need to initialize the
# tables in production too!
if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.init()
