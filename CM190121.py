#langage de script = langage léger pour réaliser des programmes léger avec des fonctionnalités précises,
#langages accessibles à des utilisateurs avec un bagage informatique limité.

#type de variables = nombres entiers, chaines de caractères (texte) et nombres réels

#TD 19 Janvier sur les les chaines de caractères
##Les chaïnes de caractères (anglais string = str).
#plusieurs manières de les écrire :
a= "string" #string destinées à l'affichage (convention d'utilisation, pas obligatoire, mais utile pour la clarté du code)
b= 'string' #usage interne au script (idem convention)
c="""string"""
d='''string'''

#Les chaines à triples délimiteurs permettent d'écrire sur plusieurs lignes.
ml="""Père Castor,
raconte nous une
 histoire"""

#caractères spéciaux :  le \ permet d'écrire les caractères spéciaux : \n (retour à la ligne), \t (tabulation)
ml2="Père Castor,\n raconte nous \n une \t histoire"

#chaine brute (affichage à l'identique sans mise en forme des caractères spéciaux).
#On préfixe la chaine par r. r=raw (brut)
print(r"bla\tbla\nbla")
print("bla\tbla\nbla")

#Déclarer une variable de type chaine de caractère
titre_journal="Quel est le profil du nouveau Congrés américain qui votera les lois ?"
paragraphe="""Avec 26,9 % de femmes, soit 144 sur 535, ce Parlement qui va discuter 
et voter les lois du 46e président, Joe Biden, est le plus féminisé de
l’histoire des Etats-Unis. Il demeure néanmoins beaucoup moins
paritaire que nombre de pays occidentaux : les femmes
représentaient 47 % du Parlement suédois en 2020, 44 % en Espagne
et 36 % en France. Il est aussi en retard sur la société, qui, en Europe
comme aux Etats-Unis, compte environ 51 % de femmes."""
print(titre_journal)
print(paragraphe)

#renvois à la ligne avec \n
paragraphe2="Avec 26,9 % de femmes,\n soit 144 sur 535,\n ce Parlement qui va discuter et voter les lois du 46e président,\n Joe Biden,\n est le plus féminisé de l’histoire des Etats-Unis.\n Il demeure néanmoins beaucoup moins paritaire que nombre de pays occidentaux :\n les femmes représentaient 47 % du Parlement suédois en 2020,\n 44 % en Espagne et 36 % en France.\n Il est aussi en retard sur la société,\n qui,\n en Europe comme aux Etats-Unis,\n compte environ 51 % de femmes."

print(paragraphe2)

#extraire et afficher la date d'élection du congrès
paragraphe3="Le Congrès élu en novembre 2020, c’est-à-dire l’entité formée par la Chambre des représentants (435 membres) et le Sénat (100), est le plus divers et paritaire jamais élu. Avec 26,9 % de femmes, soit 144 sur 535, ce Parlement qui va discuter et voter les lois du 46e président, Joe Biden, est le plus féminisé de l’histoire des Etats-Unis."
print(paragraphe3[18:31])
#extraire la deuxième phrase
print(paragraphe3[172:])

