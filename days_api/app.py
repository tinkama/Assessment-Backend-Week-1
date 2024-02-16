"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime

from flask import Flask, request, jsonify, abort

from date_functions import convert_to_datetime, get_day_of_week_on, get_days_between

app_history = []

app = Flask(__name__)


def add_to_history(current_request):
    """Adds a route to the app history."""
    if current_request == 0:
        return app_history

    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })


@app.get("/")
def index():
    """Returns an API welcome messsage."""
    return jsonify({"message": "Welcome to the Days API."})


@app.route("/between", methods=['POST'])
def difference_in_date(first, last):
    """Returns the difference in date"""

    if first is None or last is None:
        abort(400)
    else:
        data = request.json
        data['first'] = first
        data['last'] = last
        first_date = convert_to_datetime(first)
        last_date = convert_to_datetime(last)
        if not isinstance(first_date, datetime) or not isinstance(last_date, datetime):
            abort(400)
        else:
            data['days'] = get_days_between(first_date, last_date)
            add_to_history(request.method)
            return jsonify(data)


@app.route("/weekday", methods=['POST'])
def difference_in_week(date):
    """Returns the weekday"""

    if date is None:
        abort(400)
    else:
        data = request.json
        date_datetime = convert_to_datetime(date)
        if isinstance(date_datetime, ValueError):
            abort(400)
        data["weekday"] = get_day_of_week_on(date_datetime)
        print(data)
        add_to_history(request.method)
        return jsonify(data)


@app.route("/history", methods=['GET', 'DELETE'])
def show_history():
    """Shows the history of the API."""
    app_history = add_to_history(0)
    if request.method == 'GET':
        return jsonify(app_history)
    if request.method == 'DELETE':
        app_history = []
        return jsonify({"status": "History cleared"})


if __name__ == "__main__":
    app.run(port=8080, debug=True)
