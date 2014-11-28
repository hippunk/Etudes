#ifndef _FONCTION_H
#define _FONCTION_H


int my_pgcd(int tmp1,int tmp2);

int my_inverse(int a,int n);

int expo_mod(int m,int e,int n);

int first_test(int n);

int is_Carmichael(int n);

int Gen_nombrePremier();

int Gen_Carmichael();

int list_Carmichael(int k);

int test_Fermat(int n);

double experimental_Fermat(int nbtirage);

int TestRabinMiller(int n);

double experimental_RabinMiller(int nbtirage);

int GenPKRSA(int t);

#endif


