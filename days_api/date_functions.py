"""Functions for working with dates."""

from datetime import datetime
from datetime import timedelta


def convert_to_datetime(date: str) -> datetime:
    """Converts a string to Datetime"""
    valid_date = date.split(".")
    for i in valid_date:
        if not i.isdigit():
            raise ValueError("Unable to convert value to datetime.")

    months_with_31 = ['01', '03', '05', '07', '08', '10', '12']
    months_with_30 = ['02', '04', '06', '09', '11']
    if int(date[3:5]) in months_with_31:
        if int(date[0:2]) > 31:
            raise ValueError("Unable to convert value to datetime.")
    elif date[3:5] in months_with_30:
        if int(date[3:5]) == 2 and int(date[0:2]) > 28:
            raise ValueError("Unable to convert value to datetime.")
        elif int(date[0:2]) > 30:
            raise ValueError("Unable to convert value to datetime.")
    new_date = datetime.strptime(date, '%d.%m.%Y')

    return new_date


def get_days_between(first: datetime, last: datetime) -> int:
    """Finds the number of days between two days."""
    if not isinstance(first, datetime) or not isinstance(first, datetime):
        raise TypeError("Datetimes required.")
    if first is None or last is None:
        raise TypeError("Datetimes required.")
    if first is None or last is None:
        raise TypeError("Datetimes required.")
    delta = last - first

    return delta.days


def get_day_of_week_on(date: datetime) -> str:
    """Finds the weekday of a day"""

    if not isinstance(date, datetime):
        raise TypeError("Datetime required.")
    days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                    'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days_of_week[date.weekday]
