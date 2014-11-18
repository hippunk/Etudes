#ifndef ARITHZN_H
#define ARITHZN_H

#include<gmp.h>


/*Renvoi le maximum entre a et b au format mpz_t*/
void mpz_max(mpz_t result,mpz_t a, mpz_t b);

/*Renvoi le minimum entre a et b au format mpz_t*/
void mpz_min(mpz_t result,mpz_t a, mpz_t b);

/*mpzMy_pgcd alloue les variables temporaires nécéssaire à l'algo et passe le tout a My_pgcdMemSave (Permet d'éviter alloc dynamique dans récursion)*/
void mpzMy_pgcd(mpz_t result,mpz_t a, mpz_t b);

/*Algo basique d'euclide pour pgcd adapté à gmp (Voir mpzMy_pgcd pour explications sur passage des variables temporaires et gestion mémoire)*/
void mpzMy_pgcdMemSave(mpz_t result,mpz_t a, mpz_t b,mpz_t min,mpz_t max,mpz_t tmp);

void mpzMy_inverse(mpz_t result, mpz_t a, mpz_t n);

/*Algo euclide pgcd avec int*/
int iMy_pgcd(int a, int b);

int iMy_inverse(int a, int b);
#endif
