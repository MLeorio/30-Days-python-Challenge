# Day 6 : Les tuples

"""
Un tuple est un ensemble de différents types de données, ordonné et immuable. Les tuples sont écrits entre parenthèses (). Une fois créé, il est impossible d'en modifier les valeurs. Les méthodes add, insert et remove ne sont pas utilisables dans un tuple, car il n'est pas modifiable. Contrairement à une liste, un tuple possède peu de méthodes. Méthodes
liées aux tuples :
    - tuple() : pour créer un tuple vide
    - count() : pour compter le nombre d'éléments spécifiés dans un tuple
    - index() : pour trouver l'index d'un élément spécifié dans un tuple
    - operator : pour joindre deux tuples ou plus et en créer un nouveau
"""

# Exercice 1

# 1. Créer un tuple vide
mon_tuple_vide = ()

# 2. Créez un tuple contenant les noms de vos sœurs et de vos frères (les frères et sœurs imaginaires sont autorisés).
mes_freres_et_sœurs = ("Alice", "Bob", "Charlie")

# 3. Joignez les tuples frères et sœurs et attribuez-les aux frères et sœurs
mes_freres_et_sœurs = mes_freres_et_sœurs + ("David", "Eva")

# 4. Combien de frères et sœurs avez-vous ?
nombre_de_freres_et_sœurs = len(mes_freres_et_sœurs)

# 5. Modifiez le tuple des frères et sœurs, ajoutez le nom de votre père et de votre mère et attribuez-le à family_members.
family_members = mes_freres_et_sœurs + ("Father", "Mother")

# Exercice 2

# 1. Décomposer les frères et sœurs et les parents de family_members
freres_et_sœurs, parents = family_members[:-2], family_members[-2:]

# 2. Créez des tuples de fruits, légumes et produits animaux. Reliez les trois tuples et assignez-les à une variable appelée food_stuff_tp.
fruits = ("apple", "banana", "cherry")
légumes = ("carrot", "broccoli", "spinach")
produits_animaux = ("milk", "cheese", "eggs")
food_stuff_tp = fruits + légumes + produits_animaux

# 3. Changer le tuple about food_stuff_tp en une liste food_stuff_lt
food_stuff_lt = list(food_stuff_tp)

# 4. Découpez l'élément ou les éléments du milieu du tuple food_stuff_tp ou de la liste food_stuff_lt.
milieu_index = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
    milieu_elements = food_stuff_tp[milieu_index - 1:milieu_index + 1]
else:
    milieu_elements = food_stuff_tp[milieu_index:milieu_index + 1]

# 5. Découpez les trois premiers éléments et les trois derniers éléments de la liste food_staff_lt
premiers_elements = food_stuff_lt[:3]
derniers_elements = food_stuff_lt[-3:]

# 6. Supprimer complètement le tuple food_staff_tp
del food_stuff_tp

# 7. Vérifier si un élément existe dans le tuple :
#   Vérifiez si « Estonie » est un pays nordique
#   Vérifiez si « Islande » est un pays nordique
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway',
'Sweden')
is_estonia_nordic = 'Estonia' in nordic_countries
is_iceland_nordic = 'Iceland' in nordic_countries