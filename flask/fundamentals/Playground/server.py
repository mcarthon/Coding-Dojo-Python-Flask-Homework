from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/play")
@app.route("/play/<int:url_n>")
@app.route("/play/<int:url_n>/<url_box_color>")
def box_color(url_n:int = 3, url_box_color: str = "blue") -> None:
	return render_template("x-boxes.html", html_n = url_n, html_box_color = url_box_color)

if __name__ == "__main__":
	app.run(debug = True)