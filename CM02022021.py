# -*- coding: utf-8 -*

# Question 1: Déclarer une variable nommée villes qui contient le nom de 5 villes
# suivantes : Paris, Lille, Lyon, Toulouse, Grenoble

villes = "Paris, Lille, Lyon, Toulouse, Grenoble"

# Question 2: Calculer et afficher la taille de la chaine villes
print(len(villes))

# Question 3: Chercher et afficher la position de la sous-chaine Lille
print(villes.find("Lille"))

# Question 4: Tester si la chaine villes contient la sous-chaine Grenoble
print(villes.find("Grenoble"))

# Question 5: Tester si la chaines villes contient Marseille
print(villes.find("Marseille"))

# Question 6: Remplacer Toulouse par Nice
villes = villes.replace("Toulouse", "Nice")
print(villes)

tweet1= "Le président Emmanuel Macron et son premier ministre Jean Castex donneront une conf de presse demain."
tweet2= "Député de la 4e circo des Bouches-du-Rhones, pdt du grpe @FranceInsoumise. JLM ne tweete pas en personne"

# Question 7: Extraire à partir de tweet1 et tweet2
# les noms de personnes qui ont été cités
print(tweet1[13:28])
print(tweet1[53:64])
print(tweet2[75:78])

# Question 8: Afficher la taille de chaine, tweet1 et tweet2
print(len(tweet1))
print(len(tweet2))

# Question 9: utiliser une structure de contrôle (traitement conditionnel) pour faire le traitement suivant :
# afficher OUI si le texte du tweet 1 ou 2 parlent du président de la république et non sinon
if (tweet1.find("Emmanuel Macron")!=(-1)) or (tweet2.find("Emmanuel Macron")!=(-1)):
    print("OUI")
else:
    print("NON")

if ("président" in tweet1) or ("Macron" in tweet1) or ("le chef de l'état" in tweet1) or ("le chef de l'armée" in tweet1):
    print("le tweet1 parle du président")
else:
    print("le tweet1 ne parle pas du président")

# Question 10: soit la chaine de caractère suivantes :
descriptif = "Dans ce roman l'auteur américain nous décrit l'aventure de Huck Finn qui a traversé le Mississipi"
# tester si ce descriptif contient le mot aventure, alors afficher le message suivant
message1 = "C'est un livre d'aventure"
# sinon afficher le message :
message2 = "Ce n'est pas un livre d'aventure"

if (descriptif.find("aventure")!=(-1)):
    print(message1)
else:
    print(message2)
