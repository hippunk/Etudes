#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <iostream>

#include <QMainWindow>
#include <QTextEdit>
 #include <QFileDialog>

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

public slots:
    void openFile();
    void saveFile();

};

#endif // MAINWINDOW_H
