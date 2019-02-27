#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#include "defines.h"
#include "affichage.h"
#include "outil.h"

void data_impression(FILE *fichier)
{/*impression dans le fichier de data*/
        int i;

        fprintf(fichier, "Data        :  ");
        for(i = 0;Data_I[i] != Vide; i++)
        {
            fprintf(fichier, "%i ",Data_I[i]);
        }
        fprintf(fichier, "\n");
}

void serie_impression(serie_t serie, FILE *fichier)
{/*impression dans le fichier de la série*/
    int i = 0;

    fprintf(fichier,"serie codee : ");

    for(i = 0; i < N; i++)
    {
        if(serie.P_o[i] == 0 && serie.N_o[i] == 0)
            fprintf(fichier," 0");
       else if(serie.P_o[i] == 1 && serie.N_o[i] == 0)
            fprintf(fichier," 1");
        else if(serie.P_o[i] == 0 && serie.N_o[i] == 1)
            fprintf(fichier,"-1");
        else if(serie.P_o[i] != Vide && serie.N_o[i] != Vide)
        {
            erreur(2);
        }
    }
    fprintf(fichier,"\n");
}

void out_impression(serie_t serie, FILE *fichier)
{/*impression des sorties dans le fichier*/
    int i = 0;

    fprintf(fichier,"P_o         : ");

    for(i = 0; i < N; i++)
    {
        if(serie.P_o[i] != Vide)
            fprintf(fichier,"%2i", serie.P_o[i]);
    }

    fprintf(fichier,"\n");
    fprintf(fichier,"N_o         : ");

    for(i = 0; i < N; i++)
    {
        if(serie.N_o[i] != Vide)
           fprintf(fichier,"%2i", serie.N_o[i]);
    }

    fprintf(fichier,"\n");
}

void fichier_exporter(serie_t serie)
{/*exporte les données dans un fichier*/
    FILE* fichier = NULL;
    int overflow = 0;
    char nom_fichier[33];
    char repertoire[42];
    char en_tete[64];

    printf("Saisissez le nom du fichier :\n");
    overflow = s_scanf(nom_fichier, 33);
    printf("Saisissez votre en tete :\n");
    overflow = s_scanf(en_tete, 64);

    if(overflow)
        erreur(5);

    strcpy(repertoire,"fichiers/");
    strcat(repertoire,nom_fichier);

    fichier = fopen(repertoire, "w");

    if (fichier != NULL)
    {
        data_impression(fichier);
        fprintf(fichier,"\n### %s ###\n", en_tete);
        serie_impression(serie, fichier);
        out_impression(serie, fichier);
        fclose(fichier);
    }
    else
    {
        erreur(4);
    }
}

void fichier_importer()
{/*importe la data depuis un fichier*/
    FILE* fichier = NULL;
    int overflow = 0;
    char nom_fichier[33];
    char repertoire[42];
    int i = 0;
    char temp;

    printf("Saisissez le nom du fichier :\n");
    overflow = s_scanf(nom_fichier, 33);

    if(overflow)
        erreur(5);

    strcpy(repertoire,"fichiers/");
    strcat(repertoire,nom_fichier);

    fichier = fopen(repertoire, "r");

    if (fichier != NULL)
    {
        while(temp != '\n')
        {
            fscanf(fichier, "%c", &temp);
            if(temp == '0')
            {
                Data_I[i] = 0;
                i++;
            }

            else if(temp == '1')
            {
                Data_I[i] = 1;
                i++;
            }
        }

        while(i < N)
        {
            Data_I[i] = Vide;
            i++;
        }

        fclose(fichier);
    }
    else
    {
        erreur(4);
    }
}

