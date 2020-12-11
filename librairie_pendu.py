# -*- coding : utf-8 -*-

# Header
"""
Librairie pour le pendu
Fait par Delaplaine Romain
27/11/2020
To do : rien
"""

import random as rd

#fonction qui trie le fichier pour le mettre dans le bon ordre
"""param : fichier.txt / sortie : le fichier trié"""

def fTri (pFichier):
    fichier = open(pFichier,"r")
    liste_1 = []
    for ligne in fichier :
            ligne = ligne.strip()
            if ligne :
                liste_1.append(ligne)
    dico = {}
    liste_2 = []
    sorted(liste_1, key=len)
    for val in liste_1:
        size = len(val)
        if size not in dico.keys() :
            dico[size] = [val]
        elif val not in dico[size] :
            dico[size].append(val)
    for i in dico.keys() :
        liste_tri = sorted(dico[i])
        liste_2.extend(liste_tri)    
    fichier.close()
    fichier = open(pFichier, "w")        
    for val in liste_2:
        fichier.write(val + "\n")
    fichier.close()
    return fichier

#fonction qui récupère un mot random
"""param : fichier.txt / sortie : le mot"""

def fChoix_mot (pFichier):
    fichier = open(pFichier)
    liste = []
    for ligne in fichier :
        ligne = ligne.strip()
        if ligne :
            liste.append(ligne)
    i = rd.randint(0,len(liste)-1)
    mot = liste[i]
    fichier.close()
    return mot

#fonction qui affiche le mot avec les underscores
"""param : mot / sortie : mot_affichage"""

def fAffichage (pMot) :
    mot_affichage = pMot[0].upper()
    for i in range(1,len(pMot)):
        mot_affichage += "_"
    return mot_affichage

#fonction qui remplace le _ par la lettre trouvé
"""param : lettre,motcdu pendu / sortie : mot_affichage"""

def fReplace_lettre (pLettre,pMot,pMot_affichage) :
    pMot_affichage = list(pMot_affichage)
    for i,lettre in enumerate (pMot) :
        if pLettre == lettre :
            pMot_affichage[i] = lettre
    return "".join(pMot_affichage)

#fonction qui verifie si la lettre a deja ete dite
"""param : lettre,liste de lettre / sortie : rien"""

def fPresence_lettre (pLettre,pListe_lettre) :
    rep = False     #la lettre est nouvelle
    if pLettre in pListe_lettre :
        rep = True      #la lettre a deja ete dite
    else :
        pListe_lettre.append(pLettre)
    return rep

#fonction qui demande au joueur d'entrer une lettre pr la tester
"""param : mot du pendu,mot_affichage,vie / sortie : true false en fct de la presence et le mot a afficher"""

def fTest_lettre (pLettre,pListe_lettre,pMot,pMot_affichage) :
    succes = True
    test = fPresence_lettre (pLettre,pListe_lettre)
    if test == False :   #plus de visibilité comme ca
        if pLettre.lower() in pMot.lower() :
            pMot_affichage = fReplace_lettre(pLettre,pMot,pMot_affichage)
        else :
            succes = False
    else :
        print ("lettre deja dite")
    return succes,pMot_affichage

#fonction qui verifie si le joueur a gagné
"""param : mot, mot_afficahge / sortie : True ou false"""

def fVictoire (pMot,pMot_affichage) :
    if pMot == pMot_affichage :
        return True
    else :
        return False


#fonction qui demande au joueur s'il veut rejouer
"""param : rien / sortie : True ou false"""

def fRejouer ():
    rep = input("voulez-vous rejouez ? (1 pour oui,0 pour non) ")
    if rep == "0" :
        return False
    else :
        return True

#fonction qui calcule le nouveau score
"""param : ancien score / sortie : nouveau score"""

def fUp_score (pScore,pFichier):
    fichier = open(pFichier,"w")
    pScore += 1
    fichier.write(str(pScore))
    fichier.close()
    return pScore

#fonction qui calcule le nouveau score
"""param : fichier de score / sortie : score"""

def fGet_score (pFichier):
    fichier = open(pFichier)
    liste = []
    for ligne in fichier :
        ligne = ligne.strip()
        if ligne :
            liste.append(ligne)
    score = liste[0]
    fichier.close()
    return score

#fonction pour verifier la saisie de l'utilisateur
"""param : entre / sortie : true ou false"""

def fValidite_saisie (pEntre):
    rep = False
    if len(pEntre) == 1 :
        rep = True 
    return rep