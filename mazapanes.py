# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfazieeGPB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 579)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMaximumSize(QSize(16777215, 45))
        self.frame_superior.setLayoutDirection(Qt.LeftToRight)
        self.frame_superior.setStyleSheet(u"QFrame {\n"
"background-color : rgb(53,53,79);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"font:87 12pt \"Arial Black\";\n"
"background-color : #000000ff;\n"
"color : rgb(20,200,220);\n"
"border-radius:5px;\n"
"border :1px solid white;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_5 = QPushButton(self.frame_superior)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 41))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        icon = QIcon()
        icon.addFile(u"../Imagenes/mazapan.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.label = QLabel(self.frame_superior)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 35))
        self.label.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(434, 13, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(40, 35))
        self.bt_minimizar.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"\n"
"QFrame {\n"
"background-color: rgb(0,0,0)\n"
"}\n"
"\n"
"QpushButton{\n"
"background-color:#000000ff;\n"
"border-radius:20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(53,53,79);\n"
"border-radius:20px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../Imagenes/minizar.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.bt_minimizar)

        self.bt_restaurar = QPushButton(self.frame_superior)
        self.bt_restaurar.setObjectName(u"bt_restaurar")
        self.bt_restaurar.setMinimumSize(QSize(40, 35))
        self.bt_restaurar.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"../Imagenes/mini.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_restaurar.setIcon(icon2)
        self.bt_restaurar.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.bt_restaurar)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMinimumSize(QSize(40, 35))
        self.bt_maximizar.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u"../Imagenes/agrandar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.bt_maximizar)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMinimumSize(QSize(40, 35))
        self.bt_cerrar.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u"../Imagenes/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.bt_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(40, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"background-color : rgb(53,53,79);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"font:87 12pt \"Arial Black\";\n"
"background-color : #000000ff;\n"
"color : rgb(20,200,220);\n"
"border-radius:5px;\n"
"border :1px solid white;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bt_uno = QPushButton(self.frame_2)
        self.bt_uno.setObjectName(u"bt_uno")
        self.bt_uno.setLayoutDirection(Qt.RightToLeft)
        self.bt_uno.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";\n"
"border-bottom-color: rgb(65, 195, 195);")
        icon5 = QIcon()
        icon5.addFile(u"qss.py/piston.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_uno.setIcon(icon5)
        self.bt_uno.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.bt_uno)

        self.bt_dos = QPushButton(self.frame_2)
        self.bt_dos.setObjectName(u"bt_dos")
        self.bt_dos.setLayoutDirection(Qt.RightToLeft)
        self.bt_dos.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";\n"
"border-bottom-color: rgb(52, 157, 157);\n"
"")
        self.bt_dos.setIcon(icon5)
        self.bt_dos.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.bt_dos)

        self.bt_tres = QPushButton(self.frame_2)
        self.bt_tres.setObjectName(u"bt_tres")
        self.bt_tres.setLayoutDirection(Qt.RightToLeft)
        self.bt_tres.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";\n"
"border-bottom-color: rgb(57, 170, 170);\n"
"")
        self.bt_tres.setIcon(icon5)
        self.bt_tres.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.bt_tres)

        self.bt_cuatro = QPushButton(self.frame_2)
        self.bt_cuatro.setObjectName(u"bt_cuatro")
        self.bt_cuatro.setLayoutDirection(Qt.RightToLeft)
        self.bt_cuatro.setStyleSheet(u"font: 10pt \"Microsoft YaHei UI\";\n"
"border-bottom-color: rgb(54, 163, 163);\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"qss.py/paro.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cuatro.setIcon(icon6)
        self.bt_cuatro.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.bt_cuatro)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Paginas = QFrame(self.frame_4)
        self.frame_Paginas.setObjectName(u"frame_Paginas")
        self.frame_Paginas.setStyleSheet(u"QFrame {\n"
"background-color : rgb(53,53,79);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"font:87 12pt \"Arial Black\";\n"
"background-color : #000000ff;\n"
"color : rgb(20,200,220);\n"
"border-radius:5px;\n"
"border :1px solid white;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}")
        self.frame_Paginas.setFrameShape(QFrame.StyledPanel)
        self.frame_Paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_Paginas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_8 = QFrame(self.frame_Paginas)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame {\n"
"background-color : rgb(53,53,79);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"font:87 12pt \"Arial Black\";\n"
"background-color : #000000ff;\n"
"color : rgb(20,200,220);\n"
"border-radius:5px;\n"
"border :1px solid white;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bt_meno_uno = QPushButton(self.frame_8)
        self.bt_meno_uno.setObjectName(u"bt_meno_uno")
        icon7 = QIcon()
        icon7.addFile(u"../Imagenes/izquierda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_meno_uno.setIcon(icon7)
        self.bt_meno_uno.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.bt_meno_uno)

        self.bt_menu_dos = QPushButton(self.frame_8)
        self.bt_menu_dos.setObjectName(u"bt_menu_dos")
        icon8 = QIcon()
        icon8.addFile(u"../Imagenes/derechz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu_dos.setIcon(icon8)
        self.bt_menu_dos.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.bt_menu_dos)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_Paginas)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.toolBox = QToolBox(self.frame_7)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBox::tab{\n"
"background-color : rgb(255,255,255);\n"
"border-radius:5px;\n"
"olor : rgb(0,0,0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"QToolBox::tab:selected{\n"
"background-color : rgb(20,200,220);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"olor : rgb(0,0,0);\n"
"}\n"
"\n"
"QPushButton{\n"
"font:87 12pt \"Arial Black\";\n"
"background-color : #000000ff;\n"
"color : rgb(20,200,220);\n"
"border-radius:5px;\n"
"border :1px solid white;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color:black;\n"
"}")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 98, 28))
        self.pushButton = QPushButton(self.page_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 50, 93, 28))
        self.pushButton_2 = QPushButton(self.page_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 120, 93, 28))
        self.toolBox.addItem(self.page_5, u"Piston 1")
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setGeometry(QRect(0, 0, 98, 28))
        self.pushButton_3 = QPushButton(self.page_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(60, 30, 93, 28))
        self.pushButton_4 = QPushButton(self.page_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 80, 93, 28))
        self.toolBox.addItem(self.page_7, u"Piston 2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 98, 28))
        self.pushButton_8 = QPushButton(self.page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(60, 70, 93, 28))
        self.pushButton_9 = QPushButton(self.page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(60, 130, 93, 28))
        self.toolBox.addItem(self.page, u"Piston 3")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 220, 264))
        self.pushButton_6 = QPushButton(self.page_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(60, 50, 93, 28))
        self.pushButton_7 = QPushButton(self.page_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(60, 110, 93, 28))
        self.toolBox.addItem(self.page_6, u"Boton de Paro")

        self.verticalLayout_7.addWidget(self.toolBox)


        self.verticalLayout.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame_Paginas)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color: rgb(53,53,79);\n"
"}\n"
"\n"
"QlLabel{\n"
"font: 87  12pt \"Arial Black\";\n"
"background-color:#000000ff;\n"
"color: rgb(20,200,220);\n"
"border:0px solid #14C8DC;\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.Panel)
        self.PaginaUno = QWidget()
        self.PaginaUno.setObjectName(u"PaginaUno")
        self.verticalLayout_8 = QVBoxLayout(self.PaginaUno)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.PaginaUno)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"../Imagenes/prueba 1.webp"))

        self.verticalLayout_8.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.PaginaUno)
        self.PaginaDos = QWidget()
        self.PaginaDos.setObjectName(u"PaginaDos")
        self.verticalLayout_9 = QVBoxLayout(self.PaginaDos)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.PaginaDos)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../Imagenes/prueba 1.webp"))
        self.label_3.setIndent(0)

        self.verticalLayout_9.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.PaginaDos)
        self.PaginaTres = QWidget()
        self.PaginaTres.setObjectName(u"PaginaTres")
        self.verticalLayout_10 = QVBoxLayout(self.PaginaTres)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_4 = QLabel(self.PaginaTres)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u"../Imagenes/prueba 1.webp"))

        self.verticalLayout_10.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.PaginaTres)
        self.PaginaCuatro = QWidget()
        self.PaginaCuatro.setObjectName(u"PaginaCuatro")
        self.verticalLayout_11 = QVBoxLayout(self.PaginaCuatro)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.PaginaCuatro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(300, 16777215))
        self.label_5.setStyleSheet(u"background-color: rgb(69, 206, 206);")
        self.label_5.setPixmap(QPixmap(u"../Imagenes/stop.png"))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_5)

        self.stackedWidget.addWidget(self.PaginaCuatro)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Menu Dinamico", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_uno.setText(QCoreApplication.translate("MainWindow", u"Piston 1", None))
        self.bt_dos.setText(QCoreApplication.translate("MainWindow", u"Piston 2", None))
        self.bt_tres.setText(QCoreApplication.translate("MainWindow", u"Piston 3", None))
        self.bt_cuatro.setText(QCoreApplication.translate("MainWindow", u"Boton de Paro", None))
        self.bt_meno_uno.setText("")
        self.bt_menu_dos.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Subir", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Bajar", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"Piston 1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Adelante", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), QCoreApplication.translate("MainWindow", u"Piston 2", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Adelante", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Atr\u00e1s", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Piston 3", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Si", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"Boton de Paro", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
    # retranslateUi

