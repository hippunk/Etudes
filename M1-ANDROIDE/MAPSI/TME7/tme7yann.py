# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 10:51:07 2014

@author: 3000892
"""

# -*- coding: utf-8 -*-

from pylab import *
from math import *
import numpy as np
import matplotlib.pyplot as plt
import pickle as pkl
from random import *


def discretise(X,d):
    intervalle=360./d
    nX=np.copy(X)
    for i in range(len(X)):
        nX[i]=np.floor(X[i]/intervalle)
    return nX
    
    
def initGD(X,N) :
    res = np.copy(X)
    for i in range(len(X)):
        res[i] = np.floor(np.linspace(0,N-.00000001,len(X[i])))
    return res

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
    
    cour=0
    for i in range(len(allx)):
        cour=allq[i][0]
        Pi[cour]=Pi[cour]+1
        B[allq[i][0]][allx[i][0]]=B[allq[i][0]][allx[i][0]]+1
        for j in range(1,len(allx[i])):
            B[allq[i][j]][allx[i][j]]=B[allq[i][j]][allx[i][j]]+1
            A[cour][allq[i][j]]=A[cour][allq[i][j]]+1
            cour=allq[i][j]
    A = A/np.maximum(A.sum(1).reshape(N,1),1) # normalisation
    B = B/np.maximum(B.sum(1).reshape(N,1),1) # normalisation
    Pi = Pi/Pi.sum()
    return (Pi,A,B)
    
def viterbi(x,Pi,A,B):
    sigma = np.zeros((len(x),len(A)))
    psi = np.zeros((len(x),len(A)))
    s= np.zeros(len(x))
    
    for i in range(len(A)):
        sigma[0][i]=log(Pi[i])+log(B[i][x[0]])
        psi[0][i]=-1
    
    for t in range(1,len(x)):
        for j in range(len(A)):
            maxi=-1000000000
            argi=0
            for i in range(len(A)):
                tmp=sigma[t-1][i]+log(A[i][j])
                if(tmp>maxi): 
                    maxi=tmp
                    argi=i
            sigma[t][j]=maxi+log(B[j][x[t]])
            psi[t][j]=argi

    
    S=-1000000000
    for i in range(len(A)):
        tmp=sigma[len(x)-1][i]
        if(tmp>S): 
            S=tmp
            s[len(x)-1]=i    

    for i in range(len(x)-2, -1, -1):
        s[i]= psi[i+1][s[i+1]]
        
    return (s, S)

def calc_log_pobs_v2(x,Pi, A, B):
    alpha = np.zeros((len(x),len(A)))
    s= np.zeros(len(x))
    omega=0
    for i in range(len(A)):
        alpha[0][i]=Pi[i]+B[i][x[0]]
        omega=omega+alpha[0][i]
    #alpha[0]= alpha[0]/omega   
    
    for t in range(1,len(x)):
        omega =0
        for j in range(len(A)):
            tmp=0
            for i in range(len(A)):
                tmp+=alpha[t-1][i]*A[i][j]
            alpha[t][j]=tmp*B[j][x[t]]
            omega=omega+alpha[t][j]
        #alpha[t]=alpha[t]/omega

    
    S=log(alpha[len(x)-1][0])
    for i in range(1,len(A)):
        tmp=alpha[len(x)-1][i]
        #S=S+alpha[len(x)-1][i]
        if(tmp>S): 
           S=tmp  
        
    return S
    
    
    
    
def BWsimp(X, N, K):
    q=initGD(X,N)
    Pi, A, B = learnHMM(X, q, N, K)
    L0=0
    L1=0
    v=[]
    
    for i in range(len(q)):
        q[i], _ = viterbi(X[i],Pi,A,B)
            
    for i in range(len(X)):
        L1+=log(Pi[q[i][0]])+log(B[q[i][0]][X[i][0]])
        for j in range(1,len(X[i])):
            L1+=log(A[q[i][j-1]][q[i][j]])+log(B[q[i][j]][X[i][j]])
    v.append(L1)
        
    while True:
        Pi, A, B = learnHMM(X, q, N, K)
        for i in range(len(q)):
            q[i], _ = viterbi(X[i],Pi,A,B)
        L0=L1
        for i in range(len(X)):
            L1+=log(Pi[q[i][0]])+log(B[q[i][0]][X[i][0]])
            for j in range(1,len(X[i])):
                L1+=log(A[q[i][j-1]][q[i][j]])+log(B[q[i][j]][X[i][j]])
        v.append(L1)
       
        if( (L0-L1)/L0<0.01): break
    return Pi, A, B, q, v

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
    
def generateHMM(P, A, B, n):
    x=np.zeros(n)
    q=np.zeros(n)
    r=random()
    i=0
    j=0
    N=len(A)
    K=len(B[0])
    for i in range(N):
        if(r<Pi[i]): 
            q[0]=i
            break
    
    
    r=random()
    for j in range(K):
        if(r<B[q[0]][j]): 
            x[0]=j
            break
    
    
    for i in range(1,n):
        r=random()
        for j in range(N):
            if(r<A[q[i-1]][j]): 
                q[i]=j
                break
        
        
        r=random()
        for j in range(K):
            if(r<B[q[i]][j]): 
                x[i]=j
                break
        
    return q, x

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

    
def groupByLabel( y):
    index = []
    for i in np.unique(y): # pour toutes les classes
        ind, = np.where(y==i)
        index.append(ind)
    return index

# truc pour un affichage plus convivial des matrices numpy
#np.set_printoptions(precision=2, linewidth=320)
#plt.close('all')

data = pkl.load(file("lettres.pkl","rb"))
X = np.array(data.get('letters'))
Y = np.array(data.get('labels'))

nCl = 26

K=500
N=10
Xd = discretise(X, K)
q = initGD(X,N)
q1 = initGD(X[Y=='a'],N)
print "q" ,q1
Pi, A, B = learnHMM(Xd[Y=='a'],q[Y=='a'],N,K)
 
"""print "Pi = ", Pi
print "A = ", A
print "B = ", B"""

s_est, p_est = viterbi(Xd[0], Pi, A, B)
p =  calc_log_pobs_v2(Xd[0],Pi, A, B)

tab_K = [3,10,20,50,100,500]
for ui  in range(6):
    print "K=",tab_K[ui]
    K = tab_K[ui]
    Xd = discretise(X, K)
    tab_val_ia = []
    tab_val_it = []
    nb_loop = 10
    for jk in range(nb_loop):
        itrain,itest = separeTrainTest(Y,0.8) 
        models = []   
        index = groupByLabel(Y)  # groupement des signaux par classe
        for cl in range(len(np.unique(Y))): # parcours de toutes les classes et optimisation des modèles
            models.append(BWsimp(Xd[itrain[cl]], N,K))   
        models=np.array(models)
        #Trois lettres générées pour 5 classes (A -> E)
        n = 3          # nb d'échantillon par classe
        nClred = 5   # nb de classes à considérer
        fig = plt.figure()
        
        
        
        ia = []
        for i in itrain:
            ia += i.tolist()    
        it = []
        for i in itest:
            it += i.tolist()
            
        probait = np.array([[viterbi(Xd[i], models[cl][0], models[cl][1], models[cl][2])[1] for i in it] for cl in range(len(np.unique(Y)))])
        probaia = np.array([[viterbi(Xd[i], models[cl][0], models[cl][1], models[cl][2])[1] for i in ia] for cl in range(len(np.unique(Y)))])
        
        Ynumit = np.zeros(Y[it].shape)
        for num,char in enumerate(np.unique(Y[it])):
            Ynumit[Y[it]==char] = num
            
        Ynumia = np.zeros(Y[ia].shape)
        for num,char in enumerate(np.unique(Y[ia])):
            Ynumia[Y[ia]==char] = num
            
            
        predia = probaia.argmax(0) # max colonne par colonne
        predit = probait.argmax(0) # max colonne par colonne
        
        tab_val_ia.append(np.where(predia != Ynumia, 0.,1.).mean())
        tab_val_it.append(np.where(predit != Ynumit, 0.,1.).mean())
    
    print tab_val_ia
    print tab_val_it
    
    tab_val_ia = np.array(tab_val_ia)
    tab_val_it = np.array(tab_val_it)
    
    moy_ia = np.sum(tab_val_ia) / nb_loop
    moy_it = np.sum(tab_val_it) /nb_loop
    print "Moy: ia=", moy_ia,"it=", moy_it
    sommeia =0
    sommeit =0
    for jk in range(nb_loop):
        sommeia += (tab_val_ia[jk] - moy_ia)**2
        sommeit += (tab_val_it[jk] - moy_it)**2
        
    sommeia = math.sqrt(sommeia / nb_loop)
    sommeit = math.sqrt(sommeit /nb_loop)

    print "ecart-type ia=",sommeia,"it=",sommeit

for cl in xrange(nClred):
    Pic = models[cl][0].cumsum() # calcul des sommes cumulées pour gagner du temps
    Ac = models[cl][1].cumsum(1)
    Bc = models[cl][2].cumsum(1)
    long = np.floor(np.array([len(x) for x in Xd[itrain[cl]]]).mean()) # longueur de seq. à générer = moyenne des observations
    for im in range(n):
        s,x = generateHMM(Pic, Ac, Bc, int(long))
        intervalle = 360./K  # pour passer des états => angles
        newa_continu = np.array([i*intervalle for i in x]) # conv int => double
        sfig = plt.subplot(nClred,n,im+n*cl+1)
        sfig.axes.get_xaxis().set_visible(False)
        sfig.axes.get_yaxis().set_visible(False)
        tracerLettre(newa_continu)
plt.show()

#plt.savefig("lettres_hmm.png")
"""
print BWsimp(Xd[index[0]], N, K)
print "s_est =", s_est
print "p_est =", p_est
print "p =", p
"""