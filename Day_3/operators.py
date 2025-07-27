# Day 3: Operators...

# 1. Déclarez votre âge comme une variable entière
age = 25

# 2. Déclarez votre taille comme une variable flottante
height = 1.75

# 3. Déclarer une variable qui stocke un nombre complexe
complex_number = 3 + 4j

# 4. Écrivez un script qui invite l'utilisateur à saisir la base et la hauteur du triangle et à calculer l'aire de ce triangle (aire = 0,5 x b x h).
hauteur = float(input("Entrez la hauteur du triangle: "))
base = float(input("Entrez la base du triangle: "))
area_triangle = 0.5 * base * hauteur
print(f"L'aire du triangle avec une base de {base} et une hauteur de {hauteur} est : {area_triangle}")

# 5. Écrivez un script qui invite l'utilisateur à saisir les côtés a, b et c du triangle. Calculez le périmètre du triangle (périmètre = a + b + c).
a = float(input("Entrez le côté a du triangle: "))
b = float(input("Entrez le côté b du triangle: "))
c = float(input("Entrez le côté c du triangle: "))
perimeter_triangle = a + b + c
print(f"Le périmètre du triangle avec les côtés {a}, {b} et {c} est : {perimeter_triangle}")

# 6. Déterminez la longueur et la largeur d'un rectangle à l'aide de l'invite. Calculez son aire (aire = longueur x largeur) et son périmètre (périmètre = 2 x (longueur + largeur)).
longueur = float(input("Entrez la longueur du rectangle: "))
largeur = float(input("Entrez la largeur du rectangle: "))
area_rectangle = longueur * largeur
perimeter_rectangle = 2 * (longueur + largeur)
print(f"L'aire du rectangle avec une longueur de {longueur} et une largeur de {largeur} est : {area_rectangle}")

# 7. Déterminer le rayon d'un cercle à l'aide de l'invite. Calculer l'aire (aire = pi x r x r) et la circonférence (c = 2 x pi x r) où pi = 3,14.
import math
rayon = float(input("Entrez le rayon du cercle: "))
area_circle = math.pi * (rayon ** 2)
circumference_circle = 2 * math.pi * rayon
print(f"L'aire du cercle avec un rayon de {rayon} est : {area_circle}")
print(f"La circonférence du cercle avec un rayon de {rayon} est : {circumference_circle}")

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
# slope = 2
# x_intercept = 1  # When y = 0, x = 1
# y_intercept = -2  # When x = 0, y = -2
# print(f"La pente de l'équation y = 2x - 2 est : {slope}")
# print(f"L'ordonnée à l'origine (x-intercept) de l'équation y    = 2x - 2 est : {x_intercept}")
# print(f"L'ordonnée à l'origine (y-intercept) de l'équation y    

# 9. La pente est (m = y₂-y₄/x₂-x₄). Trouvez la pente et la distance euclidienne entre le point (2, 2) et le point (6, 10).

# 10. 

# 11. Calculez la valeur de y (y = x^2 + 6x + 9). Essayez d'utiliser différentes valeurs de x et déterminez à quelle valeur de x y sera égal à 0.
y = lambda x: x**2 + 6*x + 9
x_values = [-10, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in x_values:
    result = y(x)
    print(f"Pour x = {x}, y = {result}")
    if result == 0:
        print(f"y est égal à 0 lorsque x = {x}")

# 12. Trouvez la longueur de « python » et de « dragon » et faites une fausse comparaison.
print("Longueur de 'python' :", len("python"))  # Longueur de 'python' : 6
print("Longueur de 'dragon' :", len("dragon"))  # Longueur de 'dragon' : 6
print("La longueur de 'python' est égale à la longueur de 'dragon' :", len("python") == len("dragon"))  # La longueur de 'python' est égale à la longueur de 'dragon' : True

# 13. Utilisez l'opérateur and pour vérifier si « on » est trouvé à la fois dans « python » et « dragon »
print("« on » est trouvé dans 'python' et 'dragon' :", "on" in "python" and "on" in "dragon")  # True

# 14. "J'espère que ce cours ne contient pas de jargon". Utilisez l'opérateur in pour vérifier la présence de jargon dans la phrase.
print("« jargon » est dans la phrase :", "jargon" in "J'espère que ce cours ne contient pas de jargon")  # True

# 15. Il n'y a pas de « on » dans dragon et python
print("« on » n'est pas trouvé dans 'dragon' et 'python' :", "on" not in "dragon" and "on" not in "python")  # True

# 16. Calculez la longueur du texte Python, convertissez la valeur en nombre à virgule flottante et en chaîne.
text = "Python"
text_length = len(text) # 6
float_length = float(text_length) # 6.0
string_length = str(text_length) # '6'

# 17. Les nombres pairs sont divisibles par 2 et leur reste est nul. Comment vérifier si un nombre est pair ou non avec Python ?
number = int(input("Entrez un nombre pour vérifier s'il est pair : "))
is_even = number % 2 == 0

print(f"Le nombre {number} est pair : {is_even}")  # True si le nombre est pair, False sinon

# 18. Vérifiez si la division au sol de 7 par 3 est égale à la valeur convertie en entier de 2,7.
floor_division = 7 // 3
int_value = int(2.7)
is_equal = floor_division == int_value
print(f"La division au sol de 7 par 3 est égale à la valeur entière de 2,7 : {is_equal}")  # False

# 19.  Vérifiez si le type « '10' » est égal au type « 10 »
type_string = type('10')
type_integer = type(10)
is_type_equal = type_string == type_integer
print(f"Le type de '10' est égal au type de 10 : {is_type_equal}")  # False

# 20. Vérifiez si int('9.8') est égal à 10
try:
    int_value = int('9.8')
except ValueError:
    int_value = None
    
is_int_equal = int_value == 10
print(f"int('9.8') est égal à 10 : {is_int_equal}")  # False

# 21. Écrire un script invitant l'utilisateur à saisir ses heures et son tarif horaire. Calculer le salaire de la personne.
time = float(input("Entrez le nombre d'heures travaillées : "))
tarif_hourly = float(input("Entrez votre tarif horaire : "))
salary = time * tarif_hourly
print(f"Le salaire pour {time} heures à un tarif horaire de {tarif_hourly} est : {salary}")

# 22. Écrivez un script qui invite l'utilisateur à saisir le nombre d'années. Calculez le nombre de secondes qu'une personne peut vivre. Supposons qu'une personne puisse vivre cent ans.
years = int(input("Entrez le nombre d'années : "))
seconds_per_year = 365 * 24 * 60 * 60  # Nombre de secondes dans une année
total_seconds = years * seconds_per_year
print(f"Le nombre de secondes qu'une personne peut vivre en {years} années est : {total_seconds}") 

# 23.  Écrivez un script Python qui affiche le tableau suivant
# 1 1 1 1 1 
# 2 1 2 4 8 
# 3 1 3 9 27 
# 4 1 4 16 64 
# 5 1 5 25 125
for i in range(1, 6):
    print(i, end='  ')
    res = 1
    for j in range(1, 5):
        print(res, end='  ')
        res *= i
    print()