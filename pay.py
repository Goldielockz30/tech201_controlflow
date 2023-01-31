

hours = input("How many hours have you worked this week?")
payrate = input("How much do you get paid by the hour")

pay = int(hours) * int(payrate)
over = int(payrate) * 1.5

if hours == "40":
    print(f"You have worked {hours} hours and you will be paid {pay}")
elif hours > "40":
    print(f"you have worked {hours} hours and you will be paid {pay + over}")
elif hours < "40":
    print(f"You have worked {hours} hours you will be paid {pay}")

# if film_rating.lower() == "universal":
#     print("All age groups can watch this film")
# elif film_rating.lower() == "pg":
#     print("General viewing but parental guidance advised")
# elif film_rating.lower() == "12" or film_rating == "12a":
#     print("12 rated movies may not be suitable for those under 12, but supervision is recommended")
# elif film_rating.lower() == "15":
#     print("You must be 18 to watch 15 rated movies in the cinema")
# elif film_rating.lower() == "18":
#     print("You must be 18 to watch 18 rated movies in the cinema")
# else:
#     print("This is not a correct rating, pleasu use universal, pg, 12, 15, 18")
