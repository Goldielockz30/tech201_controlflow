

def pay_program(hours, pay):

        return hours, pay

hours = input("How many hours have you worked this week? ")
pay = input("How much do you get paid by the hour? ")

paycheck = pay_program(int(hours), int(pay))
total = int(hours) * int(pay)
print(f"Total gross pay: {total} ")
