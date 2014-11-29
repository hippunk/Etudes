# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 10:51:44 2014

@author: Mathieu Franck Jean, Arthur Ramolet
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
   
   
#learnML_class_parameters(classe) prend une classe d'image en paramètre et retourne l'image moyenne et l'image variante de cette classe
#(Une image est un tableau de 256 valeurs (16x16 pixels) chaque valeur correspond au niveau de gris d'un pixel)
def learnML_class_parameters(classe):
    mu = np.zeros(256)
    sigma = np.zeros(256)
    moyenne = np.zeros(256)
    temp = np.zeros(256)
    
    #Génération de l'image moyenne
    for i in classe:
            moyenne += i   

    moyenne /= len(classe)      

    #génération de l'image variante
    for i in classe:
            sigma += pow((i-moyenne),2)    
    sigma /= len(classe)    
         
         
        
    return moyenne,sigma

#densiteCalc(sigma,x,mu) calcule la densité de x suivant une loi normale de moyenne mu et d'ecart type sigma
def densiteCalc(sigma,x,mu):
    sqr = math.sqrt(2*math.pi)*sigma
    frac = -1/2
    div = (x-mu)/sigma
    densite = (1/sqr)*math.exp(frac*math.pow(div,2))
    return densite

#learnML_all_parameters(train_data) Construit la liste des couples moyenne/variance a partir de train_data
#retourne une liste dont chaque entrée est un
# couple moyenne/variance, resultat[2][0] permet d'avoir la moyenne des images 2 resultat[4][1] 
#permet d'avoir la variance des images 4
def learnML_all_parameters(train_data):
    tmp=[]
    for i in train_data:
        
        tmp.append(learnML_class_parameters(i))
    return tmp


#log_likelihoods (image,parameters) Compare une image avec les couples moyenne/variance de chaque image
#retourne un tableau contenant la log-vraisemblance de la comparaison de l'image avec chaque classe
def log_likelihoods (image,parameters):
    tab=np.zeros(10)
    for j in range(0,10):
        tmp=[]
        for i in range(0,256):

           if parameters[j][1][i]!=0:
               dens = densiteCalc(math.sqrt(parameters[j][1][i]),image[i],parameters[j][0][i])
               if dens !=0:
                   tmp.append(math.log(dens))

        tab[j]=sum(tmp)
    return tab
 
# classify_images(image,parameters) Utilise le résultat de log_likelihoods afin de déterminer a quelle image corespond le plus le paramètre image
def classify_images(image,parameters):
    values = log_likelihoods (image,parameters)  
    return np.where(values==max(values))[0][0]
    
#classify_all_images(test_data, parameters) Utilise classify image pour comparer toute la base testée avec le modèle
#retourne le tableau des probabilitées d'appartenance d'une image a chaque classe d'image
def classify_all_images(test_data, parameters):    
    tab = np.zeros([10,10])
    m=0
    n=0
    for i in test_data:
        n=0
        longueur = len(i)
        for j in i:        
            val = classify_images(j,parameters)
            tab[m][val]+=1
        print 'Classification en cours : ',(m+1)*10,'%'
        tab[m] = tab[m]/longueur
        m+=1
    return tab
    
#Dessine le graphe 3D des probabilitées d'appartenance d'une image a chaque classe d'image    
def dessine ( classified_matrix ):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = y = np.linspace ( 0, 9, 10 )
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, classified_matrix, rstride = 1, cstride=1 )
 
 
print 'Ouverture du fichier d''apprentisage'
out = read_file("2014_tme3_usps_train.txt")

print 'Création de la base de comparaison'
parameters = learnML_all_parameters(out)

display_image (parameters[9][0])


print 'Ouverture du fichier d''images'
#out2=read_file("2014_tme3_usps_test.txt")

print 'Classification des images comparées avec la base'
#resultat = classify_all_images(out2,parameters)
#dessine(resultat)
#plt.show ()

   
    
    
    
        
    
    
    
    
    
    



    
    
    
        