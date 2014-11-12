#ifndef ARITHZN_H
#define ARITHZN_H

#include<gmp.h>

void mpz_max(mpz_t a, mpz_t b);
void mpz_min(mpz_t a, mpz_t b);
void mpzMy_pgcd(mpz_t a, mpz_t b);
int iMy_pgcd(int a, int b);

#endif
