# -*- coding : utf-8 -*-

# Header
"""
Librairie pour le pendu
Fait par Delaplaine Romain
11/12/2020
To do : tout
"""

# Ici je fais mes imports

import tkinter
import librairie_pendu as pendu

# Mes fonctions spécifiques à tkinter

def dessin_1 ():
    x = [50,400]
    y = [150,400]
    canevas.create_line(x[0],x[1],y[0],y[1],fill='green',width='4')

def dessin_2 ():
    x = [100,400]
    y = [100,100]
    canevas.create_line(x[0],x[1],y[0],y[1],fill='green',width='4')

def dessin_3 ():
    x = [100,100]
    y = [350,100]
    canevas.create_line(x[0],x[1],y[0],y[1],fill='green',width='4')

def dessin_4 ():
    x = [350,100]
    y = [350,175]
    canevas.create_line(x[0],x[1],y[0],y[1],fill='green',width='4')

def dessin_5 ():
    x = [80,400]
    y = [100,350]
    canevas.create_line(x[0],x[1],y[0],y[1],fill='green',width='4')

def dessin_6 ():
    x = [120,400]
    y = [100,350]
    canevas.create_line(x[0],x[1],y[0],y[1],fill='green',width='4')

def dessin_7 ():
    x = [100,150]
    y = [150,100]
    canevas.create_line(x[0],x[1],y[0],y[1],fill='green',width='4')

def dessin_8 ():
    x = 350
    y = 190
    r = 15
    canevas.create_oval(x-r, y-r, x+r, y+r, outline='green',width='4')
    x1 = [350,205]
    y1 = [350,285]
    canevas.create_line(x1[0],x1[1],y1[0],y1[1],fill='green',width='4')
    x2 = [330,230]
    y2 = [370,230]
    canevas.create_line(x2[0],x2[1],y2[0],y2[1],fill='green',width='4')
    x3 = [330,310]
    y3 = [350,285]
    z3 = [370,310]
    canevas.create_line(x3[0],x3[1],y3[0],y3[1],z3[0],z3[1],fill='green',width='4')

def fDraw (pVie) :
    if pVie == 8:
        dessin_1()
    elif pVie == 7:
        dessin_2()
    elif pVie == 6:
        dessin_3()
    elif pVie == 5:
        dessin_4()
    elif pVie == 4:
        dessin_5()
    elif pVie == 3:
        dessin_6()
    elif pVie == 2:
        dessin_7()
    elif pVie == 1:
        dessin_8()

def fStart ():
    global mot
    global mot_cache
    global liste_lettre
    global ma_vie
    global point
    mot = pendu.fChoix_mot("banque.txt")
    mot_cache = pendu.fAffichage(mot)
    liste_lettre = []
    ma_vie = 8
    label1.set(mot_cache)
    point = pendu.fGet_score("score.txt")
    label3.set(point)
    canevas.delete("all")

def fTest_lettre ():
    global lettre
    global ma_vie
    global mot_cache
    global point
    global i
    lettre = saisie.get()
    validite = pendu.fValidite_saisie(lettre)
    if validite :
        test , mot_cache = pendu.fTest_lettre(lettre, liste_lettre,mot,mot_cache)
        label2.set(",".join(liste_lettre))
        if not test :
            fDraw(ma_vie)
            ma_vie -= 1
            if ma_vie == 0 :
                label2.set("Vous avez perdu ...\n Le mot été : "+mot)
                i = 0
                bouton_val.set("Rejouer")
        elif pendu.fVictoire(mot,mot_cache):
            label2.set("Vous avez gagné !!!\n Le mot été : "+mot)
            point = pendu.fUp_score(int(point),"score.txt")
            i = 0
            bouton_val.set("Rejouer")
    else :
        label2.set("Saisie incorrect \n" + ",".join(liste_lettre))
    label1.set(mot_cache)
    champ.delete(0, "end")

def fGestion_bouton ():
    global i
    if i == 0 :
        fStart()
        i = 1
        bouton_val.set("Valider")
    elif i == 1 :
        fTest_lettre()

# Je crée tout les outils de ma fenêtre


"""creation de ma fenetre"""
mywindow = tkinter.Tk()
mywindow.title('Pendu')
mywindow['bg'] = 'grey'

"""creation du widget pour le dessin"""
Largeur = 500
Hauteur = 500
canevas = tkinter.Canvas(mywindow,width = Largeur , height = Hauteur, bg = 'black')
canevas.grid(row = 1 , column = 2 , rowspan = 4 , padx = 10 ,pady = 10)

"""creation d'une frame pour lancer le jeu et afficher le mot recherché"""
frame1 = tkinter.Frame(mywindow ,bg = "grey" , relief = 'groove')
frame1.grid(row = 1 , column = 1 , rowspan = 2 , padx = 10 ,pady = 10)

label1 = tkinter.StringVar()
tkinter.Label(frame1, textvariable = label1 , font = ("Courier",30) , bg = "grey").grid(padx = 10 ,pady = 10)


"""creation d'une frame pour entrer une lettre et la valider"""
frame3 = tkinter.Frame(mywindow ,bg = "grey" , relief = 'groove')
frame3.grid(row = 3 , column = 1 , padx = 10 ,pady = 10)

tkinter.Label(frame3, text = 'Lettre :' , font = "Courier" , bg = "grey").pack(side = 'left', padx = 10 , pady = 10)

saisie = tkinter.StringVar()
champ = tkinter.Entry(frame3,textvariable = saisie)
champ.focus_set()
champ.pack(side = 'left', padx = 10 , pady = 10)

bouton_val = tkinter.StringVar()
bouton_val.set("Jouer")
Bouton1 = tkinter.Button(frame3, textvariable = bouton_val , font = "Courier" , command = fGestion_bouton )
Bouton1.pack(side = 'left', padx = 10 , pady = 10)

"""creation d'une frame pour afficher des informations"""
frame2 = tkinter.Frame(mywindow , bg = "grey" , relief = 'groove')
frame2.grid(row = 4 , column = 1 , padx = 10 ,pady = 10)

label2 = tkinter.StringVar()
tkinter.Label(frame2, textvariable = label2 , bg = "grey").grid(row = 1 , columnspan = 2 , padx = 10 ,pady = 10)

label3 = tkinter.StringVar()
tkinter.Label(frame2, textvariable = label3 , bg = "grey").grid(row = 2 , column = 2 , padx = 10 ,pady = 10)

tkinter.Label(frame2, text = "Votre score :" , bg = "grey").grid(row = 2 , column = 1 , padx = 10 ,pady = 10)

# code principal

i = 0
pendu.fTri("banque.txt")

# Je lance ma fenetre

mywindow.mainloop()