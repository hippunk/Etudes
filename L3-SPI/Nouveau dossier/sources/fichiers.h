#ifndef FILES_H_INCLUDED
#define FILES_H_INCLUDED

void data_impression(FILE *fichier);
void serie_impression(serie_t serie, FILE *fichier);
void out_impression(serie_t serie, FILE *fichier);
void fichier_exporter(serie_t serie);
void fichier_importer();

#endif
