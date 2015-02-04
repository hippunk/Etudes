# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 00:05:38 2014

@author: arthur
"""

import math
import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt

def find_Number(tab, n):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == n:
                return i
            
    return -1
   
def find_max(tab):            
    maxi = -1    
    for i in tab:
        if (i and max(i) > maxi):
            maxi = max(i)
    return maxi

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
    
def discretise(X,d):
    intervalle = 360. / d
    tab = []
    for i in X:
        tab.append(np.floor(i/intervalle))
    return np.array(tab)
   
def groupByDisc(X,d):
    Xtmp = []
    tmp = []
    for l in range(d):
        for i in range(len(X)):
            if X[i] == l:
                tmp.append(i)
        Xtmp.append(tmp)
        tmp = []
        
    return np.array(Xtmp)    

def groupAllByDisc(X,d):
    Xtmp = []

    for j in range(len(X)):
        Xtmp.append(groupByDisc(X[j],d))


    return np.array(Xtmp)  
   
def learnMarkovModel(Xc, d):

     A = np.ones((d,d))
     Pi = np.ones(d)
     for i in range(0,len(Xc)):
         Pi[find_Number(Xc[i],0)]+=1
         maxi = find_max(Xc[i])
         for l in range(0,maxi):
             A[find_Number(Xc[i],l)][find_Number(Xc[i],l+1)]+=1
         
     Pi = Pi/Pi.sum()
     
        
     A = A/np.maximum(A.sum(1).reshape(d,1),1) # normalisation
     #print Pi
     #print A
     return Pi,A
     
def probaSequence(s,Pi,A):

    vra = 0
    maxi = -1.
    #print s
    for k in range(0,len(s)):
        if (s[k] and np.amax(s[k]) > maxi):
            maxi = np.amax(s[k])
            
    #print maxi
     
    ind_p = -1
    for i in range(0,maxi+1):

        if i == 0:
            ind_p = find_Number(s,i)
            #print ind_p
            if(Pi[ind_p] == 0):
                vra += -10000
            else:
                vra += math.log(Pi[ind_p])
        else :
            ind_s = find_Number(s,i)    
            
            if(A[ind_p][ind_s] == 0):
                vra += -10000
            else:
                vra += math.log(A[ind_p][ind_s])

            ind_p = ind_s
            
    return vra
    
def probaComplet(Xtest,models,Ytest):
    probatmp = []
    proba = []
    
    for i in range(len(Xtest)):
        probatmp = []
        for cl in range(len(np.unique(Ytest))):
            probatmp.append(probaSequence(Xtest[i], models[cl][0], models[cl][1]))
        proba.append(probatmp)
        
    return np.array(proba)

def stocker_model(X,d,Y):
    models = []
    for cl in np.unique(Y): # parcours de toutes les classes et optimisation des modèles
        models.append(learnMarkovModel(X[Y==cl], d))
    return models   
    
def separeTrainTest(y, pc):
    indTrain = []
    indTest = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y==i)
        n = len(ind)
        indTrain.append(ind[np.random.permutation(n)][:np.floor(pc*n)])
        indTest.append(np.setdiff1d(ind, indTrain[-1]))
    return indTrain, indTest    
    
def quelleLettre(sProba):
    return sProba.argmax(0)    
    
def evalTest(proba,Y):
    stat = 0
    for i in range(len(Y)):
        if(quelleLettre(proba[i]) == ord(Y[i])-ord('a')):
            stat +=1
        
    return (stat*1.0)/(len(Y)*1.0)
   
data = pkl.load(file("TME6_lettres.pkl","rb"))
X = np.array(data.get('letters')) # récupération des données sur les lettres
Y = np.array(data.get('labels')) # récupération des étiquettes associées 
   
itrain,itest = separeTrainTest(Y,0.8)

ia = []
for i in itrain:
    ia += i.tolist()    
it = []
for i in itest:
    it += i.tolist()   
   
d = 200

Xd = discretise(X,d)
Xdisc = groupAllByDisc(Xd,d)
   
Xtrain = Xdisc[ia]
Xtest = Xdisc[it]
Ytrain = Y[ia]
Ytest = Y[it]

models = stocker_model(Xtrain,d,Ytrain)

proba = probaComplet(Xtest,models,Ytest)
#proba = np.array([[probaSequence(Xtest[i], models[cl][0], models[cl][1]) for i in range(len(Xtest))]for cl in range(len(np.unique(Ytest)))])

print evalTest(proba,Ytest)," D : ",d


conf = np.zeros((26,26))

for i in range(len(proba)):
    conf[quelleLettre(proba[i])][ord(Ytest[i])-ord('a')]+=1


plt.figure()
plt.imshow(conf, interpolation='nearest')
plt.colorbar()
plt.xticks(np.arange(26),np.unique(Ytest))
plt.yticks(np.arange(26),np.unique(Ytest))
plt.xlabel(u'Vérité terrain')
plt.ylabel(u'Prédiction')
plt.savefig("mat_conf_lettres.png")
plt.show()