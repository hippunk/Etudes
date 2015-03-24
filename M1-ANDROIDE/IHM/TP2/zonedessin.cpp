#include "zonedessin.h"

ZoneDessin::ZoneDessin(QWidget *parent) :
    QWidget(parent)
{
    setMinimumSize(400,300);
    debut.setX(0);
    debut.setY(0);
    fin.setX(0);
    fin.setY(0);
    color = Qt::black;
}

void ZoneDessin::paintEvent( QPaintEvent* e){
    QPainter painter( this );

    for (std::vector<std::pair<QLine,QColor> >::iterator it = lignes.begin() ; it != lignes.end(); ++it){
        ligne = it->first;
        //painter.scale(15);
        painter.setPen(it->second);
        painter.drawLine(ligne);
    }

    ligne.setPoints(debut,fin);
    painter.setPen(color);
    painter.drawLine(ligne);
}

void ZoneDessin::mousePressEvent( QMouseEvent* e){
    debut = e->pos();
    fin = e->pos();
}

void ZoneDessin::mouseMoveEvent( QMouseEvent* e){
    fin = e->pos();
    repaint();
}

void ZoneDessin::mouseReleaseEvent( QMouseEvent* e){
    lignes.push_back(std::make_pair(ligne,color));
    debut.setX(0);
    debut.setY(0);
    fin.setX(0);
    fin.setY(0);
    repaint();
}

void ZoneDessin::slotCouleur(QColor color){

    this->color = color;

}

void ZoneDessin::slotEpaisseur(int newEpaisseur){

}
void ZoneDessin::slotStyle(int newStyle){

}

void ZoneDessin::slotDelete(){
    if(!lignes.empty())
        lignes.pop_back();
    repaint();
}
