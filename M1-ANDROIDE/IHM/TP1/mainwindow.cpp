#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{

    QMenuBar* myMenuBar = menuBar();
    QMenu* fileMenu = myMenuBar->addMenu("&Fichier");
    QToolBar* fileToolBar = addToolBar(tr("Fichier"));

    QAction* actOpen = new QAction(style()->standardIcon(QStyle::SP_DialogOpenButton),("&Open..."), this);
    actOpen->setShortcut(QKeySequence(tr("Ctrl+O")));
    actOpen->setToolTip("Open");
    actOpen->setStatusTip("Tip : Open");

    QAction* actSave = new QAction(style()->standardIcon(QStyle::SP_DialogSaveButton),("&Save..."), this);
    actSave->setShortcut(QKeySequence(tr("Ctrl+S")));
    actSave->setToolTip("Save");
    actSave->setStatusTip("Tip : Save");


    QAction* actQuit = new QAction(style()->standardIcon(QStyle::SP_DialogCloseButton),("Qui&t..."), this);
    actQuit->setShortcut(QKeySequence(tr("Ctrl+Q")));
    actQuit->setToolTip("Quit");
    actQuit->setStatusTip("Tip : Quit");

    fileMenu->addAction(actOpen);
    fileMenu->addAction(actSave);
    fileMenu->addAction(actQuit);

    fileToolBar->addAction(actOpen);
    fileToolBar->addAction(actSave);
    fileToolBar->addAction(actQuit);

    setCentralWidget(new QTextEdit());
    setStatusBar(new QStatusBar());

    //ui->setupUi(this);

    QObject::connect(actOpen, SIGNAL(triggered()), this, SLOT(openFile()));
    QObject::connect(actSave, SIGNAL(triggered()), this, SLOT(saveFile()));
    QObject::connect(actQuit, SIGNAL(triggered()), this, SLOT(close()));
}


void MainWindow::openFile(){
    QString fileName =  QFileDialog::getOpenFileName( this,
     tr("Open Text"), // titre
     "~/", // répertoire initial
     tr("Text Files (*.txt)") // filtre
     );

    QFile file(fileName);
}

void MainWindow::saveFile(){
    QString fileName =  QFileDialog::getSaveFileName( this,
     tr("Open Text"), // titre
     "~/", // répertoire initial
     tr("Text Files (*.txt)") // filtre
     );

    cout << qPrintable(fileName);
}

void MainWindow::quitApp(){
    cout << "Quit App\n";
}



MainWindow::~MainWindow()
{
    delete ui;
}
