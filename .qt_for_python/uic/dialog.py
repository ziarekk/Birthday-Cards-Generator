# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dialogWindow(object):
    def setupUi(self, dialogWindow):
        if not dialogWindow.objectName():
            dialogWindow.setObjectName(u"dialogWindow")
        dialogWindow.resize(657, 550)
        self.centralwidget = QWidget(dialogWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Yrsa Medium")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.imageViewer = QLabel(self.centralwidget)
        self.imageViewer.setObjectName(u"imageViewer")
        self.imageViewer.setMinimumSize(QSize(626, 417))
        self.imageViewer.setMaximumSize(QSize(626, 417))

        self.verticalLayout.addWidget(self.imageViewer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.closeTab = QPushButton(self.centralwidget)
        self.closeTab.setObjectName(u"closeTab")

        self.horizontalLayout.addWidget(self.closeTab)

        self.saveImage = QPushButton(self.centralwidget)
        self.saveImage.setObjectName(u"saveImage")

        self.horizontalLayout.addWidget(self.saveImage)


        self.verticalLayout.addLayout(self.horizontalLayout)

        dialogWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dialogWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 657, 22))
        dialogWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dialogWindow)
        self.statusbar.setObjectName(u"statusbar")
        dialogWindow.setStatusBar(self.statusbar)

        self.retranslateUi(dialogWindow)

        QMetaObject.connectSlotsByName(dialogWindow)
    # setupUi

    def retranslateUi(self, dialogWindow):
        dialogWindow.setWindowTitle(QCoreApplication.translate("dialogWindow", u"Birthday Card", None))
        self.label.setText(QCoreApplication.translate("dialogWindow", u"Here is your generated birthday card!", None))
        self.imageViewer.setText("")
        self.closeTab.setText(QCoreApplication.translate("dialogWindow", u"Close", None))
        self.saveImage.setText(QCoreApplication.translate("dialogWindow", u"Save Image", None))
    # retranslateUi

