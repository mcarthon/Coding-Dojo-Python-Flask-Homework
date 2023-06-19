from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "milton friedman"

schema = "private_wall"

bcrypt = Bcrypt(app)