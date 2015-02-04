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

def viterbi(x,Pi,A,B):
    N = len(A)
    tx = len(x)
    
    s_est = np.zeros(tx)
    sigma = np.zeros((tx, N))
    psi = np.zeros((tx, N))
    
    #Initialisation
    for i in range(N):
        sigma[0][i] = log(Pi[i]) + log(B[i][x[0]])
        psi[0][i] = -1
    
    #Recursion
    for temps in range(1,tx):
        for j in range(N):
            maxi = sigma[temps-1][0] + log(A[0][j])
            argind = 0
            for i in range(1,N):
                tmp = sigma[temps-1][i] + log(A[i][j])
                if(tmp > maxi):
                    maxi = tmp
                    argind = i
            sigma[temps][j] = maxi + log(B[j][x[temps]])
            psi[temps][j] = argind
            
    p_est = -1000000000
    for i in range(N):
        tmp = sigma[tx-1][i]
        if(tmp > p_est):
            p_est = tmp
            s_est[tx-1] = i            
           
    for i in range(tx-2,-1,-1):
        s_est[i] = psi[i+1][s_est[i+1]]
    
    return s_est, p_est
"""
def viterbi(x,Pi,A,B):
    s_est = []
    p_est = 0
    
    N= len(B)
    tx = len(x)
    #Initialisation
    sigma = np.zeros((tx,N))
    
    for i in range(0,N):
        sigma[0][i] = log(Pi[i]) + log(B[i][x[0]])
    
    #Recursion
    temps = 1
    while(temps < tx):
        for j in range(N):
            tmp = np.zeros(N)
            for i in range(N):
                tmp[i] = sigma[temps-1][i] + log(A[i][j])
            maxi = np.max(tmp)
            
            sigma[temps][j] = maxi  + log(B[j][x[temps]])
        s_est.append(np.argmax(sigma[temps-1]))
        
        temps += 1    
    s_est.append(np.argmax(sigma[temps-1]))
    p_est = np.max(sigma[temps-1])
    return s_est, p_est
"""    
def calc_log_pobs_v2(x,Pi,A,B):
    prob = 0
    
    N = len(B)   
    tx = len(x)
    
    #Initialisation
    alpha = np.zeros((N,tx))
    temps = 0
    
    for i in range(0,N):       
        alpha[i][temps] = Pi[i] * B[i][x[0]]
    temps += 1

    #Récursion
    while(temps != tx):
        for i in range(0,N):
            for j in range(0,N):
                alpha[i][temps] += (alpha[j][temps - 1] * A[j][i]) * B[i][x[temps]]
        temps += 1
        
    for i in range(0,N):
        prob += alpha[i][temps-1]
 
    return log(prob)



def Baum_Welch_simplifie(X,N,K):
    S = initGD(Xd,N)
    vrai = []
    useless = -1
    vrai_aux1 = 0
    vrai_aux2 = 0
    #Initialisation des états cachés arbitraire
    A,B,Pi = learnHMM(Xd,S,N,K)
    
    for i in range(len(S)):
        S[i],useless = viterbi(X[i],Pi,A,B)
    
    for i in range(len(X)):
        vrai_aux1 += log(Pi[S[i][0]]) + log(B[S[i][0]][X[i][0]])
        for j in range(1,len(X[i])):
            vrai_aux1 += log(A[S[i][j-1]][S[i][j]]) + log(B[S[i][j]][X[i][j]])
    vrai.append(vrai_aux1)
    
    #Recursion    
    while(True):
        A,B,Pi = learnHMM(Xd,S,N,K)
        for i in range(len(S)):
            S[i],useless = viterbi(X[i],Pi,A,B)
            
        vrai_aux2 = vrai_aux1
        for i in range(len(X)):
            vrai_aux1 += log(Pi[S[i][0]]) + log(B[S[i][0]][X[i][0]])
            for j in range(1,len(X[i])):
                vrai_aux1 += log(A[S[i][j-1]][S[i][j]]) + log(B[S[i][j]][X[i][j]])
                
        vrai.append(vrai_aux1)
        
        vraisemblance = (vrai_aux2 - vrai_aux1) / vrai_aux2
        print "vrai",vraisemblance
        if vraisemblance < 0.0001 :
            break
            
    return Pi,A,B,S,vrai

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

# affichage d'une lettre (= vérification bon chargement)
def tracerLettre(let):
    a = -let*np.pi/180;
    coord = np.array([[0, 0]]);
    for i in range(len(a)):
        x = np.array([[1, 0]]);
        rot = np.array([[np.cos(a[i]), -np.sin(a[i])],[ np.sin(a[i]),np.cos(a[i])]])
        xr = x.dot(rot) # application de la rotation
        coord = np.vstack((coord,xr+coord[-1,:]))
    plt.plot(coord[:,0],coord[:,1])
    return


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

print "s_est = ", s_est
print "p_est = ", p_est

prob = calc_log_pobs_v2(Xd[0],Pi,A,B)

print "prob :", prob
"""print Baum_Welch_simplifie(Xd,N,K)

#Trois lettres générées pour 5 classes (A -> E)
n = 3          # nb d'échantillon par classe
nClred = 5   # nb de classes à considérer
fig = plt.figure()
for cl in xrange(nClred):
    Pic = models[cl][0].cumsum() # calcul des sommes cumulées pour gagner du temps
    Ac = models[cl][1].cumsum(1)
    Bc = models[cl][2].cumsum(1)
    long = np.floor(np.array([len(x) for x in Xd[itrain[cl]]]).mean()) # longueur de seq. à générer = moyenne des observations
    for im in range(n):
        s,x = generateHMM(Pic, Ac, Bc, int(long))
        intervalle = 360./d  # pour passer des états => angles
        newa_continu = np.array([i*intervalle for i in x]) # conv int => double
        sfig = plt.subplot(nClred,n,im+n*cl+1)
        sfig.axes.get_xaxis().set_visible(False)
        sfig.axes.get_yaxis().set_visible(False)
        tracerLettre(newa_continu)
plt.savefig("lettres_hmm.png")
"""