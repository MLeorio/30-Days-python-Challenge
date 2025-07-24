# Day 1 - Hello World Exercise

# Exercice 1
# Exucter dans la console Python


# Exercice 2
"""
1. Vérifiez la version Python que vous utilisez
"""
import sys
print("Version de Python :", sys.version)
# Dans un terminal, vous pouvez aussi utiliser la commande `python --version` ou `python3 --version`.

"""
2. Ouvrez le shell interactif Python et effectuez les opérations suivantes. Les opérandes s
ont 3 et 4.
o Addition (+) o Soustraction
(-) o Multiplication (*) o Mod
ule (%) o Division (/) o Expon
entielle (**) O Floor Division
Operator (//)
"""
print(3+4)  # Addition
print(3-4)  # Soustraction
print(3*4)  # Multiplication
print(3%4)  # Modulo
print(3/4)  # Division
print(3**4)  # Exponentielle
print(3//4)  # Floor Division

"""
Écrivez des chaînes sur la coque interactive Python. Les cordes sont les suivantes:
O votre nom o votre nom de famille
o votre pays o je profite de 30 jours
de python
"""
print("Votre nom")
print("Votre nom de famille")
print("Votre pays")
print("Je profite de 30 jours de Python")


# Exercice 3
"""
1. Écrivez un exemple pour différents types de données Python tels que le nombre
(entier, float, complexe), String, Boolean, List, Tuple, Set et Dictionary.
"""
# Exemple de différents types de données Python
exemple_entier = 10
exemple_float = 10.5
exemple_complexe = 1 + 2j
exemple_string = "Bonjour, Python!"
exemple_boolean = True
exemple_liste = [1, 2, 3, "Python", True]
exemple_tuple = (1, 2, 3, "Python", True)
exemple_set = {1, 2, 3, "Python", True}
exemple_dict = {"nom": "Python", "version": 3.10, "actif": True}

# Affichage des exemples
print("Exemple entier:", exemple_entier)
print("Exemple float:", exemple_float)
print("Exemple complexe:", exemple_complexe)
print("Exemple string:", exemple_string)
print("Exemple boolean:", exemple_boolean)
print("Exemple liste:", exemple_liste)
print("Exemple tuple:", exemple_tuple)
print("Exemple set:", exemple_set)
print("Exemple dict:", exemple_dict)


"""
2. Trouvez une distance euclidienne entre (2, 3) et (10, 8)
"""
import math
distance_euclidienne = math.sqrt((10 - 2) ** 2 + (8 - 3) ** 2)
print("Distance euclidienne entre (2, 3) et (10, 8) :", distance_euclidienne)

