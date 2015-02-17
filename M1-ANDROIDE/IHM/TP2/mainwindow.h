#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <iostream>

#include <QMainWindow>
#include <QTextEdit>
#include <QFileDialog>

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
    ZoneDessin *zoneDessin;
    QStatusBar *qStatusBar;

signals:

public slots:
    void openFile();
    void saveFile();

};

#endif // MAINWINDOW_H
