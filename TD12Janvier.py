# 2ème TD en Langages de Scripts TD3


# Question 1: Afficher le message suivant " C'est mon deuxième script Python "
print("C'est mon deuxième script Python")

# Question 2: déclarer 4 variables permettant d'enregister le titre d'un livre de votre choix, le nom de l'auteur, 
#l'année de publication et le nom de l'éditeur
titre="Dune"
auteur="Frank Herbert"
anneePub=2020
editeur="Robert Laffont"

# Question 3: Afficher le contenu des 4 variables ci-dessus dans un message décrivant le livre 
# par exemple: le livre Apocalypse cognitive a été écrit par ... et publié par ...en ...
print("Le roman "+titre+" a été écrit par "+auteur+" et publié par "+editeur+" en",anneePub,".")
print("Le roman "+titre+" a été écrit par "+auteur+" et publié par "+editeur+" en "+str(anneePub)+".")

# Question 4: déclarer 3 variables de type entier (integer) de votre choix
x=42
y=101010
z=21

# Question 5 : calculer et afficher la moyenne des 3 valeurs des 3 variables ci-dessus.
m=(x+y+z)/3
print(m)
