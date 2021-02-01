#Exercice : extraire les sous-chaines "Jean" "de La" "Fontaine"

identite="Jean de La Fontaine"
prenom=identite[0:4]
nom1=identite[5:10]
nom2=identite[11:]

print(prenom)
print(nom1)
print(nom2)

#Question 2 : calculer et afficher la taille de la chaine suivante
livre_americain="Adventures of Huckleberry Finn de l'auteur américain Mark Twain a été traduit dans les langues vulnérables suivantes : Tamoul, Farsi, Hindi"
taille_livre_americain=len(livre_americain)
print(taille_livre_americain)

#Question 3 : rajouter les 2 langues suivantes à la liste de langues ci-dessus: Basque, Wallon
livre_americain_maj=livre_americain+", Basque, Wallon"
print(livre_americain_maj)

#Question 4 : tester si la chaine de caractère livre_americain_maj est minuscule
print(livre_americain_maj.islower())


#Question 5 : tester si elle commence par "Adventures of Huckleberry Finn"
print(livre_americain_maj.startswith("Adventures of Huckleberry Finn"))

#Question 6 : tester si elle se termine par "Hindi"
print(livre_americain_maj.endswith("Hindi"))

#Question 7 : tester si elle se termine par "Wallon"
print(livre_americain_maj.endswith("Wallon"))

#Question 8 : tester si la chaine contient "Basque"
position=livre_americain_maj.find("Basque")
print(position)
