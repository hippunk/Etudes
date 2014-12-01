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

#N = np.random.random_integers(5,15)
N = 10
M = N
e=0.00001
y = 16
u = genUtils(M,N)
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

print "obj : ",y
        
m.setObjective(obj,GRB.MAXIMIZE)

for i in range(N):
    m.addConstr(quicksum(x[i][j]*u[i][j] for j in range(M))-y>=0
						,"contrainte%d" % i)
    
for i in range(N):
    m.addConstr(quicksum(x[i][j] for j in range(M))==1
						,"contrainte%d" % (N+i))    
    
for j in range(M):
    m.addConstr(quicksum(x[i][j] for i in range(N))==1
						,"contrainte%d" % (2*N+j))

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
