


# age = input("What is your age?")
# if age.isdigit() and int(age) < 117:
#     print(f"You are {age} years old ")
#
# else:
#     print("Please provide your answer in digits and below 117")

film_rating = input("What is your age?")

if film_rating.isdigit() and int(film_rating) < 117:
    print(f"You are {film_rating} years old ")

else:
    print("Please provide your answer in digits and below 117")

if film_rating.lower() == "universal":
     print("All age groups can watch this film")
elif film_rating.lower() == "pg":
    print("General viewing but parental guidance advised")
elif film_rating.lower() == "12" or film_rating == "12a":
   print("12 rated movies may not be suitable for those under 12, but supervision is recommended")
elif film_rating.lower() == "15":
   print("You must be 18 to watch 15 rated movies in the cinema")
elif film_rating.lower() >= "18":
   print("You can watch this movie since you are 18 or over")
