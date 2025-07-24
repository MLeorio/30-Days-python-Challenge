# Day 2 : Variables et fonctions


# Exercice 1
"""
1. À l'intérieur de 30 jours, créez un dossier appelé day_2. À l'intérieur de ce dossier, créez un fichier nommé variables.py
2. Écrivez un commentaire Python disant «Jour 2: 30 Days of Python Programming»
3. Déclarez une variable de prénom et attribuez-lui une valeur
4. Déclarez une variable de nom de famille et attribuez-lui une valeur
5. Déclarez une variable de nom complet et attribuez une valeur à lui
6. Declare une variable de pays et y attribuez une valeur à une valeur
7. Déclarer une variable municipale et attribuer une valeur
8. Déclarez une variable d'âge et attribuez-lui une valeur
9. Déclarez une variable an et lui attribuez une valeur
10. Déclarez une variable est_Married et attribuez-lui une valeur
11. Déclarez une variable is_true et attribuez-lui une valeur
12. Déclarez une variable IS_light_on et y attribuez une valeur
13. Déclarer la variable multiple sur une seule ligne
"""

# 1. Créer un dossier day_2 et un fichier variables.py

# 2. Écrire un commentaire Python
# Day 2: 30 Days of Python Programming

# 3. Declare a first name variable and assign a value to it
first_name = "Leorio"

# 4. Declare a last name variable and assign a value to it 
last_name = "KAKASHI"

# 5. Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
# full_name = "Leorio KAKASHI"

# 6. Declare a country variable and assign a value to it
country = "Japan"

# 7. Declare a city variable and assign a value to it
city = "Tokyo"

# 8. Declare an age variable and assign a value to it 
age = 25

# 9. Declare a year variable and assign a value to it
year = 2023

# 10. Declare a is_married variable and assign a value to it
is_married = False

# 11. Declare a is_true variable and assign a value to it
is_true = True

# 12. Declare a is_light_on variable and assign a value to it
is_light_on = True

# 13. Declare multiple variables on a single line
x, y, z = 5, 10.5, True


# Exercice 2
"""
1. Vérifiez le type de données de toutes vos variables à l'aide de la fonction intégrée type()
2. En utilisant la fonction intégrée len(), trouvez la longueur de votre prénom
3. Comparez la longueur de votre prénom et de votre nom de famille
4. Déclarez 5 comme num_one et 4 comme num_two
5. Ajoutez num_one et num_two et attribuez la valeur à une variable total 
6. Soustrayez num_two de num_one et attribuez la valeur à une variable diff
7. Multipliez num_two et num_one et attribuez la valeur à une variable produit 
8. Divisez num_one par num_two et attribuez la valeur à une division variable
9. Utiliser la division modulo pour calculer num_two divisé par num_one et attribuer la valeur à une variable reste.
10. Calculez num_one à la puissance num_two et attribuez la valeur à une variable exp
11. Calculer la division entiere de num_un par num_deux et attribuer la valeur à une variable floor_division
12. Le rayon d'un cercle est de 30 mètres.
    I. Calculer l'aire d'un cercle et attribuer la valeur à une variable nommée area_of_circle
    II. Calculer la circonférence d'un cercle et attribuer la valeur à une variable nommée circum_of_circle
    III. Prenez le rayon comme entrée utilisateur et calculez la surface.
13. Utilisez la fonction de saisie intégrée pour obtenir le prénom, le nom, le pays et l'âge d'un utilisateur et enregistrez les 
    valeurs dans les noms de variables correspondants.
14. Exécutez help('keywords') dans l'interpréteur de commandes Python ou dans votre fichier pour vérifier les mots ou mots-clés
    réservés Python.
 """
 
 
# 1. Vérifiez le type de données de toutes vos variables
print(type(first_name))     # str
print(type(last_name))      # str
print(type(full_name))      # str
print(type(country))        # str
print(type(city))           # str
print(type(age))            # int
print(type(year))           # int
print(type(is_married))     # bool
print(type(is_true))        # bool
print(type(is_light_on))    # bool
print(type(x))              # int
print(type(y))              # float
print(type(z))              # bool


# 2. En utilisant la fonction intégrée len(), trouvez la longueur de votre prénom
print("Longueur du prénom :", len(first_name))  # Longueur du prénom : 6


# 3. Comparez la longueur de votre prénom et de votre nom de famille
print("Longueur du prénom est égale à la longueur du nom de famille :", len(first_name) == len(last_name))

# 4. Déclarez 5 comme num_one et 4 comme num_two
num_one = 5
num_two = 4


# 5. Ajoutez num_one et num_two et attribuez la valeur à une variable total
total = num_one + num_two               # total = 9

# 6. Soustrayez num_two de num_one et attribuez la valeur à une variable diff
diff = num_one - num_two                # diff = 1

# 7. Multipliez num_two et num_one et attribuez la valeur à une variable produit
produit = num_one * num_two             # produit = 20

# 8. Divisez num_one par num_two et attribuez la valeur à une variable division
division = num_one / num_two            # division = 1.25

# 9. Utiliser la division modulo pour calculer num_two divisé par num_one et attribuer la valeur à une variable reste
reste = num_two % num_one               # reste = 4 % 5 = 4

# 10. Calculez num_one à la puissance num_two et attribuez la valeur à une variable exp
exp = num_one ** num_two                # exp = 625

# 11. Calculer la division entière de num_one par num_two et attribuer la valeur à une variable floor_division
floor_division = num_one // num_two     # floor_division = 1

# 12. Le rayon d'un cercle est de 30 mètres.
# I. Calculer l'aire d'un cercle et attribuer la valeur à une variable nommée area_of_circle
import math
area_of_circle = math.pi * (30 ** 2)        # math.pi est la constante π = 3.141592653589793
print("L'aire du cercle de 30m de rayon est : ", area_of_circle)    # L'aire du cercle de 30m de rayon est :  2827.4333882308138

# II. Calculer la circonférence d'un cercle et attribuer la valeur à une variable nommée circum_of_circle
circum_of_circle = 2 * math.pi * 30
print("La circonférence du cercle de 30m de rayon est : ", circum_of_circle)  # La circonférence du cercle de 30m de rayon est :  188.49555921538757

# III. Prenez le rayon comme entrée utilisateur et calculez la surface
rayon = float(input("Entrez le rayon du cercle : "))
area_user_circle = math.pi * (rayon ** 2)
print(f"L'aire du cercle avec un rayon de {rayon} mètres est : {area_user_circle}")


# 13. Utilisez la fonction de saisie intégrée pour obtenir le prénom, le nom, le pays et l'âge d'un utilisateur
user_first_name = input("Entrez votre prénom : ")
user_last_name = input("Entrez votre nom de famille : ")
user_country = input("Entrez votre pays : ")
user_age = int(input("Entrez votre âge : "))

# Affichage des informations de l'utilisateur
print(f"Prénom : {user_first_name}, Nom de famille : {user_last_name}, Pays : {user_country}, Âge : {user_age}")

# 14. Exécutez help('keywords') dans l'interpréteur de commandes Python ou dans votre fichier pour vérifier les mots ou mots-clés réservés Python.