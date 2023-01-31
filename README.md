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
