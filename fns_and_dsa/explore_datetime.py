from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # حفظ التاريخ والوقت الحالي
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # هنرجعه نستخدمه بعدين

def calculate_future_date(current_date):
    try:
        days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    future_date = current_date + timedelta(days=days)  # حساب التاريخ المستقبلي
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")


# تشغيل البرنامج
current = display_current_datetime()
calculate_future_date(current)
