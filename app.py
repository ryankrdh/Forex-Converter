from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from currency import CurrencyCalculator

RESPONSES_KEY = "resposnes"
app = Flask(__name__)
app.config["SECRET_KEY"] = "rhk"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

currency_rate = CurrencyCalculator()

@app.route("/")
def show_forex_form():
    """
    redirects to currency exchange page.
    """
    
    return render_template("index.html")

@app.route("/currency")
def homepage():
    """
    Displays the currency exchange page.
    """
    # QUESTION: diff. between request.args and request.args.get.
    # why does the internet sometimes say () and []
    convert_to_input = request.args["convert_to"]
    convert_from_input = request.args["convert_from"]
    money_amount_input = request.args["money_amount"]
    
    convert_to_name, convert_from_name, converted_amount = currency_rate.calculate(convert_to_input, convert_from_input, money_amount_input)
    

    return redirect("index.html", convert_to_name = convert_to_name, convert_from_name = convert_from_name, converted_amount = converted_amount, convert_to_input = convert_to_input, convert_from_input = convert_from_input, money_amount_input = money_amount_input)

    # return render_template("index.html")


