# Day 5: Les listes

# Exercice 1:

# 1. Declarez une liste vide.
liste_vide = []

# 2. Déclarer une liste avec plus de 5 éléments
liste_avec_elements = [1, 2, 3, 4, 5, 6]


# 3. Trouvez la longueur de votre liste
longueur_liste = len(liste_avec_elements)


# 4. Obtenez le premier élément, l'élément du milieu et le dernier élément de la liste
premier_element = liste_avec_elements[0]
milieu_index = len(liste_avec_elements) // 2
milieu_element = liste_avec_elements[milieu_index]
dernier_element = liste_avec_elements[-1]


# 5. Déclarez une liste appelée mixed_data_types, saisissez votre (nom, âge, taille, état civil, adresse)
mixed_data_types = ["Eugene", 25, 1.75, "Célibataire", "123 Rue Exemple"]


# 6. Déclarez une variable de liste nommée it_companies et attribuez-lui des valeurs initiales Facebook, Google, Microsoft, Apple, IBM, Oracle et Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]


# 7. Affichez la liste it_companies
print(it_companies)

# 8. Affichez le nombre d'entreprises dans la liste it_companies
nombre_entreprises = len(it_companies)

# 9. Affichez le premier, le milieu et le dernier élément de la liste it_companies
premier_it_company = it_companies[0]
milieu_it_index = len(it_companies) // 2
milieu_it_company = it_companies[milieu_it_index]
dernier_it_company = it_companies[-1]

# 10.Imprimer la liste après avoir modifié l'une des sociétés
it_companies[0] = "Meta"
print(it_companies)

# 11.Ajoutez une entreprise informatique à it_companies
it_companies.append("Tesla")

# 12. Insérer une entreprise informatique au milieu de la liste des entreprises
milieu_it_index = len(it_companies) // 2
it_companies.insert(milieu_it_index, "Nvidia")

# 13. Changez l'un des noms de sociétés informatiques en majuscules (IBM exclu !)
it_companies = [company.upper() if company != "IBM" else company for company in it_companies]

# 14. Rejoignez les it_companies avec une chaîne '#; '
it_companies_joined = '#; '.join(it_companies)

# 15. Vérifiez si une certaine entreprise existe dans la liste it_companies.
entreprise_a_verifier = "Google"
existe = entreprise_a_verifier in it_companies

# 16. Trier la liste à l'aide de la méthode sort()
it_companies.sort()

# 17. Inverser la liste par ordre décroissant en utilisant la méthode reverse()
it_companies.reverse()

# 18. Découpez les 3 premières entreprises de la liste
premieres_entreprises = it_companies[:3]

# 19. Découpez les 3 dernières entreprises de la liste
dernieres_entreprises = it_companies[-3:]

# 20. Retirez la ou les entreprises informatiques intermédiaires de la liste
if len(it_companies) > 2:
    it_companies.pop(milieu_it_index)

# 21. Supprimer la première entreprise informatique de la liste
if it_companies:
    it_companies.pop(0)
    
# 22. Supprimez la ou les entreprises informatiques intermédiaires de la liste
if len(it_companies) > 2:
    it_companies.pop(len(it_companies) // 2)

# 23. Supprimer la dernière entreprise informatique de la liste
if it_companies:
    it_companies.pop(-1)

# 24. Supprimer toutes les entreprises informatiques de la liste
it_companies.clear()

# 25. Détruisez la liste des entreprises informatiques
del it_companies

# 26. Rejoignez les listes suivantes :
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

# 27. Après avoir joint les listes de la question 26, copiez la liste jointe et attribuez-la à une variable full_stack, puis insérez Python et SQL après Redux.
full_stack = front_end + back_end
full_stack.insert('Python')
full_stack.insert('SQL')
full_stack.insert('Redux')


# Exercice 2:
# 1. Voici une liste de 10 étudiants dont l'âge est :
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# a. Trier la liste et trouver l'âge minimum et maximum
ages.sort()
age_minimum = ages[0]
age_maximum = ages[-1]

# b. Ajoutez à nouveau l'âge minimum et l'âge maximum à la liste
ages.append(age_minimum)
ages.append(age_maximum)

# c. Trouvez l'âge médian (un élément du milieu ou deux éléments du milieu divisés par deux)
if len(ages) % 2 == 0:
    median_index1 = len(ages) // 2 - 1
    median_index2 = len(ages) // 2
    age_median = (ages[median_index1] + ages[median_index2]) / 2
else:
    median_index = len(ages) // 2
    age_median = ages[median_index]

# d. Trouvez l'âge moyen (somme de tous les éléments divisée par leur nombre)
age_moyen = sum(ages) / len(ages)

# e. Trouver la plage d'âges (max moins min)
age_plage = age_maximum - age_minimum

# f. Comparez la valeur de (min - moyenne) et (max - moyenne), utilisez la méthode abs()
min_moyenne = abs(age_minimum - age_moyen)
max_moyenne = abs(age_maximum - age_moyen)

# 2. Trouver le(s) pays intermédiaire(s) dans la liste des pays
from Day_5.countries import countries
if countries:
    milieu_index = len(countries) // 2
    if len(countries) % 2 == 0:
        pays_intermediaires = countries[milieu_index - 1: milieu_index + 1]
    else:
        pays_intermediaires = [countries[milieu_index]]

# 3. Divisez la liste des pays en deux listes égales si elle est égale ou s'il n'y a pas un pays de plus pour la première moitié.
if len(countries) % 2 == 0:
    pays_1 = countries[:len(countries) // 2]
    pays_2 = countries[len(countries) // 2:]
else:
    pays_1 = countries[:len(countries) // 2 + 1]
    pays_2 = countries[len(countries) // 2 + 1:]
    

# 4. [« Chine », « Russie », « États-Unis », « Finlande », « Suède », « Norvège », « Danemark »]. Décomposez les trois premiers pays et les autres en pays scandinaves.
scandinavian_countries = ['Chine', 'Russie', 'États-Unis', 'Finlande', 'Suède', 'Norvège', 'Danemark']
pays_scandinaves = scandinavian_countries[3:]

