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
import matplotlib.animation as animation

def read_file ( filename ):
    """
    Lit le fichier contenant les données du geyser Old Faithful
    """
    # lecture de l'en-tête
    infile = open ( filename, "r" )
    for ligne in infile:
        if ligne.find ( "eruptions waiting" ) != -1:
            break

    # ici, on a la liste des temps d'éruption et des délais d'irruptions
    data = []
    for ligne in infile:
        nb_ligne, eruption, waiting = [ float (x) for x in ligne.split () ]
        data.append ( eruption )
        data.append ( waiting )
    infile.close ()

    # transformation de la liste en tableau 2D
    data = np.asarray ( data )
    data.shape = (data.size / 2, 2 )

    return data
"""    
def params_calc(data):
    tab = {"muX":0,"muZ":0}
    longueur = len(data)
    
    #moyenne
    for i in data:
        tab["muX"] += (i[0]*1/longueur)
        tab["muZ"] += (i[1]*1/longueur)
        
    print(tab["muX"],tab["muZ"])
    
    #variance
    for i in data:
        tab["muX"] += ((i[0]-tab["muX"])**2)1/longueur
        tab["muZ"] += ((i[1]-tab["muZ"])**2)1/longueur
"""

def dessine_normales ( data, params, weights, bounds, ax ):
    # récupération des paramètres
    mu_x0, mu_z0, sigma_x0, sigma_z0, rho0 = params[0]
    mu_x1, mu_z1, sigma_x1, sigma_z1, rho1 = params[1]

    # on détermine les coordonnées des coins de la figure
    x_min = bounds[0]
    x_max = bounds[1]
    z_min = bounds[2]
    z_max = bounds[3]

    # création de la grille
    nb_x = nb_z = 100
    x = np.linspace ( x_min, x_max, nb_x )
    z = np.linspace ( z_min, z_max, nb_z )
    X, Z = np.meshgrid(x, z)

    # calcul des normales
    norm0 = np.zeros ( (nb_x,nb_z) )
    for j in range ( nb_z ):
        for i in range ( nb_x ):
            norm0[j,i] = normale_bidim ( x[i], z[j], params[0] )# * weights[0]
    norm1 = np.zeros ( (nb_x,nb_z) )
    for j in range ( nb_z ):
        for i in range ( nb_x ):
             norm1[j,i] = normale_bidim ( x[i], z[j], params[1] )# * weights[1]

    # affichages des normales et des points du dataset
    ax.contour ( X, Z, norm0, cmap=cm.winter, alpha = 0.5 )
    ax.contour ( X, Z, norm1, cmap=cm.autumn, alpha = 0.5 )
    for point in data:
        ax.plot ( point[0], point[1], 'k+' )


def find_bounds ( data, params ):
    # récupération des paramètres
    mu_x0, mu_z0, sigma_x0, sigma_z0, rho0 = params[0]
    mu_x1, mu_z1, sigma_x1, sigma_z1, rho1 = params[1]

    # calcul des coins
    x_min = min ( mu_x0 - 2 * sigma_x0, mu_x1 - 2 * sigma_x1, data[:,0].min() )
    x_max = max ( mu_x0 + 2 * sigma_x0, mu_x1 + 2 * sigma_x1, data[:,0].max() )
    z_min = min ( mu_z0 - 2 * sigma_z0, mu_z1 - 2 * sigma_z1, data[:,1].min() )
    z_max = max ( mu_z0 + 2 * sigma_z0, mu_z1 + 2 * sigma_z1, data[:,1].max() )

    return ( x_min, x_max, z_min, z_max )
    
    
def normale_bidim(x,z,params):
    A = 1.0 / (2 * math.pi*params[2]*params[3]* math.sqrt(1 - (params[4]**2))) 
    B = (-1.0 / ( 2* ( 1-(params[4]**2))))
    C = 1.0*((x - params[0])/ params[2])**2
    D = -2.0*params[4] * (x - params[0])*(z -params[1]) / (params[2] *params[3])
    E = 1.0*((z- params[1])/params[3])**2
    return 1.0 *A * math.exp ( B* ( C + D + E ))    



def dessine_1_normale ( params ):
    # récupération des paramètres
    mu_x, mu_z, sigma_x, sigma_z, rho = params

    # on détermine les coordonnées des coins de la figure
    x_min = mu_x - 2 * sigma_x
    x_max = mu_x + 2 * sigma_x
    z_min = mu_z - 2 * sigma_z
    z_max = mu_z + 2 * sigma_z

    # création de la grille
    x = np.linspace ( x_min, x_max, 100 )
    z = np.linspace ( z_min, z_max, 100 )
    X, Z = np.meshgrid(x, z)

    # calcul des normales
    norm = X.copy ()
    for i in range ( x.shape[0] ):
        for j in range ( z.shape[0] ):
            norm[i,j] = normale_bidim ( x[i], z[j], params )

    # affichage
    fig = plt.figure ()
    plt.contour ( X, Z, norm, cmap=cm.autumn )
    plt.show ()    
    
def Q_i(data,current_params,current_weights):
    result = np.zeros((len(data),2))
    
    vra1 = 0
    vra2 = 0

    for i in range (0,len(data)):
        result[i][0] = 1.0*normale_bidim(data[i][0],data[i][1],current_params[0]) * 1.0*current_weights[0]
        result[i][1] = 1.0*normale_bidim(data[i][0],data[i][1],current_params[1]) * 1.0*current_weights[1]
        temp = result[i][1] + result[i][0]
    

        if(result[i][0] != 0):
            vra1 += math.log(result[i][0])
        else:
            vra1 += -100000000
        if(result[i][1] != 0):
            vra2 += math.log(result[i][1])    
        else:
            vra2 += -100000000    
        
        result[i][0] /=  temp
        result[i][1] /=  temp
    

        
    return result,vra1,vra2
    
def M_step( data, Q, current_params, current_weights ):
    mu_x0, mu_z0, sigma_x0, sigma_z0, rho0 = params[0]
    mu_x1, mu_z1, sigma_x1, sigma_z1, rho1 = params[1]
        
    pi0 = sum(Q[:,0])/sum(Q[:,0]+Q[:,1])
    pi1 = sum(Q[:,1])/sum(Q[:,0]+Q[:,1])
    
    muX0 = sum(Q[:,0]*data[:,0])/sum(Q[:,0])
    muX1 = sum(Q[:,1]*data[:,0])/sum(Q[:,1])
    
    muZ0 = sum(Q[:,0]*data[:,1])/sum(Q[:,0])
    muZ1 = sum(Q[:,1]*data[:,1])/sum(Q[:,1])

    varX0 = (sum(Q[:,0]*(1.0*data[:,0]-mu_x0)**2))/sum(Q[:,0])
    varX1 = (sum(Q[:,1]*(1.0*data[:,0]-mu_x1)**2))/sum(Q[:,1])
        
    varZ0 = (sum(Q[:,0]*(1.0*data[:,1]-mu_z0)**2))/sum(Q[:,0])
    varZ1 = (sum(Q[:,1]*(1.0*data[:,1]-mu_z1)**2))/sum(Q[:,1])
    
    sigmaX0 = math.sqrt(varX0)
    sigmaX1 = math.sqrt(varX1) 
    
    sigmaZ0 = math.sqrt(varZ0)
    sigmaZ1 = math.sqrt(varZ1)
    
    rho0 = sum(Q[:,0]*(((1.0*data[:,0]-mu_x0)*(1.0*data[:,1]-mu_z0))/(1.0*sigma_x0*sigma_z0)))/sum(Q[:,0])
    rho1 = sum(Q[:,1]*(((1.0*data[:,0]-mu_x1)*(1.0*data[:,1]-mu_z1))/(1.0*sigma_x1*sigma_z1)))/sum(Q[:,1])
        
    return [[muX0,muZ0,sigmaX0,sigmaZ0,rho0],[muX1,muZ1,sigmaX1,sigmaZ1,rho1]],[pi0,pi1]
    
    
# calcul des bornes pour contenir toutes les lois normales calculées
def find_video_bounds ( data, res_EM ):
    bounds = np.asarray ( find_bounds ( data, res_EM[0][0] ) )
    for param in res_EM:
        new_bound = find_bounds ( data, param[0] )
        for i in [0,2]:
            bounds[i] = min ( bounds[i], new_bound[i] )
        for i in [1,3]:
            bounds[i] = max ( bounds[i], new_bound[i] )
    return bounds

# la fonction appelée à chaque pas de temps pour créer l'animation
def animate ( i ):
    ax.cla ()
    dessine_normales (data, res_EM[i][0], res_EM[i][1], bounds, ax)
    ax.text(5, 40, 'step = ' + str ( i ))
    print "step animate = %d" % ( i )
    
# éventuellement, sauver l'animation dans une vidéo
# anim.save('old_faithful.avi', bitrate=4000)

data = read_file ("2014_tme4_faithful.txt")

# affichage des données : calcul des moyennes et variances des 2 colonnes
mean1 = data[:,0].mean ()
mean2 = data[:,1].mean ()
std1  = data[:,0].std ()
std2  = data[:,1].std ()

# les paramètres des 2 normales sont autour de ces moyennes
params = np.array ( [(mean1 - 0.2, mean2 - 1, std1, std2, 0),
                     (mean1 + 0.2, mean2 + 1, std1, std2, 0)] )
                                          
weights = np.array ( [0.4, 0.6] )

res_EM = []
vra = []
vra2 = []
res_EM.append([params,weights])

for i in range(0,20):
    Q,v,v2 = Q_i(data,params,weights)
    vra.append(v)
    vra2.append(v2)
    
    params,weights = M_step(data,Q,params,weights)
    res_EM.append(M_step(data,Q,params,weights))


#bounds = find_video_bounds ( data, res_EM )

# création de l'animation : tout d'abord on crée la figure qui sera animée
#fig = plt.figure ()
#ax = fig.gca (xlim=(bounds[0], bounds[1]), ylim=(bounds[2], bounds[3]))

#Affichage de l'annimation
#anim = animation.FuncAnimation(fig, animate,frames = len ( res_EM ), interval=500 )


plt.figure()               
plt.plot(np.arange(0, 20),vra)
# affichage de la figure
#bounds = find_bounds ( data, params )
#fig = plt.figure ()
#ax = fig.add_subplot(111)
#dessine_normales ( data, params, weights, bounds, ax )

#fig.show ()    
#plt.show()

#Q = Q_i(data,params,weights)
#weights,params = M_step(data,Q,params,weights)

#bounds = find_bounds ( data, params )



