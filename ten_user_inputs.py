# While loop
# declare two variables
# the amout of inputs the user has made
# the number they give you
# set them to 0
# amount = 0
# number = 0
# as long as the program is running
# while True:
#
#     number += int(input("Number: ")) # get user input, turn it into an int and adding it
#     amount += 1  # increment it so now I'ts going to be one
#     if amount == 10:
#         break
# print(f"Numbers in total: {amount}")
# print(f"Sum of numbers: {number}")
# print(number)


# For loop
# range is an in built function that you can use to make a list based on the number that you put in ()
total = 0
for i in range(3):
    total += int(input("Enter a number: "))
print(f"The total of your inputs is: {total}")