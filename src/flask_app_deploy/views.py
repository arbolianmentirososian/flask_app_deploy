from flask import jsonify, make_response

from flask_app_deploy import app


@app.route("/", methods=['GET'])
def hello():
    """ Test function that returns string 'Hello, world!'.
        It can be used to check whether application is running.
    """
    return "Hello, world!\n"


@app.route("/add/<int:num1>/<int:num2>", methods=['GET'])
def add(num1, num2):
    """Calculates the sum of two integer numbers passed into the function.

        Parameters
        ----------
            num1: int
                The first number.
            num2: int
                The second number.

        Returns
        -------
            JSON
                JSON containing values of passed in numbers and their sum.
    """
    response = {
        "num1": num1,
        "num2": num2,
        "num1 + num2": num1 + num2,
    }
    return make_response(jsonify(response), 200)


@app.route("/subtract/<int:num1>/<int:num2>", methods=['GET'])
def subtract(num1, num2):
    """Calculates the difference of two integer numbers passed into the function.

        Parameters
        ----------
            num1: int
                The first number.
            num2: int
                The second number.

        Returns
        -------
            JSON
                JSON containing values of passed in numbers and their difference.
    """
    response = {
        "num1": num1,
        "num2": num2,
        "num1 - num2": num1 - num2,
    }
    return make_response(jsonify(response), 200)


@app.route("/multiply/<int:num1>/<int:num2>", methods=['GET'])
def multiply(num1, num2):
    """Calculates the product of two integer numbers passed into the function.

        Parameters
        ----------
            num1: int
                The first number.
            num2: int
                The second number.

        Returns
        -------
            JSON
                JSON containing values of passed in numbers and their product.
    """
    response = {
        "num1": num1,
        "num2": num2,
        "num1 * num2": num1 * num2,
    }
    return make_response(jsonify(response), 200)


@app.route("/divide/<int:num1>/<int:num2>", methods=['GET'])
def divide(num1, num2):
    """Calculates the quotient of two integer numbers passed into the function.

        Parameters
        ----------
            num1: int
                The first number.
            num2: int
                The second number.

        Returns
        -------
            JSON
                JSON containing values of passed in numbers and their quotient.
    """
    response = {
        "num1": num1,
        "num2": num2,
        "num1 / num2": num1 / num2,
    }
    return make_response(jsonify(response), 200)


@app.route("/modulo/<int:num1>/<int:num2>", methods=['GET'])
def modulo(num1, num2):
    """Calculates the remainder of division of two integer numbers passed into the function.

        Parameters
        ----------
        num1: int
            The first number.
        num2: int
            The second number.

        Returns
        -------
            JSON
                JSON response with values of passed in numbers and the remainder of their division.

    """
    response = {
        "num1": num1,
        "num2": num2,
        "num1 % num2": num1 % num2,
    }
    return make_response(jsonify(response), 200)
