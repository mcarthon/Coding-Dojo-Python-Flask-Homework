#!/bin/bash

projectname = "Ninja-Gold"
mkdir projectname
cd ./projectname
mkdir ./templates ./static
touch server.py ./templates/projectname.html ./static/projectname.css
pipenv install flask
