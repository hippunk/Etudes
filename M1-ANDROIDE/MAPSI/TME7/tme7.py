# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 10:53:38 2014

@author: 3401924
"""

import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
"""
def discretise(X,d):
    intervalle = 360. / d
    tab = np.empty_like(X)
    for i in range(len(X)):
        for j in range(len(X[i])):
            tab[i][j] = np.floor(X[i][j]/intervalle)

    return tab
"""
    
def discretise(X,d):
    intervalle = 360. / d
    tab = []
    for i in X:
        tab.append(np.floor(i/intervalle))
    tab = np.array(tab)
    return tab

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

    Xtmp = np.array(Xtmp)
    return Xtmp   

def initGD(X,N):
    tab = []
    for i in range(len(X)):
        tab.append(np.floor(np.linspace(0,N-.00000001,len(X[i]))))
   
    tab = np.array(tab)
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

def learnHMM(allx, allq, N, K, initTo0=False):
    if initTo0:
        A = np.zeros((N,N))
        B = np.zeros((N,K))
        Pi = np.zeros(N)
    else:
        eps = 1e-8
        A = np.ones((N,N))*eps
        B = np.ones((N,K))*eps
        Pi = np.ones(N)*eps

    for i in range(0,len(allx)):
        Pi[find_Number(allx[i],0)]+=1
        maxi = find_max(allx[i])
        for l in range(0,maxi):
            A[find_Number(allx[i],l)][find_Number(allx[i],l+1)]+=1
         
    Pi = Pi/Pi.sum()
     
        
    A = A/np.maximum(A.sum(1).reshape(N,1),1) # normalisation

    return A,B,Pi


# truc pour un affichage plus convivial des matrices numpy
np.set_printoptions(precision=2, linewidth=320)
plt.close('all')

data = pkl.load(file("TME6_lettres.pkl","rb"))
X = np.array(data.get('letters'))
Y = np.array(data.get('labels'))

nCl = 26
N = 5
K = 10

Xd = discretise(X,N)


Xdisc = groupAllByDisc(Xd,N)

S = initGD(Xd,N)
A,B,Pi = learnHMM(Xdisc[Y=='a'],S[Y=='a'],N,K,True)

print Xdisc[0]
print "Pi: \n",Pi
print "A : \n",A
print "B : \n",B

#print X[6]
#print Xd[6]