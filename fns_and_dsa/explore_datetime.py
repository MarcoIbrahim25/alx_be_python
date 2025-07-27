from datetime import datetime, timedelta
def  display_current_datetime() :
    
    now= datetime.datetime.now()
    date= now.strftime ("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", date)

def calculate_future_date():
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.date.today()
        future_date = current_date + datetime.timedelta(days=days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid number of days.")

    if __name__ == "__main__":
        display_current_datetime()