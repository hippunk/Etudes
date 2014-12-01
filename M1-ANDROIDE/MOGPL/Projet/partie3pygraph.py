# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 20:08:37 2014

@author: arthur
"""

from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph


from pygraph.algorithms.minmax import maximum_flow

import numpy as np   

def genUtils(M,N):
    u = np.ones((M,N))
    
    for i in range(M):
        for j in range(N):
            u[i][j]=np.round(np.random.triangular(0,M/2,M))
            
    return u

def calcMin(t):
    print t,min(t)

def calcRegr(u):
    for i in range(len(u)):
        u[i,:] -= min(u[i,:])
        
    for i in range(len(u[0])):
        u[:,i] -= min(u[:,i])
        
    return u
    
def majRegr(u,cuts):
    mini = 99999

    for i in range(len(u)):
        for j in range(len(u[0])):
            if(cuts[i+1] == 0 and cuts[len(u)+j+1] == 1 and u[i][j]<mini):
                mini =  u[i][j]           
        
    for i in range(len(u)):
        for j in range(len(u[0])):
            if(cuts[i+1] == 0 and cuts[len(u)+j+1] == 1):
                u[i][j]  -= mini     
            elif(cuts[i+1] == 1 and cuts[len(u)+j+1] == 0):
                u[i][j] += mini
    return u
#    return u
    

#N = np.random.random_integers(5,15)
N = 100
M = N
u = genUtils(M,N)
x = []
#u = np.array(([2,2,2,5,6],[2,5,1,0,7],[6,4,7,3,5],[5,3,3,7,0],[8,5,4,2,1]))
#u = [[2,0,0],[0,3,1],[0,1,0]]
sortie = 1

u = calcRegr(u)

while(sortie):
    # Graph creation
    cpt = 0
    gr = digraph()
    
    #Ajouts noeuds source et puit
    gr.add_nodes([0])
    gr.add_nodes([N+M+1])
    
    #ajouts noeuds agents et liens vers source
    for i in range(N):
        gr.add_nodes([i+1])
        gr.add_edge((0,i+1), wt=1)
        
    #ajouts noeuds objets et liens vers puit
    for i in range(M):
        gr.add_nodes([N+i+1])   
        gr.add_edge((N+i+1,N+M+1), wt=1)
        
        
    for i in range(N):
        for j in range(M):
            if(u[i][j]==0):
                gr.add_edge((i+1,N+j+1), wt=1)
            else:
                gr.add_edge((i+1,N+j+1), wt=0)
                
    #Sur cette partie, je pense qu'il y a un gros gain de complexité à faire sur 
    #la construction du graphe en ajoutant et retirant uniquement les arêtes concernées. 
    
    flows, cuts = maximum_flow(gr, 0, N+M+1)
    
    u = majRegr(u,cuts)
    
    
    for i in cuts:
            if(cuts[i] == 1):
                cpt += 1
    if(cpt == N+M+1):
        sortie = 0
        
    print sortie
    
print flows