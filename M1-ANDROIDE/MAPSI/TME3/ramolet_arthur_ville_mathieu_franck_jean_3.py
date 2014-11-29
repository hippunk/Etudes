# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 11:04:13 2014

@author: 2900621
"""

# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math as m


def read_file ( filename ):
    """
    Lit un fichier USPS et renvoie un tableau de tableaux d'images.
    Chaque image est un tableau de nombres réels.
    Chaque tableau d'images contient des images de la même classe.
    Ainsi, T = read_file ( "fichier" ) est tel que T[0] est le tableau
    des images de la classe 0, T[1] contient celui des images de la classe 1,
    et ainsi de suite.
    """
    # lecture de l'en-tête
    infile = open ( filename, "r" )    
    nb_classes, nb_features = [ int( x ) for x in infile.readline().split() ]

    # creation de la structure de données pour sauver les images :
    # c'est un tableau de listes (1 par classe)
    data = np.empty ( 10, dtype=object )  
    filler = np.frompyfunc(lambda x: list(), 1, 1)
    filler( data, data )

    # lecture des images du fichier et tri, classe par classe
    for ligne in infile:
        champs = ligne.split ()
        if len ( champs ) == nb_features + 1:
            classe = int ( champs.pop ( 0 ) )
            data[classe].append ( map ( lambda x: float(x), champs ) )    
    infile.close ()

    # transformation des list en array
    output  = np.empty ( 10, dtype=object )
    filler2 = np.frompyfunc(lambda x: np.asarray (x), 1, 1)
    filler2 ( data, output )

    return output




def display_image ( X ):
    """
    Etant donné un tableau de 256 flotants représentant une image de 16x16
    pixels, la fonction affiche cette image dans une fenêtre.
    """
    # on teste que le tableau contient bien 256 valeurs
    if X.size != 256:
        raise ValueError ( "Les images doivent être de 16x16 pixels" )

    # on crée une image pour imshow: chaque pixel est un tableau à 3 valeurs
    # (1 pour chaque canal R,G,B). Ces valeurs sont entre 0 et 1
    Y = X / X.max ()
    img = np.zeros ( ( Y.size, 3 ) )
    for i in range ( 3 ):
        img[:,i] = X

    # on indique que toutes les images sont de 16x16 pixels
    img.shape = (16,16,3)

    # affichage de l'image
    plt.imshow( img )
    plt.show ()
    

def learnML_class_parameters(classe):
    mu=np.zeros(256)
    mucarre=np.zeros(256)
    sigma=np.zeros(256)
    for i in range (len(classe)):
        for j in range(256):    
            mu[j]+=classe[i][j]
            mucarre[j]+=np.square(classe[i][j])
    for k in range (256):
        mu[k]/=len(classe)
        mucarre[k]/=len(classe)
        sigma[k]=mucarre[k] - np.square(mu[k])
    return (mu,sigma)
 

out = read_file("2014_tme3_usps_train.txt")
print learnML_class_parameters(out[0])
display_image(out[0][1])




def learnML_all_parameters(train_data):
    parameters = []
    for i in range (len(train_data)):
        parameters.append(learnML_class_parameters(train_data[i]))
    return parameters


#parameters=learnML_all_parameters(read_file("2014_tme3_usps_train.txt"))



    
def log_likelihoods ( image, parameters ) :
    nb_class = len(parameters) 
    nb_pix = parameters[0][0].shape[0]
    tab= []
    sqrt_2pi = np.sqrt ( 2 * np.pi )
    for i in range ( nb_class ) :
        sum_log= 0
        for j in range ( nb_pix ) :
            var = parameters[i][1][j]
            if var == 0 :
                log = 0
            else :
                esp = parameters[i][0][j]
                sqrt_var = np.sqrt ( var )
                factor = 1 / ( sqrt_2pi * sqrt_var )
                non_exp = -0.5 * np.square ( (image[j] - esp) / sqrt_var )
                log =  np.log ( factor ) + non_exp  
            sum_log += log 
        tab.append ( sum_log ) 
    return np.array ( tab )



#image=read_file("2014_tme3_usps_train.txt")[0][9]
#print log_likelihoods(image,parameters)


def classify_image(image,parameters):
    return np.argmax(log_likelihoods(image,parameters))
    



def classify_all_images(test_data,parameters):
    tabr=np.zeros((10,10))
    for c in range(len(test_data)):
        for j in range(len(test_data[c])):
            classified=classify_image(test_data[c][j],parameters)
            tabr[c][classified]+=1
        tabr[c,:]/=len(test_data[c])
    return tabr
            
#out2=read_file("2014_tme3_usps_test.txt")
      
def dessine ( classified_matrix ):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = y = np.linspace ( 0, 9, 10 )
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, classified_matrix, rstride = 1, cstride=1 )
    plt.show()
    
    
    
#dessine( classify_all_images(out2,parameters))
'''
'''






