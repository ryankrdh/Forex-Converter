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

#   QUESTION: Methods="POST") when do we use this..? It seems app.route works even without it.
@app.route("/currency", methods=['POST'])
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
    convert_to_check, convert_from_check, amount_check = currency_rate.check_valid_input(convert_to_input, convert_from_input, money_amount_input)

    # Checking for invalid input.
    invalid_inputs = []
    if convert_to_check != True:
        invalid_inputs.append(f"Not a valid code: {convert_to_input}. Please type in proper exchange symbol for 'converting to'")
    if convert_from_check != True:
        invalid_inputs.append(f"Not a valid code: {convert_from_input}. Please type in proper exchange symbol for 'converting from'")
    if amount_check != True:
        invalid_inputs.append(f"Not a valid amount: {money_amount_input}. Please type in a proper amount")

    if invalid_inputs:
        for invalids in invalid_inputs:
            flash(invalids)
        return render_template("index.html")

    # else:
    convert_to_name, convert_from_name, converted_amount, convert_from_symbol = currency_rate.calculate(convert_to_input, convert_from_input, money_amount_input)

    return render_template("index.html", convert_to_name = convert_to_name, convert_from_name = convert_from_name, converted_amount = converted_amount, money_amount_input = money_amount_input, convert_from_symbol = convert_from_symbol)



