#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{

    myMenuBar = menuBar();
    fileMenu = myMenuBar->addMenu("&Fichier");
    fileToolBar = addToolBar(tr("Fichier"));

    actOpen = new QAction(style()->standardIcon(QStyle::SP_DialogOpenButton),("&Open..."), this);
    actOpen->setShortcut(QKeySequence(tr("Ctrl+O")));
    actOpen->setToolTip("Open");
    actOpen->setStatusTip("Tip : Open");

    actSave = new QAction(style()->standardIcon(QStyle::SP_DialogSaveButton),("&Save..."), this);
    actSave->setShortcut(QKeySequence(tr("Ctrl+S")));
    actSave->setToolTip("Save");
    actSave->setStatusTip("Tip : Save");


    actQuit = new QAction(style()->standardIcon(QStyle::SP_DialogCloseButton),("Qui&t..."), this);
    actQuit->setShortcut(QKeySequence(tr("Ctrl+Q")));
    actQuit->setToolTip("Quit");
    actQuit->setStatusTip("Tip : Quit");

    actSelectColor = new QAction(style()->standardIcon(QStyle::SP_ComputerIcon),("Select Color..."), this);
    actSelectColor->setShortcut(QKeySequence(tr("Ctrl+J")));
    actSelectColor->setToolTip("Color");
    actSelectColor->setStatusTip("Tip : SetColor");

    actDelete = new QAction(style()->standardIcon(QStyle::SP_ArrowForward),("Delete last line..."), this);
    actDelete->setShortcut(QKeySequence(tr("Ctrl+Z")));
    actDelete->setToolTip("Delete");
    actDelete->setStatusTip("Tip : Delete");

    fileMenu->addAction(actOpen);
    fileMenu->addAction(actSave);
    fileMenu->addAction(actQuit);
    fileMenu->addAction(actSelectColor);
    fileMenu->addAction(actDelete);

    fileToolBar->addAction(actOpen);
    fileToolBar->addAction(actSave);
    fileToolBar->addAction(actQuit);
    fileToolBar->addAction(actSelectColor);
    fileToolBar->addAction(actDelete);

    comboBox = new QComboBox(fileToolBar);
    comboBox->addItem("Paris");
    comboBox->addItem("Londres");
    comboBox->addItem("Singapour");
    comboBox->addItem("Tokyo");

    zoneDessin = new ZoneDessin();
    qStatusBar = new QStatusBar();

    setCentralWidget(zoneDessin);
    setStatusBar(qStatusBar);

    //ui->setupUi(this);

    QObject::connect(actOpen, SIGNAL(triggered()), this, SLOT(openFile()));
    QObject::connect(actSave, SIGNAL(triggered()), this, SLOT(saveFile()));
    //QObject::connect(actSelectColor, SIGNAL(triggered()), zoneDessin, SLOT(slotCouleur(color = QColorDialog::getColor())));
    QObject::connect(actSelectColor, SIGNAL(triggered()), this, SLOT(setColor()));
    QObject::connect(actDelete, SIGNAL(triggered()), this->zoneDessin, SLOT(slotDelete()));
    QObject::connect(actQuit, SIGNAL(triggered()), this, SLOT(close()));

    //cout << "This : " << this << " ui : " << ui << endl;

}


void MainWindow::openFile(){
    QString fileName =  QFileDialog::getOpenFileName( this,
     tr("Open Text"), // titre
     "~/", // répertoire initial
     tr("Text Files (*.txt)") // filtre
     );

    QFile file(fileName);
}

void MainWindow::setColor(){
    zoneDessin->slotCouleur(QColorDialog::getColor());
}

void MainWindow::saveFile(){
    QString fileName =  QFileDialog::getSaveFileName( this,
     tr("Open Text"), // titre
     "~/", // répertoire initial
     tr("Text Files (*.txt)") // filtre
     );

    cout << qPrintable(fileName);
}

MainWindow::~MainWindow()
{
    delete ui;
}
