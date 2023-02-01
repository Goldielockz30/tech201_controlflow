# tech201_controlflow
tech201_controlflow


# Control flow

### Control Flow -> Flow through a particular process

### If statement

```age = 15

if age >= 18:
     print("You are the correct age to watch this film and can buy a ticket")  

 if age < 18:  
     print("I'm affraid you cannot watch this movie you are not old enough")
```
### elif and else
```
film_rating = "18"  
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
    print("This is not a correct rating, please use universal, pg, 12, 15, 18")  
```
### In python there's no 'switch statements' or 'case statements'


# looping

### A for loop is where you define an iterator number and cycle through data (list or dictionary) 'for each' entry in that data structure

### Creating a for loop
```
list_data = [1, 2, 3, 4, 5]  
embedded_lists = [[1, 2, 3] , [4, 5, 6]]  

a dictionary with 3 small dictionaries inside  
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}  

for each instance in list_data do this thing eg. print  
#num (or anything written in place of num) means for every item in the list  

for num in list_data:
   print(num * 2)

to print out both lists inside embedded_lists
for data in embedded_lists:
    print(data)

nested for loops, (make sure you indent again for second forloop inside)
to show each lists and then all individual data in each the lists
for data in embedded_lists:
   print(data)
   for num in data:
       print(num)
```
# loops for dictionaries

### to get all values back from the dictionary
```
for item in dict_data.values():  
   print(item)  

this is a better looking way to return all values from the dictionary #  

for item in dict_data.values():
  for embed_value in item.values():
     print(embed_value) # print statements needs to be embedded

this returns values in the smaller dictionary inside the dictionary #

for item in dict_data.values():
   print(item)
    for embed_value in item.values():
        print(embed_value) # print statements needs to be embedded
```
### to get a particular value from a key
```
for items in dict_data.values():
    print(items['money'])
```
### please see Python documentation for more you can do with dictionaries and loops

### Loops and if statements
```
list_1 = [1, 2, 3, 4, 5]  

for num in list_1:  
     if num == 3:   
         print("I found three!")  
     elif num > 3:  
         print("Gone too far!")  
     else:  
         print("Too soon")  
```
### While loops

### While loops monitor data rather than iterate


what is the value of x
how does compare to this value
we only do get something if this comparison is true
```
x = 0

while x <  10:
    print(f"it's working -> {x}")
    x += 1 # incrementer
```
### Using break
```
while x < 10:
     print(f"it's working -> {x}")
     if x == 4:
         break # this stops the while loop
     x += 1

 print(x) # x = 4
```
### verify user input
This can either be an int (20) or string (twenty)  
```
age = input("What is your age?")

print(f"Your age is {age}")

#### with a while loop we can

user_promt = True

while user_promt:
     age = input("What is your age?")
if age.isdigit() and int(age) < 117:
         user_promt = False
else:
         print("Please provide your answer in digits and below 117") # print(f"Your age is {age}")
```
# While loops

### While loops monitor data rather than iterate


what is the value of x  
how does compare to this value  
we only do get something if this comparison is true  
```
x = 0

while x <  10:  
    print(f"it's working -> {x}") 
    x += 1 # incrementer  
```
# Using break
```
while x < 10:  
    print(f"it's working -> {x}")  
    if x == 4:  
       break # this stops the while loop  
    x += 1  
```
print(x) # x = 4

# verify user input
### This can either be an int (20) or string (twenty)
```
age = input("What is your age?")  

print(f"Your age is {age}")  

### with a while loop we can  

user_promt = True  

while user_promt:  
     age = input("What is your age?")  
if age.isdigit() and int(age) < 117:  
         user_promt = False  
else:
         print("Please provide your answer in digits and below 117") # print(f"Your age is {age}")  
```
