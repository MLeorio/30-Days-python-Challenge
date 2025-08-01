# Exercice 1: Loop

# 1. 
for x in range(11):
	print(x)

x = 0	
while x <= 10:
	print(x)
	x += 1

# 2. 

# 3. 
for x in range(8):
	print("#"*x)


# 4.
for x in range(8):
	for y in range(8):
		print("#", end=" ")
	print()

# 5.
for i in range(11):
	print(f"{i} * {i} = {i*i}")
	
# 6.
li = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in li:
	print(item)

# 7.
for x in range(101):
	if x % 2 == 0:
		print(x)

# 8.
for x in range(100):
	if x % 2 != 0:
		print(x)
		
		
		
# Exercice 2 :
# 1.
s = 0
for x in range(101):
	s += x
print("The sum of all numbers is : ",s)

# 2.
s_ev = 0
s_od = 0
for x in range(101):
	if x % 2 == 0:
		s_ev += x
	if x % 2 != 0:
		s_od += x

print("The sum of all even numbers ", s_ev)
print("The sum of all odd numbers ", s_od)

# Exercice 3:
from countries import countries
for country in countries:
	if "land" in country:
		print(country)

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)