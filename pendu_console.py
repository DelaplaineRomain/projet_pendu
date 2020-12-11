# -*- coding : utf-8 -*-

# Header
"""
Librairie pour le pendu
Fait par Delaplaine Romain
27/11/2020
To do : rien
"""
import librairie_pendu as lib
import tkinter

volonte = True
point = lib.fGet_score("score.txt")
lib.fTri("banque.txt")

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
        validite = lib.fValidite_saisie(lettre)
        if validite :
            succes,mot_affichage = lib.fTest_lettre(lettre,liste_lettre,mot,mot_affichage)
            if not succes :
                vie -= 1
            resultat = lib.fVictoire (mot.lower(),mot_affichage.lower())
        else :
            print("Saisie incorrect")
    if vie == 0 :
        print ("vous avez perdu")
        print ("le mot été :",mot)
    elif resultat == True :
        print ("vous avez gagné")
        print ("le mot été :",mot)
        point = lib.fUp_score(int(point),"score.txt")
    volonte = lib.fRejouer()

print ("Nombre de point",point)


