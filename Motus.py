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

#========================#
# VARIABLES ET FONCTIONS #
#========================#
# Variables
#----------
dictionnaire="dictionnaire.lst"

# on recupere l'emplacement du rep_script
# on se deplace dans ce repertoire qui devient le repertoire de travail
#----------------------------------------------------------------------
rep_script=os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(rep_script)






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

# zone d'affichage des mots
#--------------------------
frame_mots=Frame(root)
frame_mots.grid(row=1)
label_mot_1=Label(frame_mots, text="trte", font=("bold","32"))
label_mot_1.grid(row=1)
label_mot_2=Label(frame_mots, text="trte", font=("bold","32"))
label_mot_2.grid(row=2)
label_mot_3=Label(frame_mots, text="trte", font=("bold","32"))
label_mot_3.grid(row=3)
label_mot_4=Label(frame_mots, text="trte", font=("bold","32"))
label_mot_4.grid(row=4)
label_mot_5=Label(frame_mots, text="trte", font=("bold","32"))
label_mot_5.grid(row=5)
label_mot_6=Label(frame_mots, text="trte", font=("bold","32"))
label_mot_6.grid(row=6)

# zone de choix du nombre de lettres
#-----------------------------------
frame_nbLettre=Frame(root)
frame_nbLettre.grid(row=1,column=2)
label_nbLettre=Label(frame_nbLettre, text="choisissez du nombre de lettres")
label_nbLettre.grid(row=1)
vals=[5,6,7,8,9]
varGr=IntVar(frame_nbLettre,vals[0])
for i in range(5):
    bouton=Radiobutton(frame_nbLettre, variable=varGr, text=vals[i], value=vals[i], indicatoron=0, borderwidth=3)
    bouton.grid(row=2,column=i)





root.mainloop()
#==================#
# FIN DU PROGRAMME #
#==================#