# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 15:19:03 2014

@author: arthur
"""

from gurobipy import *
import numpy as np    

def genUtils(M,N):
    u = np.ones((M,N))
    
    for i in range(N):
        for j in range(M):
            u[i][j]=np.round(np.random.triangular(0,M/2,M))
            
    return u

def maxzi(u):
    ret=np.zeros(1,len(u))
    
    for i in range(len(u)):
        
        for j in range(len(u[i])):
            if(ret[i]<u[i][j]):
                ret[i]=u[i][j]
    return ret
#N = np.random.random_integers(5,15)
N = 100
M = N

u = genUtils(M,N)
zi=maxzi(u)
x = []
print u
         

m = Model("prjMogpl")     

for i in range(N):
    tmp = []
    for j in range(M):
        name = "x"+str(i)+","+str(j)
        tmp.append(m.addVar(vtype=GRB.BINARY, name=name))
    x.append(tmp)
y = m.addVar(vtype=GRB.CONTINUOUS, name="y")
m.update() 
       
obj = LinExpr()
obj = 0       

obj += y
        
m.setObjective(obj,GRB.MINIMIZE)

for i in range(N):
    n.addConstr(y-(zi[i]-quicksum(x[i][j]*u[i][j] for j in range(M)))>=0,"contrainte%d" % i)

for i in range(N):
    m.addConstr(quicksum(x[i][j] for j in range(M))==1,"contrainte%d" % i)
    
for j in range(M):
    m.addConstr(quicksum(x[i][j] for i in range(N))==1,"contrainte%d" % (N+j))

m.optimize()
"""
print ""
print "Liste des objets :"
print u 
print 'Solution optimale : '
for i in range(N):
    for j in range(M):
        print 'x'+str(i)+str(j), '=', x[i][j].x
print ""
print 'Valeur de la fonction objectif :', m.objVal
"""