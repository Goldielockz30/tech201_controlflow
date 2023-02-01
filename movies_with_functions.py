
def movie_program():
    age = int(input("How old are you? "))
    if int(age) > 0 and int(age) < 117:
        if int(age) >= 18:
            print("You are old enough to but a ticket for any movie")
        elif int(age) < 18 and int(age) >= 15:
            print("You can watch 15, 12, PG and universal rated movies")
        elif int(age) < 15 and int(age) >= 12:
            print("You can watch 15, 12, PG and universal rated movies")
        else:
            print("You can buy tickets for U and PG movies")
    else:
        print("Please enter a valid number for your age")
movie_program()
movie_program()

