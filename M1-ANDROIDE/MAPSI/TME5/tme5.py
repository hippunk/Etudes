# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 16:03:07 2014

@author: 3401924
"""
import pydot        
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.stats as stats


# etant donné une BD data et son dictionnaire, cette fonction crée le
# tableau de contingence de (x,y) | z
def create_contingency_table ( data, dico, x, y, z ):
    # détermination de la taille de z
    size_z = 1
    offset_z = np.zeros ( len ( z ) )
    j = 0
    for i in z:
        offset_z[j] = size_z      
        size_z *= len ( dico[i] )
        j += 1

    # création du tableau de contingence
    res = np.zeros ( size_z, dtype = object )

    # remplissage du tableau de contingence
    if size_z != 1:
        z_values = np.apply_along_axis ( lambda val_z : val_z.dot ( offset_z ),
                                         1, data[z,:].T )
        i = 0
        while i < size_z:
            indices, = np.where ( z_values == i )
            a,b,c = np.histogram2d ( data[x,indices], data[y,indices],
                                     bins = [ len ( dico[x] ), len (dico[y] ) ] )
            res[i] = ( indices.size, a )
            i += 1
    else:
        a,b,c = np.histogram2d ( data[x,:], data[y,:],
                                 bins = [ len ( dico[x] ), len (dico[y] ) ] )
        res[0] = ( data.shape[1], a )
    return res

# fonction pour transformer les données brutes en nombres de 0 à n-1
def translate_data ( data ):
    # création des structures de données à retourner
    nb_variables = data.shape[0]
    nb_observations = data.shape[1] - 1 # - nom variable
    res_data = np.zeros ( (nb_variables, nb_observations ), int )
    res_dico = np.empty ( nb_variables, dtype=object )

    # pour chaque variable, faire la traduction
    for i in range ( nb_variables ):
        res_dico[i] = {}
        index = 0
        for j in range ( 1, nb_observations + 1 ):
            # si l'observation n'existe pas dans le dictionnaire, la rajouter
            if data[i,j] not in res_dico[i]:
                res_dico[i].update ( { data[i,j] : index } )
                index += 1
            # rajouter la traduction dans le tableau de données à retourner
            res_data[i,j-1] = res_dico[i][data[i,j]]
    return ( res_data, res_dico )


# fonction pour lire les données de la base d'apprentissage
def read_csv ( filename ):
    data = np.loadtxt ( filename, delimiter=',', dtype='S' ).T
    names = data[:,0].copy ()
    data, dico = translate_data ( data )
    return names, data, dico
    
def sufficient_statistics ( data, dico, x, y, z ):
    res = create_contingency_table ( data, dico, x, y, z)
    zlen = len(res)
    #print(res[0][1][0,:])
    #print(res[0][1][1,:])
    #print(dico)
    nBz = 0
    total = 0
    #print(x)
    for z in range(0,zlen):
       if(res[z][0] != 0):
           nBz+=1
       xlen = len(res[z])
       for x in range(0,xlen):
           #print "z,x : ",z,x

           #print res[0][1][1]
           resZ1 = res[z][1]
           #print "xlen",resZ1[1]
           
           ylen = len(resZ1[x])
           for y in range(0,ylen):
               Nxyz = res[z][1][x][y]
               Nxz = sum(res[z][1][x,:])
               Nyz = sum(res[z][1][:,y])
               Nz = res[z][0]
               #print("Ligne : ",res[z])
               #print("x : ",x," y : ",y," z :",z)
               #print("Nxyz : ",Nxyz," Nxz : ",Nxz," Nyz : ",Nyz," Nz :",Nz)
               num = 0
               denom = 0
               result = 0
               if(Nz != 0):
                   num = (Nxyz - (Nxz*Nyz/Nz))**2 
                   denom = Nxz*Nyz/Nz
               
               if(denom != 0):
                   result = num/denom
                   #print(result)
                   total += result
    dof = nBz*(len(res[0][1][0,:])-1)*(len(res[0][1][:,0])-1)
    return(total,dof)
        
def indep_score( data, dico, x, y, z ):
    x2,DoF = sufficient_statistics ( data, dico, x, y, z )
    res = create_contingency_table ( data, dico, x, y, z)
    dMin = 5*len(res[0][1][0,:])*len(res[0][1][:,0])*len(res[0])
    #print("dmin :",dMin)
    if(len(data[0]) < dMin):
        print("prout")
        result = (-1,1)    
    else:
        result = stats.chi2.sf ( x2, DoF )
    return result

def best_candidate ( data, dico, x, z, alpha ):
    best = 100000000
    bestY = []
    for y in range(0,x):
        tmp = indep_score( data, dico, x, y, z )
        if(tmp <= alpha and tmp < best):
            best = tmp
            bestY = [y]
    return bestY
    
def create_parents ( data, dico, x, alpha ):
    y = 0
    z = []
    while(y != []):
        y = best_candidate ( data, dico, x, z, alpha )
        z+=y
    return z
    
def learn_BN_structure ( data, dico, alpha ):
    list = []
    for i in range(0,len(data)):
        x = create_parents( data, dico, i,alpha)
        list.append(x)
    print "learn_BN_structure",list
    return(list)
        
def display_BN ( node_names, bn_struct, bn_name, style ):
    graph = pydot.Dot( bn_name, graph_type='digraph')

    # création des noeuds du réseau
    for name in node_names:
        new_node = pydot.Node( name, 
                               style="filled",
                               fillcolor=style["bgcolor"],
                               fontcolor=style["fgcolor"] )
        graph.add_node( new_node )

    # création des arcs
    for node in range ( len ( node_names ) ):
        parents = bn_struct[node]
        for par in parents:
            new_edge = pydot.Edge ( node_names[par], node_names[node] )
            graph.add_edge ( new_edge )

    # sauvegarde et affaichage
    outfile = bn_name + '.png'
    graph.write_png( outfile )
    img = mpimg.imread ( outfile )
    plt.imshow( img )
    
names,data,dico = read_csv("2014_tme5_alarm.csv")

style = { "bgcolor" : "#6b85d1", "fgcolor" : "#FFFFFF" }
resultats = learn_BN_structure( data, dico, 0.05)

display_BN(names,resultats,"Asia",style)
