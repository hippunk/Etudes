# -*- coding: utf-8 -*-

import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
from math import *
from random import *

data = pkl.load(file("lettres.pkl","rb"))
X = np.array(data.get('letters')) # récupération des données sur les lettres
Y = np.array(data.get('labels')) # récupération des étiquettes associées 


# affichage d'une lettre
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
    #plt.savefig("exlettre.png")
    plt.show()
    return
   
#print(Y)
#tracerLettre(X[5])

def discretise(X,d):
    intervalle=360./d
    nX=np.copy(X)
    for i in range(len(X)):
        nX[i]=np.floor(X[i]/intervalle)
    return nX
    
#print(discretise(X,3)[0])
        
def groupByLabel( y):
    index = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y==i)
        index.append(ind)
    return index
    
#print(groupByLabel(discretise(X,3)[0]))

def learnMarkovModel(Xc, d):
     A = np.zeros((d,d))
     Pi = np.zeros(d)
     cour=0
     for i in range(len(Xc)):
         cour=Xc[i][0]
         Pi[cour]=Pi[cour]+1
         for j in range(1,len(Xc[i])):
             A[cour][Xc[i][j]]=A[cour][Xc[i][j]]+1
             cour=Xc[i][j]
     A = A/np.maximum(A.sum(1).reshape(d,1),1) # normalisation
     Pi = Pi/Pi.sum()
     return(Pi,A)
     
def learnMarkovModelOnes(Xc, d):
     A = np.ones((d,d))
     Pi = np.ones(d)
     cour=0
     for i in range(len(Xc)):
         cour=Xc[i][0]
         Pi[cour]=Pi[cour]+1
         for j in range(1,len(Xc[i])):
             A[cour][Xc[i][j]]=A[cour][Xc[i][j]]+1
             cour=Xc[i][j]
     A = A/np.maximum(A.sum(1).reshape(d,1),1) # normalisation
     Pi = Pi/Pi.sum()
     return(Pi,A)
    
def groupLettres(X,Y,labels):
    nX=[] 
    for i in range(len(Y)):
       if(Y[i]==labels): nX.append(X[i])
    return np.array(nX)
    
    
def probaSequence(s,Pi,A):
    res=Pi[s[0]]
    for i in range(1,len(s)):
        res=res*A[s[i-1]][s[i]]
    if(res>0):
        return log(res)
    else:
        return float("-infinity") 
        
        
        
def separeTrainTest(y, pc):
    indTrain = []
    indTest = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y==i)
        n = len(ind)
        indTrain.append(ind[np.random.permutation(n)][:np.floor(pc*n)])
        indTest.append(np.setdiff1d(ind, indTrain[-1]))
    return indTrain, indTest
    
    
    
    
    
def generate(Pi,A,nb):
    s=[]
    cour=0
    sPi=Pi.cumsum()
    sA=np.copy(A)
    for i in range(len(A)):
        sA[i]=A[i].cumsum()
    r=random()
    i=0
    while(i<len(sPi) and r>sPi[i]) :i=i+1
    s.append(i)
    for i in range(1,nb):
        r=random()
        j=0

        while(j<len(sA[cour]) and r>sA[cour][j]): j=j+1
        if(j==len(sA[cour])): j=j-1
        s.append(j)
        cour=j
    return s    
    

#print(groupLettres(X,Y,'a'))
#d=4
#Xc=discretise(groupLettres(X,Y,'a'),d)
#print(learnMarkovModel(Xc, d))
  


d=100    # paramètre de discrétisation
Xd = discretise(X,d)  # application de la discrétisation
index = groupByLabel(Y)  # groupement des signaux par classe
models = []
for cl in range(len(np.unique(Y))): # parcours de toutes les classes et optimisation des modèles
    models.append(learnMarkovModel(Xd[index[cl]], d)) 


    

   
proba=np.zeros(26)
for i in range(26): proba[i]=probaSequence(Xd[0],models[i][0],models[i][1])
print(proba)

proba = np.array([[probaSequence(Xd[i], models[cl][0], models[cl][1]) for i in range(len(Xd))]for cl in range(len(np.unique(Y)))])

Ynum = np.zeros(Y.shape)
for num,char in enumerate(np.unique(Y)):
    Ynum[Y==char] = num
    
pred = proba.argmax(0) # max colonne par colonne

print np.where(pred != Ynum, 0.,1.).mean()

# separation app/test, pc=ratio de points en apprentissage

# exemple d'utilisation
itrain,itest = separeTrainTest(Y,0.8)

ia = []
for i in itrain:
    ia += i.tolist()    
it = []
for i in itest:
    it += i.tolist()
      
#print itrain
models = []
for cl in range(len(np.unique(Y))): # parcours de toutes les classes et optimisation des modèles
    models.append(learnMarkovModel(Xd[itrain[cl]], d))     

modelsOnes = []
for cl in range(len(np.unique(Y))): # parcours de toutes les classes et optimisation des modèles
    modelsOnes.append(learnMarkovModelOnes(Xd[index[cl]], d))         
  
    
probait = np.array([[probaSequence(Xd[i], models[cl][0], models[cl][1]) for i in it] for cl in range(len(np.unique(Y)))])
probaia = np.array([[probaSequence(Xd[i], models[cl][0], models[cl][1]) for i in ia] for cl in range(len(np.unique(Y)))])

probaitO = np.array([[probaSequence(Xd[i], modelsOnes[cl][0], modelsOnes[cl][1]) for i in it] for cl in range(len(np.unique(Y)))])
probaiaO = np.array([[probaSequence(Xd[i], modelsOnes[cl][0], modelsOnes[cl][1]) for i in ia] for cl in range(len(np.unique(Y)))])

Ynumit = np.zeros(Y[it].shape)
for num,char in enumerate(np.unique(Y[it])):
    Ynumit[Y[it]==char] = num
    
Ynumia = np.zeros(Y[ia].shape)
for num,char in enumerate(np.unique(Y[ia])):
    Ynumia[Y[ia]==char] = num
    
    
predia = probaia.argmax(0) # max colonne par colonne
predit = probait.argmax(0) # max colonne par colonne

prediaO = probaiaO.argmax(0) # max colonne par colonne
preditO = probaitO.argmax(0) # max colonne par colonne

print ('app :' + repr(np.where(predia != Ynumia, 0.,1.).mean())) 
print ("test :" + repr(np.where(predit != Ynumit, 0.,1.).mean()))

print ('appO :' + repr(np.where(prediaO != Ynumia, 0.,1.).mean())) 
print ("testO :" + repr(np.where(preditO != Ynumit, 0.,1.).mean()))


conf = np.zeros((26,26))

for i in range(len(predit)) :
    conf[predit[i]][Ynumit[i]]=conf[predit[i]][Ynumit[i]]+1

confO = np.zeros((26,26))
for i in range(len(predit)) :
    confO[preditO[i]][Ynumit[i]]=confO[preditO[i]][Ynumit[i]]+1
    
plt.figure()
plt.subplot(121)
plt.imshow(conf, interpolation='nearest')
plt.colorbar()
plt.xticks(np.arange(26),np.unique(Y))
plt.yticks(np.arange(26),np.unique(Y))
plt.xlabel(u'Vérité terrain')
plt.ylabel(u'Prédiction')
plt.subplot(122)
plt.imshow(confO, interpolation='nearest')
plt.colorbar()
plt.xticks(np.arange(26),np.unique(Y))
plt.yticks(np.arange(26),np.unique(Y))
plt.xlabel(u'Vérité terrain')
plt.ylabel(u'Prédiction')
#plt.savefig("mat_conf_lettres.png")
plt.show()



    

newa = generate(modelsOnes[25][0],modelsOnes[25][1], len(Xd[0])) # generation d'une séquence d'états
print newa
print Xd[0]
intervalle = 360./d # pour passer des états => valeur d'angles
newa_continu = np.array([i*intervalle for i in newa]) # conv int => double
tracerLettre(newa_continu)
i = 40
print Y[i]
tracerLettre(np.array([i*intervalle for i in Xd[i]]))

