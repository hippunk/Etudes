#include "zonedessin.h"

ZoneDessin::ZoneDessin(QWidget *parent) :
    QWidget(parent)
{
    setMinimumSize(400,300);
    debut.setX(0);
    debut.setY(0);
    fin.setX(0);
    fin.setY(0);
}

void ZoneDessin::paintEvent( QPaintEvent* e){
    QPainter painter( this );
    ligne.setPoints(debut,fin);
    ligne.
    painter.drawLine(ligne);
}

void ZoneDessin::mousePressEvent( QMouseEvent* e){
    //ligneTrace();
    debut = e->pos();
    fin = e->pos();
    update();
}

void ZoneDessin::mouseMoveEvent( QMouseEvent* e){
    fin = e->pos();
    update();
}

void ZoneDessin::mouseReleaseEvent( QMouseEvent* e){
    update();
}
