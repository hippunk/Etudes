# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 10:55:18 2014

@author: 3100208
"""

import numpy as np
import pickle as pkl
from math import *

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

######################################################################
######################### code rajouter ##############################

def f ( x, w, b):
    return (1 / (1 + exp(-(np.dot(x ,w) + b))))
    
def log_vraisemblance(x,y,w,b):
    somme = 0
    result = f(x,w,b)
    for i in range(0,len(y)):
        Y = y[i]
        somme += Y*log(result) +(1-Y)*log((1 - result))
    return somme

def derive_log_vrai(x,y,w,b):
    dwj = np.zeros(len(w))
    db = 0
    for i in range(0,len(x)):
        aux = y[i] - f(x,w,b)
        db += aux
        dwj[i] += x[i] * aux
          
    ## Tu peux améliorer ce qui suit si tu veux ##
    tab = np.zeros(2,dtype=object)
    tab[0] = dwj
    tab[1] = db    
    return tab
          


######################################################################
#########################     script      ############################


# Données au format pickle: le fichier contient X, XT, Y et YT
# X et Y sont les données d'apprentissage; les matrices en T sont les données de test
data = pkl.load(file('usps_small.pkl','rb'))

X = data['X']
Y = data['Y']
XT = data['XT']
YT = data['YT']

theta = learnGauss ( X,Y ) # apprentissage

logp  = logpobs(X, theta)  # application des modèles sur les données d'apprentissage
logpT = logpobs(XT, theta) # application des modèles sur les données de test

ypred  = logp.argmax(0)    # indice de la plus grande proba (colonne par colonne) = prédiction
ypredT = logpT.argmax(0)

print "Taux bonne classification en apprentissage : ",np.where(ypred != Y, 0.,1.).mean()
print "Taux bonne classification en test : ",np.where(ypredT != YT, 0.,1.).mean()

epsilon = 0.00005

###################### Apprentissage d'un modele binaire ######################
alpha = []

## Initialisation ##
w0 = (1 + 1)*np.random.sample(len(X[0])) -1 # [0,*1[
b0 =    np.random.sample() * epsilon
alpha0 = [w0,b0]
alpha.append(alpha0)
#print alpha
#print w0

for i in range(0, len(X[0])):
    w0[i] = w0[i] *epsilon

tab_vrai = []    
## Recursion ##
i=0
encore = True
while(encore):
#for i in range(0):
    v = log_vraisemblance(X[i],Y,alpha[i][0],alpha[i][1])
    tab_vrai.append(v)
    #print "v",v
    tab_result_derive = derive_log_vrai(X[i],Y,alpha[i][0],alpha[i][1]) 
    #print "d",len(tab_result_derive[0]),"b",tab_result_derive[1]
    
    ## Mise à  jour de b ##    
    bi = alpha[i][1] + epsilon * tab_result_derive[1]
    #print "bi",bi
    
    ## Mise à jour de w ##
    walpha = alpha[i][0]
    wi = np.zeros(len(walpha))
    for j in range(len(walpha)):
       wi[j] = walpha[j] + epsilon * tab_result_derive[0][j]
    alpha.append(tab_result_derive)
    
    ## Calcul de la convergence ##
    k = 1
    if i>0:
        k = tab_vrai[i] - tab_vrai[i-1]/tab_vrai[i]
        print "k",k
    if k <= 0.0001 or i > 100 :
        encore = False
    i += 1
    
print "Fin"
 
print tab_vrai 

############ Paradigme un-contre-tous pour le passage au multi-classe #########
Yc = np.zeros(10,dtype=object)
for i in range(10): #il y a 10 cases dans le problème
    Yc[i] = np.where(Y==i,1.,0.)
    
print Yc[0]
print Yc[1]

thetaRL = np.zeros(10,dtype=object)
for i in range(10):
    thetaRL[i] = learnGauss ( X,Yc[i] ) 

fc = np.zeros(10)
for i in range(10):
    fc[i] = f(X[i],thetaRL[i][0][0],theta[i][0][1])
print fc

"""
# si vos paramètres w et b, correspondant à chaque classe, sont stockés sur les lignes de thetaRL... Alors:
pRL  = np.array([[1./(1+np.exp(-x.dot(mod[0][0]) - mod[0][1])) for x in X] for mod in thetaRL ])
pRLT = np.array([[1./(1+np.exp(-x.dot(mod[0][0]) - mod[0][1])) for x in XT] for mod in thetaRL ])
print pRL[0]
ypred  = pRL.argmax(0)
ypredT = pRLT.argmax(0)
print "ypred : ",ypred
print "Taux bonne classification en apprentissage : ",np.where(ypred != Y[Y==0], 0.,1.).mean()
print "Taux bonne classification en test : ",np.where(ypredT != YT, 0.,1.).mean()
"""

#print w0
#print "X ",len(X[0]) #xi = ligne
#print "\nY ",len(Y) #yi = chiffre correspondant
#print "\nXT ", XT #T = test
#print "\nYT ", YT
#print "\ntheta ", theta[0] #(mu,sigma²)
#print "\nlogp ",logp 
#print "\nlogpT", logpT
#print "\nypred ",ypred
#print "\nypredT ", ypredT



