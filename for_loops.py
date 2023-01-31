# looping

# A for loop is where you define an iterator number and cycle through data (list or dictionary) 'for each' entry in that data structure

# Creating a for loop

# list_data = [1, 2, 3, 4, 5]
# embedded_lists = [[1, 2, 3] , [4, 5, 6]]

# a dictionary with 3 small dictionaries inside
# dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for each instance in list_data do this thing eg. print
# #num (or anything written in place of num) means for every item in the list

# for num in list_data:
#     print(num * 2)

# to print out both lists inside embedded_lists
# for data in embedded_lists:
#     print(data)

# nested for loops, (make sure you indent again for second forloop inside)
# to show each lists and then all individual data in each the lists
# for data in embedded_lists:
#     print(data)
#     for num in data:
#         print(num)

# loops for dictionaries

# to get all values back from the dictionary

# for item in dict_data.values():
#      print(item)

## this is a better looking way to return all values from the dictionary#

# for item in dict_data.values():
#    for embed_value in item.values():
#        print(embed_value) # print statements needs to be embedded

## this returns values in the smaller dictionary inside the dictionary

# for item in dict_data.values():
#     print(item)
#     for embed_value in item.values():
#          print(embed_value) # print statements needs to be embedded

# to get a particular value from a key

# for items in dict_data.values():
#     print(items['money'])

# please see Python documentation for more you can do with dictionaries and loops

# Loops and if statements

# list_1 = [1, 2, 3, 4, 5]
#
# for num in list_1:
#     if num == 3:
#         print("I found three!")
#     elif num > 3:
#         print("Gone too far!")
#     else:
#         print("Too soon")