#ifndef AFFICHAGE_H_INCLUDED
#define AFFICHAGE_H_INCLUDED
#include<SDL/SDL.h>
#include<SDL/SDL_image.h>

void erreur(const int no_erreur);
void n_affichage(SDL_Surface * ecran, int n);
void data_affichage(SDL_Surface * ecran);
void out_affichage(SDL_Surface * ecran, serie_t const serie);
void serie_affichage(SDL_Surface * ecran,serie_t const serie);

#endif
