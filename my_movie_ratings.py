


age = input("What is your age?")
if age.isdigit() and int(age) < 117:
    print(f"You are {age} years old ")

else:
    print("Please provide your answer in digits and below 117")

# film_rating = input()

if age.lower() == "universal":
     print("All age groups can watch this film")
elif age.lower() == "pg":
     print("General viewing but parental guidance advised")
elif age.lower() == "12" or age == "12a":
     print("12 rated movies may not be suitable for those under 12, but supervision is recommended")
elif age.lower() == "15":
     print("You must be 18 to watch 15 rated movies in the cinema")
elif age.lower() == "18":
     print("You must be 18 to watch 18 rated movies in the cinema")
else:
     print("This is not a correct rating, please use universal, pg, 12, 15, 18")