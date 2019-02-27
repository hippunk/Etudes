#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<assert.h>
#include<time.h>
#define CLOCKS_PER_MSEC CLOCKS_PER_SEC/1000

int NbTourMaX;

void loop(int nb_tours)
{//Nombre de tours effectué avant problème
	NbTourMaX = nb_tours;
}

void attendre(int nb_ms)
{
    const int fin = clock() + nb_ms * CLOCKS_PER_MSEC;
    while(clock() <= fin);
}

int b_while(int bExpression)
{/*declenge une assertion si le nombre de tours choisi avec loop est dépassé*/
	NbTourMaX--;
	assert(NbTourMaX > 0);

	return bExpression;
}

int int_rand(int min, int max)
{//génere un nombre entier aléatoire

	assert(max >= min);
	return ((rand() % (max - min + 1)) + min);
}

int s_scanf(char * chaine, int longueur_max)
{//super scanf. limite le nombre de caractère saisi par longueur_max-1, dernier caractère necessaire pour EOF. Prend les espaces.

    assert(longueur_max > 0); //nb_caratère forcément positif

    int nb_chara = 0;
    char temp;
    int overflow = 0;

    fflush(stdin);

    scanf("%c", &temp);
    chaine[nb_chara] = temp;

    if(longueur_max > 1) //si plus d'un caractère pas besoin de poursuivre
    {
        for(nb_chara = 1;temp != '\n'; nb_chara++) //on boucle jusqu'au retour chariot
        {
            scanf("%c", &temp);
                if(nb_chara < longueur_max) //tant qu'on dépasse pas la limite on ajoute le caractère a la suite de la chaine
                {
                    if(temp != '\n')    //si retour chariot on ajoute pas
                    chaine[nb_chara] = temp;
                }
        }
    }

    if(nb_chara <= longueur_max)
    {
        chaine[nb_chara-1] = '\0'; //si pas de dépassement le dernier caractère devient EOF
    }

    else
    {
        chaine[longueur_max-1] = '\0'; //si depassement, la limite devient EOF et il y a overflow
        overflow = 1;
    }

    return overflow;
}

