from flask_app.models.user import User
from flask_app import app
from flask import render_template, jsonify, request, redirect
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    return jsonify(User.get_all_json())

@app.route('/create/user', methods=['POST'])
def create_user():
    
    print(request.form)
    
    User.save(request.form)
    
    return jsonify(message = "Adding a user")        
    