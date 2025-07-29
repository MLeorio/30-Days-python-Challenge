# Day 7 : les Sets

"""
Un ensemble est une collection d'éléments. Revenons à votre cours de mathématiques de primaire ou de lycée. La définition mathématique d'un ensemble s'applique également en Python. Un ensemble est une collection d'éléments distincts, non ordonnés et non indexés. En Python, un ensemble permet de stocker des éléments uniques et permet de trouver l'union, l'intersection, la différence, la différence symétrique, le sous-ensemble, le sur-ensemble et l'ensemble disjoint parmi les ensembles.
"""

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercice 1: Level 1

# 1. Trouver la longueur de l'ensemble it_companies
length_it_companies = len(it_companies)

# 2. Ajoutez « Twitter » à it_companies
it_companies.add('Twitter')

# 3. Insérer plusieurs sociétés informatiques à la fois dans l'ensemble it_companies
it_companies.update(['Snapchat', 'LinkedIn', 'Reddit'])

# 4. Supprimer une des sociétés de l'ensemble it_companies
it_companies.remove('Oracle')

# 5. Quelle est la différence entre supprimer et jeter
#    - `remove()` lève une erreur si l'élément n'existe pas, tandis que `discard()` ne le fait pas.
#    - `remove()` est utilisé pour supprimer un élément spécifique, tandis que `discard()` supprime un élément sans lever d'erreur s'il n'existe pas.

# Exercice 2: Level 2

# 1. Rejoignez A et B
C = A.union(B)

# 2. Trouver l'intersection A B
intersection_AB = A.intersection(B)

# 3. A est un sous-ensemble de B ?
is_A_subset_B = A.issubset(B)

# 4. Les ensembles A et B sont-ils disjoints ?
is_disjoint = A.isdisjoint(B)

# 5. Reliez A avec B et B avec A
A_B_union = A.union(B)
B_A_union = B.union(A)

# 6. Quelle est la différence symétrique entre A et B
symmetric_difference_AB = A.symmetric_difference(B)

# 7. Supprimer complètement les ensembles
A.clear()
B.clear()

# Exercice 3: Level 3

# 1. Convertissez les âges en un ensemble et comparez la longueur de la liste et de l'ensemble. Lequel est le plus grand ?
unique_ages = set(age)
length_age_list = len(age)
length_unique_ages = len(unique_ages)
# Le plus grand est l'ensemble, car il ne contient que des éléments uniques.

# 2. Expliquez la différence entre les types de données suivants : chaîne, liste, tuple et ensemble.
# - Chaîne : Une séquence de caractères, immuable.
# - Liste : Une collection ordonnée et modifiable d'éléments, pouvant contenir
#   des éléments dupliqués.
# - Tuple : Une collection ordonnée et immuable d'éléments, pouvant contenir
#   des éléments dupliqués.
# - Ensemble : Une collection non ordonnée d'éléments uniques, non indexée et
#   modifiable. Il ne permet pas les éléments dupliqués.

# 3. "I am a teacher and I love to inspire and teach people". Combien de mots uniques ont été utilisés dans la phrase ? Utilisez les méthodes de division et de définition pour obtenir les mots uniques.
sentence = "I am a teacher and I love to inspire and teach people"
unique_words = set(sentence.lower().split())
unique_word_count = len(unique_words)

