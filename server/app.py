#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route("/count/<parameter>")
def count(parameter):
    result = ""
    for i in range(int(parameter)):
        result += f"{i}\n"
    return result
@app.route("/math/<int:num1>/<operator>/<int:num2>")
def math(num1, operator, num2):
    if operator == "+":
        return str(num1 + num2)
    elif operator == "-":
        return str(num1 - num2)
    elif operator == "*":
        return str(num1 * num2)
    elif operator == "div":
        return str(num1 / num2)
    elif operator == "%":
        return str(num1 % num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
