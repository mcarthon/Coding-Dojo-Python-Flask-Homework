from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<int:url_x>")
@app.route("/<int:url_x>/<int:url_y>")
@app.route("/<string:url_color1>")
@app.route("/<int:url_x>/<string:url_color1>")
@app.route("/<int:url_x>/<int:url_y>/<string:url_color1>/<string:url_color2>")
def home_page(url_x: int = 8, url_y: int = 8, url_color1: str = "red", url_color2: str = "black") -> None:
    return render_template("red-black-board.html", html_color1=url_color1,
                           html_color2=url_color2,
                           html_x=url_x,
                           html_y=url_y)


if __name__ == "__main__":
    app.run(debug=True, port = 5002)
