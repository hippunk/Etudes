# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 10:51:44 2014

@author: 3401924
"""

# -*- coding: utf-8 -*- 

import math
import numpy as np
import matplotlib.pyplot as plt

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
   
out = read_file("2014_tme3_usps_train.txt")

#mu = np.sort(out[0][1])[128]+np.sort(out[0][1])[129])/2

#print len(out[1][2])
#display_image(out[1][2])

def learnML_class_parameters(classe):
    mu = np.zeros(256)
    sigma = np.zeros(256)
    moyenne = np.zeros(256)
    for px in range(0,255): #pour chaque pixel
        temp = []     
        for i in classe: #pour chaque image on construit un tableau du
                         #px courant
            temp.append(i[px])
            
        #calcul de la médiane    
        temp.sort()
        if len(temp)%2 == 0:
            mu[px] = (temp[len(temp)/2-1]+temp[len(temp)/2])/2        
        else:
            mu[px] = temp[len(temp)/2+1] 
            
        #calcul moyenne pour sigma    
        moyenne[px] = sum(temp)*1.0/len(temp)*1.0
        for j in range(0,256):
            temp[j] = temp[j]-moyenne[px]

        
        sigma[px] = math.pow(sum(temp),2)/len(temp)
         
    return moyenne,sigma

var5, toto = learnML_class_parameters(out[9])

def densiteCalc(sigma,x,mu):
    sqr = math.sqrt(2*math.pi)*sigma
    frac = -1/2
    div = (x-mu)/sigma
    densite = (1/sqr)*math.exp(frac*math.pow(div,2))
    return densite

#display_image(var5)  
#display_image(toto)    

#learnML_all_parameters retourne une liste dont chaque entrée est une liste de
# couple, resultat[2][0] permet d'avoir la moyenne des images 2 resultat[4][1] 
#permet d'avoir le sigma des images 4
def learnML_all_parameters(train_data):
    tmp=[]
    for i in train_data:
        tmp.append(learnML_class_parameters(i))
    return tmp
    
    """
    for i in range(0,len(train_data):
        tmp.append(learnML_class_parameters(train_data[i]))
    """
    

    
#param    

parameters = learnML_all_parameters(out)
#print parameters

out2=read_file("2014_tme3_usps_test.txt")
#print out2[0][0]
#display_image(out2[9][1])




def log_likelihoods (image,parameters):
    tab=np.zeros(10)
    for j in range(0,10):
        tmp=[]
        for i in range(0,256):
            if parameters[j][1][i]==0:
                tmp.append(0)
            else:
                if image[i]*densiteCalc(parameters[j][0][i],i,parameters[j][1][i]) ==0:
                    tmp.append(0)
                else:
                    tmp.append(math.log(image[i]*densiteCalc(parameters[j][0][i],i,parameters[j][1][i])))
        tab[j]=sum(tmp)
    return tab
 
tab=log_likelihoods(out2[9][0],parameters)
print tab


   
    
    
    
        
    
    
    
    
    
    



    
    
    
        