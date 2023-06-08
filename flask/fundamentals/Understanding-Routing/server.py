from flask import Flask

app = Flask(__name__)

@app.route("/")
def home_page():
	return "Hello World"

@app.route("/dojo")
def dojo_page():
	return "Dojo"

@app.route("/say/<name>")
def say_name(name: str) -> str:
	return f"Hi {name[0].upper()}{name[1:]}!"

@app.route("/repeat/<number>/<text>")
def repeat_text(number: int, text: str) -> str:
	return text * int(number)

@app.errorhandler(404)
def catch_all(e) -> str:
	return "Page Not Found.\nTry new URL", 404

if __name__ == "__main__":
	app.run(debug = True)


