# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 10:53:53 2014

@author: 3100208
"""
import math
import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt

data = pkl.load(file("../TME7/TME6_lettres.pkl","rb"))
X = np.array(data.get('letters')) # récupération des données sur les lettres
Y = np.array(data.get('labels')) # récupération des étiquettes associées   

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
    return tab


#print learnMarkovModel(test2, 3)
def groupByDisc(X,d):
    Xtmp = []
    tmp = []
    for l in range(d):
        for i in range(len(X)):
            if X[i] == l:
                tmp.append(i)
        Xtmp.append(tmp)
        tmp = []
        
    return Xtmp    

def groupAllByDisc(X,d):
    Xtmp = []
    for i in range(len(X)):
        Xtmp.append(groupByDisc(X[i],d))

    return Xtmp    
    
def rangeParClasse(data,d):
    tab = []
    aux = []
    tmp = 'a'
    for i in range(len(data)):
        group = groupByDisc(data[i],d)
        if Y[i] != tmp:
            tab.append(aux)
            aux = []
            aux.append(group)
            tmp = Y[i]
        else :
           aux.append(group) 
            
            
    tab.append(aux)
    return tab
    
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
   

def learnMarkovModel(Xc, d):

     A = np.zeros((d,d))
     Pi = np.zeros(d)
     
     for i in range(0,len(Xc)):
         Pi[find_Number(Xc[i],0)]+=1
         maxi = find_max(Xc[i])
         for l in range(0,maxi):
             A[find_Number(Xc[i],l)][find_Number(Xc[i],l+1)]+=1
         
     Pi = Pi/Pi.sum()
     
        
     A = A/np.maximum(A.sum(1).reshape(d,1),1) # normalisation
     print Pi
     print A
     return Pi,A
     
#print data
#print X
#print Y

def stocker_model(X,d):
    models = []
    for cl in range(0,26): # parcours de toutes les classes et optimisation des modèles
        models.append(learnMarkovModel(X[cl], d))
    return models
    
def probaSequence(s,Pi,A):

    vra = 1
    maxi = -1
    for k in range(0,len(s)):
        if (s[k] and np.amax(s[k]) > maxi):
            maxi = np.amax(s[k])
     
    ind_p = -1
    for i in range(0,maxi+1):

        if i == 0:
            ind_p = find_Number(s,i)
            vra *= Pi[ind_p]
        else :
            ind_s = find_Number(s,i)         
            vra *= A[ind_p][ind_s]
            ind_p = ind_s
    if vra <= 0:
        vra=-100000000
    else :
        vra = math.log(vra)
    return vra
    
# separation app/test, pc=ratio de points en apprentissage
def separeTrainTest(y, pc):
    indTrain = []
    indTest = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y==i)
        n = len(ind)
        indTrain.append(ind[np.random.permutation(n)][:np.floor(pc*n)])
        indTest.append(np.setdiff1d(ind, indTrain[-1]))
    return indTrain, indTest


def getXtestNtrain(X,itrain,itest,Y):
    xTrainTmp = []
    xTestTmp = []
    xTrain = []
    xTest = []
    Ytest = np.array([])
    
    for i in range(26):
        for train in itrain[i]:
            xTrainTmp.append(X[train])
            
        for test in itest[i]:
            xTestTmp.append(X[test])
            Ytest = np.append(Ytest,test)
            
        xTrain.append(xTrainTmp)
        xTest.append(xTestTmp)
        xTrainTmp = []
        xTestTmp = []

        
    return xTrain,xTest,Ytest

def test1(disc):


    d = disc

    Xd = discretise(X,d)
    Xr = rangeParClasse(Xd,d)
    
    models = stocker_model(Xr,d)
    
    Xkk = []
    for cl in range(26):
        for i in range(len(Xr[cl])): 
            Xkk.append(Xr[cl][i])   
    
    proba = np.array([[probaSequence(Xkk[i], models[cl][0], models[cl][1]) for i in range(len(Xkk))]for cl in range(26)])

    Ynum = np.zeros(Y.shape)
    for num,char in enumerate(np.unique(Y)):
        Ynum[Y==char] = num
    pred = proba.argmax(0) # max colonne par colonne
    print np.where(pred != Ynum, 0.,1.).mean()


test1(3)

"""
data = pkl.load(file("TME6_lettres.pkl","rb"))
X = np.array(data.get('letters')) # récupération des données sur les lettres
Y = np.array(data.get('labels')) # récupération des étiquettes associées   

d = 3

Xd = discretise(X,d)
Xk = groupAllByDisc(Xd,d)
itrain,itest = separeTrainTest(Y,0.9)
xTrain,xTest,Ytest = getXtestNtrain(Xk,itrain,itest,Y)

models = stocker_model(xTrain,d)

Xkk = []
for cl in range(26):
    for i in range(len(xTest[cl])): 
        Xkk.append(xTest[cl][i])    
        
print models[0][0],models[0][1]
for i in range(26):
    print probaSequence(Xkk[7], models[i][0], models[i][1])
    
        
proba = np.array([[probaSequence(Xkk[i], models[cl][0], models[cl][1]) for i in range(len(Xkk))]for cl in range(26)])


Ynum = np.zeros(Ytest.shape)
for num,char in enumerate(np.unique(Ytest)):
    Ynum[Ytest==char] = num
pred = proba.argmax(0) # max colonne par colonne
print np.where(pred != Ynum, 0.,1.).mean()"""