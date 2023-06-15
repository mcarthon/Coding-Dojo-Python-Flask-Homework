
#!/bin/bash

project_folder_name="books"

mkdir "${project_folder_name}"

cd "${project_folder_name}"

#project_name="users"

mkdir flask_app

touch server.py

pipenv install flask PyMySQL

cd flask_app

mkdir config controllers models static templates

touch __init__.py credentials.py .gitignore

touch ./config/mysqlconnection.py

#touch "./controllers/${project_name}.py"

#touch "./models/${project_name}.py"

#touch "./static/${project_name}.css"

#touch "./templates/${project_name}.html"
