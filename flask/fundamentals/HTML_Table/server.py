from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def render_table():

    users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    users_length = len(users)

    return render_template("html_table.html", 
    users = users, 
    users_length = users_length
    )

if __name__ == "__main__":
    app.run(debug = True)