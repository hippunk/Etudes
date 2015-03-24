#ifndef ZONEDESSIN_H
#define ZONEDESSIN_H

#include <QWidget>
#include <QPainter>
#include <QMouseEvent>
#include <QLine>
#include <QColorDialog>
#include <iostream>
#include <vector>

class ZoneDessin : public QWidget
{
    Q_OBJECT

    public:
        explicit ZoneDessin(QWidget *parent = 0);
        void paintEvent(QPaintEvent *e = 0);

    protected:
        void mousePressEvent( QMouseEvent* e);
        void mouseMoveEvent( QMouseEvent* e);
        void mouseReleaseEvent( QMouseEvent* e);

    private:
        QPoint debut;
        QPoint fin;
        QLine ligne;
        QColor color;
        std::vector<std::pair<QLine,QColor> > lignes;
    signals:

    public slots:
        void slotCouleur(QColor color);
        void slotEpaisseur(int newEpaisseur);
        void slotStyle(int newStyle);
        void slotDelete();

    
};

#endif // ZONEDESSIN_H
