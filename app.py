from flask import Flask, request, render_template
from currency import CurrencyCalculator

app = Flask(__name__)
app.config["SECRET_KEY"] = "rhk"

currency_rate = Currency

@app.route("/")
def homepage():
    """
    Displays the homepage.
    """

    return render_template("index.html")


@app.route("/currency")
def post_currency():
