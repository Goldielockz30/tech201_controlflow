film_rating = "12"

user_promt = True
while user_promt:
    age = input("What is your age?")
    if age.isdigit() and int(age) < 117:
        user_promt = False
    else:
        print("Please provide your answer in digits and below 117")
print(f"Your age is {age}")


 if film_rating.lower() == "universal":
     print("All age groups can watch this film")
 elif film_rating.lower() == "pg":
     print("General viewing but parental guidance advised")
 elif film_rating.lower() == "12" or film_rating == "12a":
     print("12 rated movies may not be suitable for those under 12, but supervision is recommended")
 elif film_rating.lower() == "15":
     print("You must be 18 to watch 15 rated movies in the cinema")
 elif film_rating.lower() == "18":
     print("You must be 18 to watch 18 rated movies in the cinema")
 else:
     print("This is not a correct rating, pleasu use universal, pg, 12, 15, 18")