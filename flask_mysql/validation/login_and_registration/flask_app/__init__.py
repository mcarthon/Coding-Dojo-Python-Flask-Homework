from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "polar bear"

schema = "login_registration_schema"

bcrypt = Bcrypt(app)