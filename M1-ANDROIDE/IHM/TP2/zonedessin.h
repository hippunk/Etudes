#ifndef ZONEDESSIN_H
#define ZONEDESSIN_H

#include <QWidget>
#include <QPainter>
#include <QMouseEvent>
#include <QLine>

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

    signals:

    public slots:
        /*void couleur();
        void epaisseur();
        void style();*/

    
};

#endif // ZONEDESSIN_H
