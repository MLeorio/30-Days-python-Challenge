# Day 4 : String Manipulation

# Exercice


# 1. Concaténez les chaînes « Trente », « Jours », « De », « Python » en une seule chaîne : « Trente Jours de Python ».
chaine1 = "Trente"
chaine2 = "Jours"
chaine3 = "De"
chaine4 = "Python"
chaine_concatenee = f"{chaine1} {chaine2} {chaine3} {chaine4}"
print(chaine_concatenee)

# 2. Concaténez la chaîne « Codage », « Pour », « Tous » en une seule chaîne, « Codage pour tous ».
chaine5 = "Codage"
chaine6 = "Pour"
chaine7 = "Tous"
chaine_concatenee2 = f"{chaine5} {chaine6} {chaine7}"
print(chaine_concatenee2)

# 3. Déclarez une variable nommée entreprise et attribuez-lui la valeur initiale « Codage pour tous ».
entreprise = "Codage pour tous"

# 4. Imprimez la variable company en utilisant print().
print(entreprise)

# 5. Imprimez la longueur de la chaîne de l'entreprise à l'aide de la méthode len() et print().
print(len(entreprise))

# 6. Changez tous les caractères en majuscules à l'aide de la méthode upper().
entreprise_majuscule = entreprise.upper()
print(entreprise_majuscule)

# 7. Changez tous les caractères en lettres minuscules en utilisant la méthode lower().
entreprise_minuscule = entreprise.lower()
print(entreprise_minuscule)

# 8. Utilisez les méthodes capitalize(), title(), swapcase() pour formater la valeur de la chaîne Coding For All.
chaine_formattee = "Coding For All"
chaine_capitalisee = chaine_formattee.capitalize()
chaine_titree = chaine_formattee.title()
chaine_swapcase = chaine_formattee.swapcase()
print(chaine_capitalisee)
print(chaine_titree)
print(chaine_swapcase)

# 9. Découpez le premier mot de la chaîne Coding For All.
premier_mot = chaine_formattee.split()[0]
print(premier_mot)

# 10. Vérifiez si la chaîne « Coding For All » contient un mot « Coding » à l'aide de la méthode index, find ou d'autres méthodes.
mot_a_trouver = "Coding"
chaine = "Coding For All"
print(chaine.index(mot_a_trouver))

# 11. Remplacez le mot codage dans la chaîne « Coding For All » par Python.
chaine_remplacee = chaine.replace("Coding", "Python")
print(chaine_remplacee)

# 12. Changez "Python for Everyone" en "Python for All" en utilisant la méthode replace ou d’autres méthodes.
chaine_initiale = "Python for Everyone"
chaine_modifiee = chaine_initiale.replace("Everyone", "All")
print(chaine_modifiee)

# 13. Divisez la chaîne « Coding For All » en utilisant l'espace comme séparateur (split()).
chaine_divisee = chaine.split()
print(chaine_divisee)

# 14. « Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon » : divisez la chaîne à la virgule.
chaine_entreprises = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
chaine_entreprises_divisee = chaine_entreprises.split(", ")
print(chaine_entreprises_divisee)

# 15. Quel est le caractère à l'index 0 dans la chaîne "Coding For All".
caractere_index_0 = chaine_formattee[0]
print(caractere_index_0)

# 16. Quel est le dernier index de la chaîne "Coding For All".
dernier_index = len(chaine_formattee) - 1
print(dernier_index)

# 17. Quel caractère se trouve à l'index 10 dans la chaîne « Coding For All ».
caractere_index_10 = chaine_formattee[10]
print(caractere_index_10)

# 18. Créez un acronyme ou une abréviation pour le nom « Python pour tous ».
mots = chaine.split()
print(''.join(mot[0].upper() for mot in mots))

# 19. Créez un acronyme ou une abréviation pour le nom « Coding For All ».

# 20. Utilisez l'index pour déterminer la position de la première occurrence de C dans Coding For All.
position_C = chaine_formattee.index('C')
print(position_C)

# 21. Utiliser l'index pour déterminer la position de la première occurrence de F dans Coding For All.
position_F = chaine_formattee.index('F')

# 22. Utilisez rfind pour déterminer la position de la dernière occurrence de l dans Coding For All People.
position_derniere_l = chaine_formattee.rfind('l')
print(position_derniere_l)

# 23. Utilisez index ou find pour trouver la première occurrence du mot « because » dans la phrase suivante : « You cannot end a sentence with because because because is a conjunction. »
phrase = "You cannot end a sentence with because because because is a conjunction."
position_because = phrase.index('because')
print(position_because)

# 24. Utilisez rindex pour trouver la dernière occurrence du mot because dans la phrase suivante : « You cannot end a sentence with because because because is a conjunction. »
position_derniere_because = phrase.rindex('because')
print(position_derniere_because)

# 25. Supprimez l'expression « because because because » dans la phrase suivante : « You cannot end a sentence with because because because is a conjunction. »
phrase_sans_because = phrase.replace('because because because', '')
print(phrase_sans_because)

# 26. Trouvez la position de la première occurrence du mot « because » dans la phrase suivante : « You cannot end a sentence with because because because is a conjunction. »
position_premiere_because = phrase.find('because')
print(position_premiere_because)

# 27. Supprimez l'expression « because because because » dans la phrase suivante : « On ne peut pas terminer une phrase par « You cannot end a sentence with because because because is a conjunction. »
phrase_sans_because2 = phrase.replace('because because because', '')
print(phrase_sans_because2)

# 28. Est-ce que « Coding For All » commence par une sous-chaîne Coding ?
commence_par_coding = chaine_formattee.startswith("Coding")
print(commence_par_coding) 

# 29. Est-ce que « Coding For All » se termine par une sous-chaîne Coding ?
se_termine_par_coding = chaine_formattee.endswith("Coding")
print(se_termine_par_coding)

#  30. « Codage pour tous », supprimez les espaces de fin gauche et droite dans la chaîne donnée.
chaine_espaces = " Codage pour tous "
chaine_sans_espaces = chaine_espaces.strip()
print(chaine_sans_espaces)

# 31. Laquelle des variables suivantes renvoie True lorsque nous utilisons la méthode isidentifier() :
    # 30DaysOfPython 
    # thirty_days_of_python
variable1 = "30DaysOfPython"
variable2 = "thirty_days_of_python"
print(variable1.isidentifier())  # False, starts with a digit
print(variable2.isidentifier())  # True, valid identifier

# 32. La liste suivante contient les noms de certaines bibliothèques Python : ['Django','Flask', 'Bottle', 'Pyramid', 'Falcon']. Joignez la liste avec un hachage contenant une chaîne d'espaces.

bibliotheques = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
bibliotheques_chaine = ' '.join(bibliotheques)
print(bibliotheques_chaine)

# 33. Utilisez la séquence d’échappement de nouvelle ligne pour séparer les phrases suivantes: I am enjoying this challenge. I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City 
# Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. Utilisez la méthode de formatage de chaîne pour afficher les éléments suivants :
# radius = 10 
# area = 3.14 * radius ** 2 
# The area of a circle with radius 10 is 314 meters square. 
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")


# 36. Effectuez les opérations suivantes à l’aide des méthodes de formatage de chaîne :
# 8 + 6 = 14 
# 8 - 6 = 2 
# 8 * 6 = 48 
# 8 / 6 = 1.33 
# 8 % 6 = 2 
# 8 // 6 = 1 
# 8 ** 6 = 262144
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6:.2f}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")