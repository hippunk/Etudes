#include<stdio.h>
#include<stdlib.h>

#include "defines.h"
#include "affichage.h"

void erreur(const int no_erreur)
{/*gere les erreurs*/
    if (no_erreur == 0)
        printf("\nErreur : contenu pointeur\n");
    if (no_erreur == 1)
        printf("\nErreur : valeur de polarite\n");
    if (no_erreur == 2)
        printf("\nErreur : contenu des sorties\n");
    if (no_erreur == 3)
        printf("\nErreur : contenu de Data\n");
    if (no_erreur == 4)
        printf("\nErreur : Fichier inexistant\n");
    if (no_erreur == 5)
        printf("\nErreur : Depassement du nombre de caracteres autorise\n");

    exit(EXIT_FAILURE);
}

void n_affichage(SDL_Surface * ecran, int n)
{
    SDL_Surface * chiffre = NULL;
    SDL_Rect position;
    position.x = 995;
    position.y = 50;

    if(n == 2)
    {
        chiffre = IMG_Load("GFX/2.png");
    }

    else if(n == 3)
    {
        chiffre = IMG_Load("GFX/3.png");
    }

    else if(n == 4)
    {
        chiffre = IMG_Load("GFX/4.png");
    }


    SDL_BlitSurface(chiffre, NULL, ecran, &position);
    SDL_FreeSurface(chiffre);
}

void out_affichage(SDL_Surface * ecran, serie_t const serie)
{/*affiche les sorties*/
    int i = 0;

    SDL_Surface * positif = NULL;
    SDL_Surface * negatif = NULL;
    SDL_Surface * nul = NULL;

    positif = IMG_Load("GFX/1g.png");
    negatif = IMG_Load("GFX/1r.png");
    nul = IMG_Load("GFX/0.png");


    SDL_Rect position;
    position.x = 170;
    position.y = 350;

    for(i = 0; i < N; i++)
    {
        if(serie.P_o[i] == 1)
        {
            SDL_BlitSurface(positif, NULL, ecran, &position);
            position.x += 30;
        }
        else if(Data_I[i] != Vide)
        {
            SDL_BlitSurface(nul, NULL, ecran, &position);
            position.x += 30;
        }
    }

    position.x = 170;
    position.y = 450;

    for(i = 0; i < N; i++)
    {
        if(serie.N_o[i] == 1)
        {
            SDL_BlitSurface(negatif, NULL, ecran, &position);
            position.x += 30;
        }
        else if(Data_I[i] != Vide)
        {
            SDL_BlitSurface(nul, NULL, ecran, &position);
            position.x += 30;
        }
    }

    SDL_FreeSurface(positif);
    SDL_FreeSurface(negatif);
    SDL_FreeSurface(nul);
}

void data_affichage(SDL_Surface * ecran)
{/*affiche la data*/
    int i = 0;
    SDL_Surface * un = NULL;
    SDL_Surface * nul = NULL;
    un = IMG_Load("GFX/1.png");
    nul = IMG_Load("GFX/0.png");


    SDL_Rect position;
    position.x = 170;
    position.y = 150;
    for(i = 0; i < N; i++)
    {
        if(Data_I[i] == 0)
        {
            SDL_BlitSurface(nul, NULL, ecran, &position);
            position.x += 30;
        }
        else if(Data_I[i] == 1)
        {
            SDL_BlitSurface(un, NULL, ecran, &position);
            position.x += 30;
        }
        else if(Data_I[i] != Vide)
        {
            erreur(3);
        }
    }

    SDL_FreeSurface(un);
    SDL_FreeSurface(nul);
}

void serie_affichage(SDL_Surface * ecran,serie_t const serie)
{/*affiche la serie*/
    int i = 0;

    SDL_Surface * positif = NULL;
    SDL_Surface * negatif = NULL;
    SDL_Surface * nul = NULL;

    SDL_Rect position;
    position.x = 170;
    position.y = 250;

    positif = IMG_Load("GFX/1g.png");
    negatif = IMG_Load("GFX/n1r.png");
    nul = IMG_Load("GFX/0.png");

    for(i = 0; i < N; i++)
    {
        if(serie.P_o[i] == 0 && serie.N_o[i] == 0)
        {
            SDL_BlitSurface(nul, NULL, ecran, &position);
            position.x += 30;
        }

       else if(serie.P_o[i] == 1 && serie.N_o[i] == 0)
       {
            SDL_BlitSurface(positif, NULL, ecran, &position);
            position.x += 30;
       }

        else if(serie.P_o[i] == 0 && serie.N_o[i] == 1)
        {
            SDL_BlitSurface(negatif, NULL, ecran, &position);
            position.x += 30;
        }
    }

    SDL_FreeSurface(positif);
    SDL_FreeSurface(negatif);
    SDL_FreeSurface(nul);
}

