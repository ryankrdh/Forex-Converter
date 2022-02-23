from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from currency import CurrencyCalculator


app = Flask(__name__)
app.config["SECRET_KEY"] = "rhk"

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

    # Testing Edge Cases
    convert_to_check, convert_from_check, amount_check= currency_rate.check_valid_input(convert_to_input, convert_from_input, money_amount_input)

    
    # Checking for invalid input.
    invalid_inputs = []
    if convert_to_check != True:
        invalid_inputs.append(convert_to_check)
    if convert_from_check != True:
        invalid_inputs.append(convert_from_check)
    if amount_check != True:
        invalid_inputs.append(amount_check)

    # if invalid_input list is true, it will end the function by returning render_template.
    if invalid_inputs:
        for invalids in invalid_inputs:
            flash(invalids)
        return render_template("index.html")

    # else:
    convert_to_name, convert_from_name, converted_amount, convert_from_symbol, codes_list = currency_rate.calculate(convert_to_input, convert_from_input, money_amount_input)

    return render_template("index.html", codes_list = codes_list, convert_to_name = convert_to_name, convert_from_name = convert_from_name, converted_amount = converted_amount, money_amount_input = money_amount_input, convert_from_symbol = convert_from_symbol)

    # return render_template("index.html")
