#!/bin/bash

project_folder_name="flask_app"

project_name="users"

mkdir $project_folder_name

cd project_folder_name

touch server.py

pipenv install flask PyMySQL

cd project_name

mkdir config controllers models static templates

touch __init__.py credentials.py .gitignore

touch ./config/mysqlconnection.py 

touch "./controllers/${project_name}.py"

touch  "./models/${project_name}.py"

touch  "./static/${project_name}.css"

touch "./templates/${project.name}.html"