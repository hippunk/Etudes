#ifndef DEFINES_H_INCLUDED
#define DEFINES_H_INCLUDED

#define N 30
#define Vide -9

int Data_I[N];
int Reset_I[N];

typedef struct serie_s
{/*struc serie, contient les sorties P_o et N_o et les polarités*/
    int P_o[N];
    int N_o[N];

    int polarite;
    int polarite_v;

}serie_t;

#endif
