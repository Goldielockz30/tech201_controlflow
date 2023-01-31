


age = input("What is your age?")
if age.isdigit() and int(age) < 117:
   print(f"You are {age} years old ")

else:
   print("Please provide your answer in digits and below 117")

age = input("What is your age?")

if age <= "11":
    print("You can watch U rated movies and PG")
elif int(age) == int("12") or int(age) < int("18"):
    print("You can watch U, PG and 12 rated movies")
elif int(age) >= int("18"):
    print("You can watch all movies since you are 18 or over")


# elif age == "15":
#    print("You must be 18 to watch 15 rated movies in the cinema")
# elif age >= "18":
#    print("You can watch this movie since you are 18 or over")


