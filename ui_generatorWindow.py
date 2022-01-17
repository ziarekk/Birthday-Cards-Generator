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


class Ui_GeneratorWindow(object):
    def setupUi(self, GeneratorWindow):
        if not GeneratorWindow.objectName():
            GeneratorWindow.setObjectName(u"GeneratorWindow")
        GeneratorWindow.resize(530, 267)
        self.centralwidget = QWidget(GeneratorWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Kinnari")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.nameEdit = QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName(u"nameEdit")
        self.nameEdit.setFont(font)

        self.verticalLayout.addWidget(self.nameEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 203, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.generateCard = QPushButton(self.centralwidget)
        self.generateCard.setObjectName(u"generateCard")
        font1 = QFont()
        font1.setFamily(u"Kinnari")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.generateCard.setFont(font1)
        self.generateCard.setCursor(QCursor(Qt.PointingHandCursor))
        self.generateCard.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.generateCard)

        GeneratorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GeneratorWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 22))
        GeneratorWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GeneratorWindow)
        self.statusbar.setObjectName(u"statusbar")
        GeneratorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GeneratorWindow)

        QMetaObject.connectSlotsByName(GeneratorWindow)
    # setupUi

    def retranslateUi(self, GeneratorWindow):
        GeneratorWindow.setWindowTitle(QCoreApplication.translate("GeneratorWindow", u"Birthday Card Generator", None))
        self.label.setText(QCoreApplication.translate("GeneratorWindow", u"Type here name of the person that you want to send wishes...", None))
        self.nameEdit.setText("")
        self.generateCard.setText(QCoreApplication.translate("GeneratorWindow", u"Generate Card!", None))
    # retranslateUi

