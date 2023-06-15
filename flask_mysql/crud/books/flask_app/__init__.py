from flask import Flask
app = Flask(__name__)
app.secret_key = "java world"
schema = "books_schema"