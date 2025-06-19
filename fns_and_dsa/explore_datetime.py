from datetime import datetime , timedelta
def display_current_datetime():
    current = datetime.now()
    current_date = current.strftime("%Y-%m-%d %H:%M:%S")
    return current_date

print(f"Current date and time: {display_current_datetime()}")
number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = datetime.now()
    future_date = timedelta(days=number_of_days) + current_date
    return future_date.strftime("%Y-%m-%d %H:%M:%S")

print(f"Future date: {calculate_future_date()}")
