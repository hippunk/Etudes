#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <iostream>

#include <QMainWindow>
#include <QTextEdit>
#include <QFileDialog>
#include <QColorDialog>.
#include <QComboBox>

#include "zonedessin.h"

using namespace std;

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    QMenuBar* myMenuBar;
    QMenu* fileMenu;
    QToolBar* fileToolBar;
    QAction* actOpen;
    QAction* actSave;
    QAction* actQuit;
    QAction* actSelectColor;
    QAction* actDelete;
    ZoneDessin *zoneDessin;
    QStatusBar *qStatusBar;
    QColor color;
    QComboBox *comboBox;

signals:

public slots:
    void openFile();
    void saveFile();
    void setColor();

};

#endif // MAINWINDOW_H
