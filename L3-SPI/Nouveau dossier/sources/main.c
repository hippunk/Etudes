#include<stdio.h>
#include<stdlib.h>
#include<SDL/SDL.h>
#include<SDL/SDL_image.h>

#include "defines.h"
#include "HDBn.h"
#include "affichage.h"
#include "fichiers.h"
#include "outil.h"

int main(int argc, char *argv[])
{
    SDL_Init(SDL_INIT_VIDEO);

    SDL_Surface * ecran = NULL;
    SDL_Surface * fond = NULL;
    SDL_Event event;

    serie_t serie;
    data_init();
    serie_init(&serie);
    int continuer = 1;
    int n = 2;
    int nb_elem = 0;
    int actualiser = 1;

    SDL_Rect positionFond;
    positionFond.x = 0;
    positionFond.y = 0;
    SDL_WM_SetIcon(IMG_Load("GFX/icone.jpg"), NULL);
    ecran = SDL_SetVideoMode(1100,600,32,SDL_HWSURFACE);
    SDL_WM_SetCaption("HDBnATOR", NULL);
    fond = IMG_Load("GFX/HDBn.png");

    SDL_EnableKeyRepeat(100,100);
    SDL_BlitSurface(fond, NULL, ecran, &positionFond);
    SDL_Flip(ecran);

    while(continuer)
    {
        if(actualiser == 1)
        {
            serie_reset(&serie);
            HDBn(&serie, n);
            SDL_BlitSurface(fond, NULL, ecran, &positionFond);
            n_affichage(ecran, n);
            polarite_reset(&serie);
            data_affichage(ecran);
            serie_affichage(ecran, serie);
            out_affichage(ecran, serie);
            SDL_Flip(ecran);
            actualiser = 0;
        }

        SDL_WaitEvent(&event);
        switch(event.type)
        {
            case SDL_QUIT:
                continuer = 0;
                break;

            case SDL_KEYDOWN:
                if(event.key.keysym.sym == SDLK_2 || event.key.keysym.sym == SDLK_KP2)
                {
                    n = 2;
                    actualiser = 1;
                }
                else if(event.key.keysym.sym == SDLK_3 || event.key.keysym.sym == SDLK_KP3)
                {
                    n = 3;
                    actualiser = 1;
                }
                else if(event.key.keysym.sym == SDLK_4 || event.key.keysym.sym == SDLK_KP4)
                {
                    n = 4;
                    actualiser = 1;
                }

                else if((event.key.keysym.sym == SDLK_0 || event.key.keysym.sym == SDLK_o || event.key.keysym.sym == SDLK_KP0) && nb_elem < N)
                {
                    Data_I[nb_elem] = 0;
                    nb_elem++;
                    actualiser = 1;
                }
                else if((event.key.keysym.sym == SDLK_1 || event.key.keysym.sym == SDLK_i || event.key.keysym.sym == SDLK_KP1) && nb_elem < N)
                {
                    Data_I[nb_elem] = 1;
                    nb_elem++;
                    actualiser = 1;
                }
                else if(event.key.keysym.sym == SDLK_BACKSPACE && nb_elem > 0)
                {
                    nb_elem--;
                    Data_I[nb_elem] = Vide;
                    actualiser = 1;
                }
        }
    }

    SDL_FreeSurface(fond);
    SDL_Quit();
    return EXIT_SUCCESS;
}

