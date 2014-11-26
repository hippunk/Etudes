# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 10:53:38 2014

@author: 3401924
"""

import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
from math import *

    
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
        
    for i in range(0,len(allq)):
      #Calcul de PI
      Pi[allq[i][0]] += 1
      
      #Calcul de A
      ind = 0
      while(1):
          if ind == len(allq[i]) - 1:
              break
          A[allq[i][ind]][allq[i][ind+1]] += 1
          ind += 1
          
      for j in range(0,len(allx[i])):
          B[allq[i][j]][allx[i][j]] += 1
         
    Pi = Pi/Pi.sum()
    for i in range(0,N):
        somme = B[i].sum()
        for j in range(0,K):
            B[i][j] /= somme
        
    A = A/np.maximum(A.sum(1).reshape(N,1),1) # normalisation

    return A,B,Pi
"""
def viterbi(x,Pi,A,B):
    s_est = []
    p_est = 0.0
    T = 10    
        
    #Initialisation
    for i in range(0,len(Pi)):
        aux = log(Pi[i]) + log(B[i][1]) # je ne suis pas sûr sur les indices de B
        s_est.append(aux)
    p_est = -1
    
    #Recursion    
    delta_max = -1
    for i in range(0,len(s_est)): #recherche du max des delta t-1
        if(s_est[i] > delta_max):
            delta_max = s_est[i]
            
    argmaxi = np.argmax(s_est)
    for i in range(0,len(Pi)):
        for j in range(0,T-1):
            
    
    return s_est, p_est
 """
 
""" 
def viterbi(x,Pi,A,B):
    s_est = []
    p_est = 0.0
    
    N = len(B)   
    tx = len(x)
    
    #Initialisation
    sigma = np.zeros((N,tx))
    temps = 0
    
    for i in range(0,N):       
        sigma[i][temps] = log(Pi[i]) + log(B[i][x[0]])
    temps += 1
    
    #Recursion
    while(temps != tx):
        for i in range(0,N):
            if i == 0:
                maxi = sigma[0][temps-1]
                indice = 0
            if maxi < sigma[i][temps-1]:
                maxi = sigma[i][temps-1]
                indice = i
        s_est.append(indice)
        for i in range(0,N):
            sigma[i][temps] = maxi + log(A[indice][i]) + log(B[i][x[temps]])
        temps += 1
    maxi = sigma[0][temps-1]
    indice = 0
    for i in range(0,N):
        if maxi < sigma[i][temps-1]:
            maxi = sigma[i][temps-1]            
            indice = i
    s_est.append(indice)
    p_est = maxi
    
    return s_est, p_est
"""
def maxni(tab):
    i = 0
    maxi = -999999   
    
    for n in range(0,len(tab)) :
        if(tab[n] > maxi):
            maxi = tab[n]
            i = n
            
        
        
    
    return maxi,i

def viterbi(x,Pi,A,B):

    lenpi = len(Pi)    
    
    S1 = np.zeros(lenpi)
    S2 = np.zeros(lenpi)
    
    P1 = np.zeros(lenpi)
    P2 = np.zeros(lenpi)
    
    #Init
    for i in range(lenpi):
        S1[i] = log(Pi[i]) + log(B[i][0])
        P1[i] = -1   

    for j in range(len(x)):
        for i in range(lenpi):
            tmp,ind = maxni(S1)
            S2[i] = tmp+log(A[ind][i])+log(B[i][x[j]])

    print S2
    return 1,1
        
   
# truc pour un affichage plus convivial des matrices numpy
np.set_printoptions(precision=2, linewidth=320)
plt.close('all')

data = pkl.load(file("TME6_lettres.pkl","rb"))
X = np.array(data.get('letters'))
Y = np.array(data.get('labels'))

nCl = 26
N = 5
K = 10

Xd = discretise(X,K)

#Xdisc = groupAllByDisc(Xd,N)
#print "Xd : " ,Xd
S = initGD(Xd,N)
#print S[0]
#print Xd[Y == 'a'][1]
#print Xdisc[Y == 'a'][1]
#print S[Y == 'a'][1]
A1,B1,Pi1 = learnHMM(Xd[Y=='a'],S[Y=='a'],N,K,True)
A,B,Pi = learnHMM(Xd[Y=='a'],S[Y=='a'],N,K)

#print Xdisc[0]
print "Pi: \n",Pi1
print "A : \n",A1
print "B : \n",B1

s_est, p_est = viterbi(Xd[0],Pi,A,B)

#print "s_est = ", s_est
#print "p_est = ", p_est


"""
#Baum-Welch simplifié
tab_lettre = np.unique(Y)
#print tab_lettre
tab_alpha = np.zeros((len(tab_lettre),3),dtype=object)
vrai = 0.000000000000000001
nb_tour = 0
courbe =[]
aux = []
while(1):
    for i in range(0,len(tab_lettre)):
        tab_alpha[i] = learnHMM(Xd[Y==tab_lettre[i]],S[Y==tab_lettre[i]],N,K)    
    
    vrai_k = 0.00000000000000000000001
    for lettre in range(0,len(tab_lettre)-1):
        for i in range(0,len(Xd)-1):
            s_est,p_est = viterbi(Xd[i],tab_alpha[lettre][2],tab_alpha[lettre][0],tab_alpha[lettre][1])
            vrai_k += p_est
    
    if nb_tour == 0:
        vrai = vrai_k
    else:
        auxi = (vrai - vrai_k) / vrai
        print auxi   
        if auxi <= 0.0001:
            courbe.append(vrai_k)
            break;
    courbe.append(vrai_k)
    nb_tour += 1
    
    
print "FIN " , vrai_k
print courbe
print aux
        

#print X[6]
#print Xd[6]
"""