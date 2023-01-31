


user_prompt = True

while user_prompt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117 and int(age) > 1:
         user_prompt = False
    else:
         print("Please provide your answer in digits, with age 1 and about and below 117")




if int(age.isdigit()) and int(age) <= int("11") and int(age) > int("1"):
    print("You can watch U rated movies and PG")
elif int(age.isdigit()) == int("12") or int(age) < int("18") and int(age) > int("1"):
    print("You can watch U, PG and 12 rated movies")
elif int(age.isdigit()) >= int("18") and int(age) > int("1"):
    print("You can watch all movies since you are 18 or over")
else:
    print("Please provide your answer in digits, with age 1 and about and below 117")





