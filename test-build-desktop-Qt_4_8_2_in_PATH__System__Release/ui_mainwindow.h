/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created: Tue Feb 3 15:43:50 2015
**      by: Qt User Interface Compiler version 4.8.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QGridLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QMainWindow>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QStatusBar>
#include <QtGui/QToolBar>
#include <QtGui/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QPushButton *pushButton_4;
    QPushButton *pushButton_3;
    QPushButton *pushButton_5;
    QPushButton *pushButton_2;
    QPushButton *pushButton;
    QPushButton *pushButton_6;
    QPushButton *pushButton_7;
    QPushButton *pushButton_8;
    QPushButton *pushButton_9;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(400, 300);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        gridLayoutWidget = new QWidget(centralWidget);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(-1, -1, 401, 231));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        pushButton_4 = new QPushButton(gridLayoutWidget);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));

        gridLayout->addWidget(pushButton_4, 2, 1, 1, 1);

        pushButton_3 = new QPushButton(gridLayoutWidget);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));

        gridLayout->addWidget(pushButton_3, 0, 0, 1, 1);

        pushButton_5 = new QPushButton(gridLayoutWidget);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));

        gridLayout->addWidget(pushButton_5, 1, 1, 1, 1);

        pushButton_2 = new QPushButton(gridLayoutWidget);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));

        gridLayout->addWidget(pushButton_2, 1, 0, 1, 1);

        pushButton = new QPushButton(gridLayoutWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        gridLayout->addWidget(pushButton, 2, 0, 1, 1);

        pushButton_6 = new QPushButton(gridLayoutWidget);
        pushButton_6->setObjectName(QString::fromUtf8("pushButton_6"));

        gridLayout->addWidget(pushButton_6, 0, 1, 1, 1);

        pushButton_7 = new QPushButton(gridLayoutWidget);
        pushButton_7->setObjectName(QString::fromUtf8("pushButton_7"));

        gridLayout->addWidget(pushButton_7, 1, 2, 1, 1);

        pushButton_8 = new QPushButton(gridLayoutWidget);
        pushButton_8->setObjectName(QString::fromUtf8("pushButton_8"));

        gridLayout->addWidget(pushButton_8, 0, 2, 1, 1);

        pushButton_9 = new QPushButton(gridLayoutWidget);
        pushButton_9->setObjectName(QString::fromUtf8("pushButton_9"));

        gridLayout->addWidget(pushButton_9, 2, 2, 1, 1);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 400, 29));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0, QApplication::UnicodeUTF8));
        pushButton_4->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
        pushButton_3->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
        pushButton_5->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
        pushButton_2->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
        pushButton->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
        pushButton_6->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
        pushButton_7->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
        pushButton_8->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
        pushButton_9->setText(QApplication::translate("MainWindow", "PushButton", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
