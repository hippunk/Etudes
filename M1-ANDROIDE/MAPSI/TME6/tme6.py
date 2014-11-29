# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 10:53:53 2014

@author: 3100208
"""

import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt



def tracerLettre(let):
    a = -let*np.pi/180; # conversion en rad
    coord = np.array([[0, 0]]); # point initial
    for i in range(len(a)):
        x = np.array([[1, 0]]);
        rot = np.array([[np.cos(a[i]), -np.sin(a[i])],[ np.sin(a[i]),np.cos(a[i])]])
        xr = x.dot(rot) # application de la rotation
        coord = np.vstack((coord,xr+coord[-1,:]))
    plt.figure()
    plt.plot(coord[:,0],coord[:,1])
    plt.savefig("exlettre.png")
    plt.show()
    
data = pkl.load(file("TME6_lettres.pkl","rb"))
X = np.array(data.get('letters')) # récupération des données sur les lettres
Y = np.array(data.get('labels')) # récupération des étiquettes associées 

def discretise(X,d):
    intervalle = 360. / d
    tab = []
    for i in X:
        tab.append(np.floor(i/intervalle))
    return tab
        
def groupByLabel( y):
    index = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y==i)
        index.append(ind)
    return index     
    
def discretiseTout(data,d,Y):
    tab = []
    aux = []
    tmp = 'a'
    for i in range(len(data)):
        disc = discretise(data[i],d)
        group = groupByLabel(disc)
        aux.append(group)
        if Y[i] != tmp:
            tab.append(aux)
            aux = []
            tmp = Y[i]
            
            
    tab.append(aux)
            
        
    return tab
    
def find_Number(tab, n):
    indice = -1
    for i in range(len(tab)):
        if tab[i].count(n) != 0:
            indice = i
    return indice
    
def learnMarkovModel(Xc, d):
     A = np.zeros((d,d))
     Pi = np.zeros(d)
     
     for i in Xc:
         for j in range(len(i)):
             if i[j][0] == 0:
                 Pi[j] += 1

     Pi = Pi/Pi.sum()
     for i in Xc:
         val = 0
         ind_p = -1
         while(1):
         taille = np.zeros(len(i))
         ind_s = find_Number(i,val)
         taille[ind_s] += 1
         if ind_p != -1:
            if ind_p != ind_s:
                
         
         
#print data
#print X
#print Y

X = discretiseTout(X,3,Y)
print X[0]
#print groupByLabel(res)
#print test[2]
#tracerLettre(X[0])
#Xc = groupByLabel(res)
learnMarkovModel( X[0],3) 