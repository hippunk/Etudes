# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import numpy as np
import matplotlib.pyplot as plt
import requests
import pickle as pkl
import time
plt.close('all')                 # fermer les fenêtres 

fname = "dataVelib.pkl"
f= open(fname,'rb')
data = pkl.load(f)
f.close()
liste = []

#Suppression des arrondissements parasites
for station in data:
    arrondissement = station['number']//1000
    if arrondissement > 0 and arrondissement <= 20:
        liste.append({'alt':station['alt'],'lng':station['position']['lng'],'lat':station['position']['lat'],'arr':station['number']//1000,'tot':station['bike_stands'],'disp':station['available_bikes']})

#Calcul du nombre de stations par arrondissements
nbArr = [0]*20
for elem in liste:   
    nbArr[elem['arr']-1]+=1

#Division par le nombre de stations, Utilisation de pynum pour éviter boucle ?    
probArr = []
for elem in nbArr:   
    probArr.append(elem/len(liste))
 
#Affichages des probabilitées   
#print(probArr)

#debug somme proba, Utilisation de pynum pour éviter boucle ?
#x = 0
#for elem in probArr:   
#    x+=elem
#print(x)   
        
#Debug traitement arrondissements parasites
#for station in data:
#    arrondissement = station['number']//1000
#    print(arrondissement)
#    print("\n")


