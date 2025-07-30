# Day 8 : Les dictionnaires

# Exercice 

# 1. Creer un dictionnaire vide nomme chien
chien = {}
# print(chien)

# 2. Ajouter le nom, couleur, race, jambe et age
chien['nom'] = "Petich"
chien['couleur'] = "Jaune"
chien['race'] = "Africain"
chien['jambe'] = "Moyen"
chien['age'] = 4

# print(chien)

# 3. Creer un dictionnaire etudiant et ajoutez d'abord le nom, le prenom, sexe, age, etat matrimonial, competences, pays, ville, adresse comme cles pour le dictionnaire
etudiant = {
    'nom' : "Dupont",
    'prenom' : "Lucas",
    'sexe' : "Masculin",
    'age' : 22,
    'etat_matrimonial' : "Celibataire",
    'competences' : ["Physics", "Chimie", "Maths"],
    'pays' : "Philippines",
    'ville' : "Manilles",
    'adresse': "123 Av. Stars"
}

# print(etudiant)

# 4. Obtenez la taille du dictionnaire etudiant
taille_etudiant = len(etudiant)

# print(taille_etudiant)

# 5. Obtenez la valeur des competences et verifier le type de donnees qu'il s'agit. Il devrait s'agir d'une liste

competences = etudiant['competences']
# print(competences)
# print(type(competences))

# 6. Modifier les valeurs des competences en ajoutant deux ou trois competences
# etudiant['competences'].append("Histoire")
# etudiant['competences'].append("Geographie")

# print(etudiant)

# 7. Obtenez les cles du dictionnaire comme une liste
liste_cles = etudiant.keys()
# print(liste_cles)

# 8. Obtenez les valeurs du dictionnaire comme une liste
liste_valeurs = etudiant.values()
# print(liste_valeurs)

# 9. Changer le dictionnaire en une liste de tuples en utlisant la methode items()
list_dict = etudiant.items()
# print(list_dict)

# 10. Supprimer l'un des elements du dict
etudiant.pop('etat_matrimonial')
# print(etudiant)

# 11. Supprimer un des dictionnaires
print(chien)
del chien
print(chien)