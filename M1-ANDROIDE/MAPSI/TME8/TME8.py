# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 10:51:07 2014

@author: 3000892
"""

# -*- coding: utf-8 -*-


import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from math import *
from random import *


# fonction de suppression des 0 (certaines variances sont nulles car les pixels valent tous la même chose)
def woZeros(x): 
    y = np.where(x==0., 1., x)
    return y

# Apprentissage d'un modèle naïf où chaque pixel est modélisé par une gaussienne (+hyp. d'indépendance des pixels)
# cette fonction donne 10 modèles (correspondant aux 10 classes de chiffres)
# USAGE: theta = learnGauss ( X,Y )
# theta[0] : modèle du premier chiffre,  theta[0][0] : vecteur des moyennes des pixels, theta[0][1] : vecteur des variances des pixels
def learnGauss (X,Y): 
    theta = [(X[Y==y].mean(0),woZeros(X[Y==y].var(0))) for y in np.unique(Y)]
    return (np.array(theta)) 

# Application de TOUS les modèles sur TOUTES les images: résultat = matrice (nbClasses x nbImages)
def logpobs(X, theta):
    logp = [[-0.5*np.log(mod[1,:] * (2 * np.pi )).sum() + -0.5 * ( ( x - mod[0,:] )**2 / mod[1,:] ).sum () for x in X] for mod in theta ]
    return np.array(logp)
    
    
    
    
    
    
# la fonction f du tme
# x et w sont des vecteurs , b est une constante (je crois)   
def f (x, w , b):
    result = 0
    for i in range (len(x)):
        result = result + x[i]*w[i]    
    return (1 / (1+ exp(-(result+b))))

'''#calcul la vraisemblance comme dans le tme
# y et x sont des tableaux
def logvraisemblance (y,x,w,b):
    result = 0
    for i in range(len(y)):
        result = y[i]* log(f(x[i],w,b))+(1-y[i])*(log(1-f(x[i],w,b)))
    return result

# la variable x est une matrice et y est un tableau
#calcul la derivé du log selon wj    
def Lwj(y,x,w,b):
    wj = np.zeros(len(w))
    for j in range(len(w)):
        for i in range (len(y)):
            wj[j]= wj[j] + x[i][j]*(y[i]-f(x[i],w,b))
    return wj
    
    
    
#y est un vecteur , x est une matrice     
#calcul la derivé du log
def Lb(y,x,w,b):
    bresultat = 0
    for j in range (len(y)):
            bresultat= bresultat + (y[j]-f(x[j],w,b))
    return bresultat'''
    
def Lb_Lwj_L(x,y,w,b):
    n=len(x)
    nx=len(x[0])
    wj = np.zeros(nx)
    tf=np.zeros(n)
    bresultat = 0
    result = 0
    for i in range(n):
        tf[i]=f(x[i],w,b)
        bresultat=bresultat + (y[i]-tf[i])
        result =result + y[i]* log(tf[i])+(1-y[i])*(log(1-tf[i]))

    for j in range(nx):
        for i in range (n):
            wj[j]= wj[j] + x[i][j]*(y[i]-tf[i])
    return bresultat, wj, result
    
def classification(x, w, b):
    y=np.zeros(len(w))
    for i in range (len(w)):
        if(f (x[i], w , b)>0.5): y[i]=1
    else: y[i]=0
    return y
 
def iteration (x, y,w,b,epsilon, iteration):
    wj = w
    bresultat = b
    stock = np.zeros(iteration)
    for i in range (iteration):
        print i
        tmp = Lb_Lwj_L(x,y,wj,bresultat)
        wj = wj + epsilon* tmp[1]
        bresultat = bresultat + epsilon  *tmp[0]
        stock[i]= tmp[2]
        if i>1 and (stock[i-1]-stock[i])/stock[i-1]<0.001 : break
    return wj , bresultat, stock    
    
def initialisation(epsilon, taille):
    w = np.zeros(taille)
    for i in range( taille):
        w[i]= uniform(-1*epsilon, epsilon)
    b = uniform(-1*epsilon, epsilon)
    return w,b,epsilon
        
def learn (X,Y, n, epsilon, ite):
    thetaRL = []
    for i in range(n):
        Yc = np.where(Y==i,1.,0.)
        w,b,_= initialisation(epsilon,len(X[0]))
        thetaRL.append(iteration (X,Yc, w,b,epsilon,ite))
    return np.array(thetaRL)
######################################################################
#########################     script      ############################


# Données au format pickle: le fichier contient X, XT, Y et YT
# X et Y sont les données d'apprentissage; les matrices en T sont les données de test
data = pkl.load(file('usps_small.pkl','rb'))

X = data['X']
Y = data['Y']
XT = data['XT']
YT = data['YT']

print "taillex=",len(X), "  et taille y=", len(Y)
print len(X[0])
theta = learnGauss ( X,Y ) # apprentissage

logp  = logpobs(X, theta)  # application des modèles sur les données d'apprentissage
logpT = logpobs(XT, theta) # application des modèles sur les données de test

ypred  = logp.argmax(0)    # indice de la plus grande proba (colonne par colonne) = prédiction
ypredT = logpT.argmax(0)

print "Taux bonne classification en apprentissage : ",np.where(ypred != Y, 0.,1.).mean()
print "Taux bonne classification en test : ",np.where(ypredT != YT, 0.,1.).mean()

# Pour transformer le vecteur Y afin de traiter la classe 0:
'''Yc0 = np.where(Y==0,1.,0.)

w,b,epsilon = initialisation(0.0001,len(X[0]))
w ,b , liste = iteration (X,Yc0, w,b,epsilon,10)
p = plt.figure()
p = plt.plot (liste)
plt.show()'''


thetaRL = learn(X,Y,10, 0.0004, 10)

# si vos paramètres w et b, correspondant à chaque classe, sont stockés sur les lignes de thetaRL... Alors:

pRL  = np.array([[1./(1+np.exp(-x.dot(mod[0]) - mod[1])) for x in X] for mod in thetaRL ])
pRLT = np.array([[1./(1+np.exp(-x.dot(mod[0]) - mod[1])) for x in XT] for mod in thetaRL ])
ypred  = pRL.argmax(0)
ypredT = pRLT.argmax(0)
print "Taux bonne classification en apprentissage : ",np.where(ypred != Y, 0.,1.).mean()
print "Taux bonne classification en test : ",np.where(ypredT != YT, 0.,1.).mean()





