


hours = input("How many hours have you worked this week? ")
rate = input("How much do you get paid by the hour? ")
over = input("How many hours of over time? ")
pay = 40 * int(rate)
overtime = int(rate) * 1.5 * int(over) + pay
underpay = int(rate) * int(hours)
if hours == "40":
    print(f"You have worked {hours} hours and you will be paid {pay}")
elif hours > "40":
    print(f"you have worked {hours} hours and you will be paid {overtime}")
elif hours < "40":
    print(f"You have worked {hours} hours you will be paid {underpay}")
