from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "I'm not your bruh"

bcrypt = Bcrypt(app)

schema = "artist_paintings_schema"