#ifndef CARMICHAEL_H
#define CARMICHAEL_H

#include<gmp.h>

void mpz_pow(mpz_t result,mpz_t e,mpz_t n);
int iIs_carmichael(int n);
int mpzIs_carmichael(mpz_t n);

#endif
