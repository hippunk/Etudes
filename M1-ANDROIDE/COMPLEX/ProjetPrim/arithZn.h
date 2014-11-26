#ifndef ARITHZN_H
#define ARITHZN_H

#include<gmp.h>

/*Exposant modulaire avec implémentation fast exp résultat format mpz_t*/
void mpzExpo_mod(mpz_t result, mpz_t m, mpz_t e, mpz_t n);

/*Renvoi le maximum entre a et b au format mpz_t*/
void mpz_max(mpz_t result,mpz_t a, mpz_t b);

/*Renvoi le minimum entre a et b au format mpz_t*/
void mpz_min(mpz_t result,mpz_t a, mpz_t b);

/*mpzMy_pgcd alloue les variables temporaires nécéssaire à l'algo et passe le tout a My_pgcdMemSave (Permet d'éviter alloc dynamique dans récursion)*/
void mpzMy_pgcd(mpz_t result,mpz_t a, mpz_t b);

/*Algo basique d'euclide pour pgcd adapté à gmp (Voir mpzMy_pgcd pour explications sur passage des variables temporaires et gestion mémoire)*/
void mpzMy_pgcdMemSave(mpz_t result,mpz_t a, mpz_t b,mpz_t min,mpz_t max,mpz_t tmp);

void mpzMy_inverse(mpz_t result, mpz_t a, mpz_t n);

/**
*	Les fonctions avec int sont destinées aux tests algos pour comparer avec les mpz_t
*/

/*Exposant modulaire fastExp avec int*/
int iMod_exp(int m, int e, int n);

/*Algo euclide pgcd avec int*/
int iMy_pgcd(int a, int b);

int iMy_inverse(int a, int b);

#endif
