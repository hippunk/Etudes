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
    if arrondissement <= 0 or arrondissement > 20:
        data.remove(station)
        
#Debug traitement arrondissements parasites
#for station in data:
#    arrondissement = station['number']//1000
#    print(arrondissement)
#    print("\n")


