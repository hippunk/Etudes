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
    
    for i in range(N):
        for j in range(M):
            u[i][j]=np.round(np.random.triangular(0,M/2,M))
            
    return u

#N = np.random.random_integers(5,15)
N = 3
M = N
u = genUtils(M,N)
x = []
#u = [[2,0,0],[0,3,1],[0,1,0]]
lmb = 0
sortie = 1
#print u

# Graph creation
while(sortie):
    gr = digraph()
    
    gr.add_nodes([0])
    gr.add_nodes([N+M+1])
    
    for i in range(N):
        gr.add_nodes([i+1])
        gr.add_edge((0,i+1), wt=1)
        
    for i in range(M):
        gr.add_nodes([N+i+1])   
        gr.add_edge((N+i+1,N+M+1), wt=1)
        
    for i in range(N):
        for j in range(M):
            if(u[i][j]>=lmb):
                gr.add_edge((i+1,N+j+1), wt=1)
            else:
                gr.add_edge((i+1,N+j+1), wt=0)
    
    flows, cuts = maximum_flow(gr, 0, N+M+1)
    

    
    for i in range(N):
        k=0
        for j in range(M):
            if(flows[(i+1,N+j+1)]==0):
                k+=1
        if(k==N):
            sortie = 0
            
    if(sortie == 1):
        oldflow = flows
    lmb += 1
    
print u
print oldflow
