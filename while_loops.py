# While loops

# While loops monitor data rather than iterate


# what is the value of x
# how does compare to this value
# we only do get something if this comparison is true

x = 0

# while x <  10:
#     print(f"it's working -> {x}")
#     x += 1 # incrementer

# Using break

# while x < 10:
#     print(f"it's working -> {x}")
#     if x == 4:
#         break # this stops the while loop
#     x += 1
#
# print(x) # x = 4

# verify user input
# This can either be an int (20) or string (twenty)
# age = input("What is your age?")
#
# print(f"Your age is {age}")

# with a while loop we can

user_promt = True

while user_promt:
     age = input("What is your age?")
if age.isdigit() and int(age) < 117:
         user_promt = False
else:
         print("Please provide your answer in digits and below 117") # print(f"Your age is {age}")

