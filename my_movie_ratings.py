
age = input("What is your age?")

if int(age.isdigit()) and int(age) > int("117") and int(age) != int("0"):
    print("Please provide your answer in digits, with age 1 and above and below 117")
elif int(age.isdigit()) and int(age) <= int("11") and int(age) != int("0"):
    print("You can watch U rated movies and PG")
elif int(age.isdigit()) and int(age) == int("12") and int(age) < int("18"):
    print("You can watch U, PG and 12 rated movies")
elif int(age.isdigit()) and int(age) >= int("18") and int(age) > int("1"):
    print("You can watch all movies since you are 18 or over")
else:
    print("Please provide your answer in digits, with age 1 and above and below 117")




