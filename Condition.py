# Day 9 : Conditionals

# Exercice : Level 1
# 1.
age = int(input("Enter your age : "))
if age >= 18:
     print("You are old enough to learn to drive")
 else:
     print(f"You need {18 - age} more years to learn to drive")
    
 # 2. 
 your_age = int(input("Enter your age : "))
 my_age = 25

if my_age > your_age:
     print(f"I'm {my_age - your_age} years older than you !")
 elif your_age > my_age:
     print(f"You are {your_age - my_age} years older than me !")
 else:
     print("We are the same age !")


 # 3. 
n1 = input("Enter number one : ")
n2 = input("Enter number two : ")
if n1 > n2:
	print(f"{n1} is greater than {n2}")
elif n2 > n1:
     print(f"{n2} is greater than {n1}")
else:
    print("they are same number !")



# Exercice : Level 2
# 1.
score = float(input("Enter your score : "))
if score >= 80 and score <= 100:
    print("Your have A grade ")
elif score >= 70 :
    print("Your have B grade ")
 elif score >= 60:
 	     print("Your have C grade ")
elif score >= 50:
    print("Your have D grade ")
elif score >= 0:
  print("Your have F grade ")
    
# 2.
month = input("Enter the month : ").capitalize()

if month in ["September", "October", "November"]:
	     print("Your are in Autumn")
elif month in ["December", "January", "February"]:
	     print("Your are in Winter")
 elif month in ["March", "April", "May"]:
    print("Your are in Spring")
elif month in ["June", "July", "August"]:
   print("Your are in Summer")
else:
     print("Invalid month")


# 3.
 fruits = ["Banana", "Orange", "Mango", "Lemon"]
 fruit = input("Enter a fruit : ").capitalize()
 if fruit in fruits:
   print("That fruit already exist in the list")
 else:
 	     fruits.append(fruit)
 	     print("The modified list of fruits is: ", fruits)


# Exercice : Level 3
# 1.
person = {
    'first_name' : "Dupont",
    'last_name' : "Lucas",
    'age' : 22,
    'is_married' : True,
    'skills' : ["JavaScript", "React", "Node", "MongoDB", "Python"],
    'country' : "Philippines",
    'address': {
            'street': "Space street",
            'zipcode': '02210'
        }
}

if 'skills' in person.keys():
    skills_len = len(person['skills'])
    print(person['skills'][skills_len // 2])
    if "Python" in person['skills']:
        print(f"{person['last_name']} {person['first_name']} has Python skill")
    
    if person['skills'] == ["JavaScript", "React"]:
        print("He is a front end developer !")
    elif person['skills'] == ["Node", "MongoDB", "Python"]:
        print("He is a back end developer !")
    elif person["skills"] == ["JavaScript", "React", "Node", "MongoDB", "Python"]:
        print("He is a fullstack end developer !")
    else:
        print("Unknown title")
else:
    print("No skill provided")

if person["country"] == "Philippines" and person["is_married"]:
    print(f"{person['last_name']} {person['first_name']} lives in {person['country']}. He is married. ")