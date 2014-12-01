#ifndef TEST_H
#define TEST_H

/*Fonction chronomètre utilisant la bibliothèque temps système linux (sys/time.h), Un premier appel permet d'initialiser le chrono,
la fonction retournent le temps entre deux appels*/
double chrono();

/*Affiche la liste des nombres premiers < 100000 ainsi que le nombre trouvé*/
void test_premiers();

/*Affiche le dernier nombre premier calculé en 1 minute*/
void test_1min_premiers();

void test_5min_carmichael();

void test_carmichael();

#endif
