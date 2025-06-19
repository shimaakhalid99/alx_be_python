from datetime import datetime , timedelta
def display_current_datetime():
    current_date = datetime.now()
    return current_date

print(f"Current date and time: {display_current_datetime()}")
number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = timedelta(days=number_of_days) + display_current_datetime()
    return future_date

print(f"Future date: {calculate_future_date()}")
