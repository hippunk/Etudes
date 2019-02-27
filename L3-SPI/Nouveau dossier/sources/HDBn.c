#include<stdio.h>
#include<stdlib.h>

#include "defines.h"
#include "affichage.h"
#include "HDBn.h"

void data_saisie()
{/*Saisie manuelle de la data*/
    fflush(stdin);
    int i = 0;
    char data;

    printf("Saissisez la data. 50 caractères max, les autres seront ingorés.\n");
    while(data != '\n' && i < N)
    {
            scanf("%c", &data);
            if(data == '1')
            {
                Data_I[i] = 1;
                i++;
            }

            else if(data == '0')
            {
                Data_I[i] = 0;
                i++;
            }
    }

    while(i<N) //complete le reste de la data avec vide
    {
        Data_I[i] = Vide;
        i++;
    }

    fflush(stdin); //vide les caratères en trop
}

void data_init()
{/*initialise la data a vide*/
    int i;
    for(i = 0; i < N; i++)
    {
        Data_I[i] = Vide;
    }

    Reset_I[0] = 1;
    Reset_I[1] = -1;
}

void serie_reset(serie_t * const serie)
{/*Remet les sorties a 0*/
    int i = 0;

    for(i = 0; i < N; i++)
    {
        serie->P_o[i] = 0;
        serie->N_o[i] = 0;
    }
}

void polarite_reset(serie_t * const serie)
{/*remet les polaritées par défaut*/
    serie->polarite = Reset_I[0];
    serie->polarite_v = Reset_I[1];
}

void serie_init(serie_t * const serie)
{/*remet les sorties a 0 et les polaritées par défaut*/
    serie_reset(serie);
    polarite_reset(serie);
}

void HDBn(serie_t * const serie, const int n)
{/*effectue le traitement HDBn de la data*/

        if(serie == NULL)
        {
            erreur(0);
        }

        int i = 0;
        int j = 0;

        for(i = 0; i < N; i++)
        {
            if(Data_I[i] == Vide) //Si data[i] vide sorties a vide aussi
            {
                serie->N_o[i] = Vide;
                serie->P_o[i] = Vide;
            }

            else if(Data_I[i] == 1) //quand la data est a 1 bipolaire simple
            {
                if(serie->polarite == 1)
                {
                    serie->P_o[i] = 1;
                    serie->polarite *= -1;
                }

               else if(serie->polarite == -1)
                {
                    serie->N_o[i] = 1;
                    serie->polarite *= -1;
                }

                else
                {
                    erreur(1);
                }
            }

            else if(Data_I[i] == 0 && n !=0) //quand la data est a 0 (pas de traitement si n = 0)
            {
                int codage = 1;

                for(j=i; codage && (j <= i+n) && j < N; j++) //on vérifie si il y a plus de 2 zeros a la suite
                {
                    if(Data_I[j] == 1 || j == N || Data_I[j] == Vide || N-i < 3)
                    {
                        codage = 0;
                    }
                }

                if(codage == 1) //si oui on code avec le HDBn
                {
                    j--;

                    if(serie->polarite == -1 && serie->polarite_v == -1)
                    {
                        serie->P_o[j] = 1;
                        serie->polarite_v *= -1;
                        serie->polarite = -1;
                    }

                    else if(serie->polarite == 1 && serie->polarite_v == -1)
                    {
                        serie->P_o[i] = 1;
                        serie->P_o[j] = 1;
                        serie->polarite_v *= -1;
                        serie->polarite = -1;
                    }

                    else if(serie->polarite == -1 && serie->polarite_v == 1)
                    {
                        serie->N_o[i] = 1;
                        serie->N_o[j] = 1;
                        serie->polarite_v *= -1;
                        serie->polarite = 1;
                    }

                    else if(serie->polarite == 1 && serie->polarite_v == 1)
                    {
                        serie->N_o[j] = 1;
                        serie->polarite_v *= -1;
                        serie->polarite = 1;
                    }
                    i = j; //Le saut ici, permet de ne pas retraiter les 0 qu'on a déjà vérifier
                }
            }

            else if(n != 0)
                erreur(3);

        }
}

