'''
lab 5 if statement
'''

#3.1
alien_color = "red"
if alien_color == "green":
    print("you just earned 5 points")
    
#3.2
alien_color = "red"

if alien_color == "green":
    print("you just earned 5 points")
    
else:
    print("you just earned 10 points")
    
#3.3
favorite_fruits = ["grapes", "banana", "orange"]

if 'orange' in favorite_fruits:
    print('you really like orange')
    
if 'grapes' in favorite_fruits:
    print('you really like grapes')
    
if 'mango' in favorite_fruits:
    print('you really like mango')
    
#3.4

age = 67

if age >=20:
    print('you are an adult')
    if age >=65:
        print('you are an elder')
elif age >12:
    print('you are a teenager')
else:
    print('you are a kid')
