# -*- coding : utf-8 -*-

# Header
"""
Librairie pour le pendu
Fait par Delaplaine Romain
27/11/2020
To do : rien
"""
import librairie_pendu as lib

volonte = True
point = 0

while volonte == True :
    vie = 8
    resultat = False
    mot = lib.fChoix_mot("banque.txt")
    mot_affichage = lib.fAffichage(mot)
    liste_lettre = []
    while vie != 0 and resultat != True:
        print ("votre vie :",vie)
        print (mot_affichage)
        lettre = input("veuillez choisir une lettre:")
        succes,mot_affichage = lib.fTest_lettre(lettre,liste_lettre,mot,mot_affichage)     #a modifier 
        if not succes :
            vie -= 1
        resultat = lib.fVictoire (mot.lower(),mot_affichage.lower())
    if vie == 0 :
        print ("vous avez perdu")
    elif resultat == True :
        print ("vous avez gagné")
        point += 1
    volonte = lib.fRejouer()

print ("Nombre de point",point)


