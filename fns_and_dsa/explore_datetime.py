"""
This module demonstrates how to use the datetime module to display
the current date and time in Python.

Author: Emmanuel
Date: 2025-01-10
"""
from datetime import datetime, timedelta
def display_current_datetime(): 
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Current date and time: {formatted}')
def calculate_future_date():
    current_time = datetime.now()
    current_time.strftime("%Y-%m-%d")
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = current_time + timedelta(days=number_of_days)
    print(f'Future date: {future_date.strftime("%Y-%m-%d")}')
display_current_datetime()
calculate_future_date()
