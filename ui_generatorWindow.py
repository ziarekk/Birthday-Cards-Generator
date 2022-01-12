# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generatorWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(415, 200)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.nameEdit = QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName(u"nameEdit")

        self.verticalLayout.addWidget(self.nameEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 203, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.generateCard = QPushButton(self.centralwidget)
        self.generateCard.setObjectName(u"generateCard")
        font = QFont()
        font.setFamily(u"aakar")
        font.setPointSize(12)
        self.generateCard.setFont(font)

        self.verticalLayout_2.addWidget(self.generateCard)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 415, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Birthday Card Generator", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Type here name of the person that you want to send wishes...", None))
        self.nameEdit.setText("")
        self.generateCard.setText(QCoreApplication.translate("MainWindow", u"Generate Card!", None))
    # retranslateUi

