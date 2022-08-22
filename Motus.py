#!/usr/bin/python3
#===============================================================================================================#
#---------------------------------------------------------------------------------------------------------------#
# Nom				:	Motus.py    						    												#
# Description		:	Jeu MOTUS - Proposer des mots afin de déterminer la composition du mot mystère          #
#                           pour chaque proposition, on détermine si la lettre est présente ou pas et si elle   #
#                           est bien positionnée                                                                #
#																												#
# ENTREE																										#
#	Parametre(s)	:	n/a             																		#
#	Fichier(s)		:	dictionnaire.lst                                           								#
#																												#
# Script(s) lance(s)	:	n/a                                             									#
#																												#
# SORTIE																										#
# 	Fichier(s)		:	n/a                                                              						#
# 	Code Retour		: 	0 = OK																					#
#						autre = KO																				#
#																												#
#===============================================================================================================#
# Version	| Date			| Modifications																		#
#---------------------------------------------------------------------------------------------------------------#
# 1.0		| 10/08/2022	| EN - Creation																		#
#---------------------------------------------------------------------------------------------------------------#
#===============================================================================================================#


#==========#
# PACKAGES #
#==========#
import os,sys,glob,pathlib							# os : utiliser les fonctionnalites dependantes du systeme d'exploitation // sys : fournit un acces a certaines variables utilisees et maintenues par l'interpreteur // glob : recherche de chemins de style Unix selon certains motifs
from tkinter import *                               # module pour IHM python
from random import randint                          # module pour generer des nombre aléatoire      randint(min,max)

#===========#
# VARIABLES #
#===========#
# Variables
#----------
dictionnaire="dictionnaire.lst"
vals=(5,6,7,8,9)                    # les differents niveau du jeu à x lettres.
global tour
tour=1

# on recupere l'emplacement du rep_script
# on se deplace dans ce repertoire qui devient le repertoire de travail
#----------------------------------------------------------------------
rep_script=os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(rep_script)

#===========#
# FONCTIONS #
#===========#
def creationListeMot(fichier,nbLettre):                 # fonction pour créer la liste des mots correspondant au nombre de lettre
    if os.path.isfile(fichier):
        listeMot=[]
        with open(fichier,"r") as fichier_dico:
            for ligne in fichier_dico:
                if len(ligne)==(nbLettre+1):                                                        # on ajoute 1 à cause de l'indice 0
                    ligne=ligne.translate(ligne.maketrans("àâäéèëêïîöôüûù","aaaeeeeiioouuu"))       # on remplace les caractères spéciaux
                    ligne=ligne.strip("\n")                                                         # on supprime le retour chariot
                    ligne=ligne.upper()                                                             # on mets en majuscule
                    listeMot.append(ligne)                                                          # on ajoute à la liste
    else:
        print("Le fichier de dictionnaire n'est pas disponible. Le programme s'arrête.")
        quit()
    listeMot=tri_unique_list(listeMot)
    return listeMot

def tri_unique_list(liste_in):
	liste_out=set(liste_in)			# convertie la liste en set qui permet de n'avoir aucun element duplique
	liste_out=list(liste_out)		# convertie le set en liste
	liste_out.sort()				# trie la liste par ordre alphabetique
	return liste_out

def button_state(status):
    if status:
        for i in range(len(vals)):
            rBouton=Radiobutton(frame_nbLettre, variable=var_nbLettre, text=vals[i], value=vals[i], indicatoron=0, borderwidth=3)
            rBouton.grid(row=2,column=i)
        button_newGame.config(state="normal")
        entry_saisi.config(state="disabled")
        button_valide.config(state="disabled")
        button_abandon.config(state="disabled")
    else:
        for i in range(len(vals)):
            rBouton=Radiobutton(frame_nbLettre, variable=var_nbLettre, text=vals[i], value=vals[i], indicatoron=0, borderwidth=3, state="disabled")
            rBouton.grid(row=2,column=i)
        button_newGame.config(state="disabled")
        entry_saisi.config(state="normal")
        button_valide.config(state="normal")
        button_abandon.config(state="normal")

def new_game():
    button_state(False)
    creationListeMot(dictionnaire,var_nbLettre.get())

def affiche_mot(mot):
    mot=StringVar()
    i=1
    global tour
    # for m in mot:
    #     label_mot=Label(frame_mots, text=m, font=("bold","32"))
    #     label_mot.grid(row=tour,column=i)
    #     i+=1
    label_mot=Label(frame_mots, textvariable=mot, font=("bold","32"))
    label_mot.grid(row=tour,column=i)

def abandon():
    button_state(True)
    print("Espece de nul")
    global tour
    tour=1

def saisi():
    global tour
    entry_saisi.delete(0,last=99)           # on vide la zone de saisi
    affiche_mot(var_saisi.get())
    tour+=1


#====================#
# DEBUT DU PROGRAMME #
#====================#
root=Tk()
root.title('MO.MO.MOTUS')
root.geometry("1200x675")

# Creation de l'IHM du jeu
#=========================
# image de fond
#--------------
bg=PhotoImage(file=f"{rep_script}\motus_bg.png")
label0=Label(root,image=bg)
label0.place(x=0,y=0)

# zone de choix du nombre de lettres
#-----------------------------------
frame_nbLettre=Frame(root)
frame_nbLettre.grid(row=1,column=1)
label_nbLettre=Label(frame_nbLettre, text="choisissez du nombre de lettres")
label_nbLettre.grid(row=1)
button_newGame=Button(frame_nbLettre, text="Nouvelle partie",command=new_game)
button_newGame.grid(row=3)
var_nbLettre=IntVar(frame_nbLettre,vals[0])

# zone de saisi
#--------------
frame_saisi=Frame(root)
frame_saisi.grid(row=2,column=1)
var_saisi=StringVar()
entry_saisi=Entry(frame_saisi, textvariable=var_saisi, width=25, state="disabled")
entry_saisi.grid(row=1,column=1)
button_valide=Button(frame_saisi, text="Valider",command=saisi, state="disabled")
button_valide.grid(row=3,column=1)
button_abandon=Button(frame_saisi, text="Abandonner",command=abandon, state="disabled")
button_abandon.grid(row=3,column=2)

# zone d'affichage des mots
#--------------------------
frame_mots=Frame(root)
frame_mots.grid(row=1,column=2)

# modification du status du jeu
# True = en mode saisi des mots ; False = en mode choix de la difficulté
#-----------------------------------------------------------------------
button_state(True)


root.mainloop()
#==================#
# FIN DU PROGRAMME #
#==================#