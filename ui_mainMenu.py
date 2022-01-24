# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(505, 558)
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stack = QStackedWidget(self.centralwidget)
        self.stack.setObjectName(u"stack")
        self.menu = QWidget()
        self.menu.setObjectName(u"menu")
        self.gridLayout = QGridLayout(self.menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.calendarWidget = QCalendarWidget(self.menu)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.calendarWidget, 5, 0, 1, 1)

        self.goCredits = QPushButton(self.menu)
        self.goCredits.setObjectName(u"goCredits")
        font = QFont()
        font.setFamily(u"Kinnari")
        font.setPointSize(16)
        self.goCredits.setFont(font)

        self.gridLayout.addWidget(self.goCredits, 2, 0, 1, 1)

        self.label = QLabel(self.menu)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"aakar")
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.menu)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"aakar")
        font2.setPointSize(14)
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.goGenerator = QPushButton(self.menu)
        self.goGenerator.setObjectName(u"goGenerator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.goGenerator.sizePolicy().hasHeightForWidth())
        self.goGenerator.setSizePolicy(sizePolicy1)
        self.goGenerator.setFont(font)

        self.gridLayout.addWidget(self.goGenerator, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.stack.addWidget(self.menu)
        self.credits = QWidget()
        self.credits.setObjectName(u"credits")
        self.verticalLayout_3 = QVBoxLayout(self.credits)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.returnMenu = QPushButton(self.credits)
        self.returnMenu.setObjectName(u"returnMenu")

        self.horizontalLayout.addWidget(self.returnMenu)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.credits)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Kinnari")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.credits)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamily(u"Kinnari")
        font4.setPointSize(16)
        font4.setItalic(True)
        self.label_4.setFont(font4)
        self.label_4.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.label_6 = QLabel(self.credits)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setItalic(True)
        self.label_6.setFont(font5)
        self.label_6.setMargin(4)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_5 = QLabel(self.credits)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setMargin(4)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_8 = QLabel(self.credits)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setMargin(4)

        self.verticalLayout_2.addWidget(self.label_8)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.stack.addWidget(self.credits)

        self.verticalLayout.addWidget(self.stack)

        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 505, 22))
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainMenu)
        self.statusbar.setObjectName(u"statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenu)

        self.stack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"MainWindow", None))
        self.goCredits.setText(QCoreApplication.translate("MainMenu", u"Author and Credits", None))
        self.label.setText(QCoreApplication.translate("MainMenu", u"Birthday Cards Generator v.1.1", None))
        self.label_2.setText(QCoreApplication.translate("MainMenu", u"Today is:", None))
        self.goGenerator.setText(QCoreApplication.translate("MainMenu", u"Go to generator", None))
        self.returnMenu.setText(QCoreApplication.translate("MainMenu", u"Return to Main Menu", None))
        self.label_3.setText(QCoreApplication.translate("MainMenu", u"It is a semestral project created for 21Z PIPR classes on WUT. Designed and created by Karol Ziarek.", None))
        self.label_4.setText(QCoreApplication.translate("MainMenu", u"Special thanks to creators of frames and fonts used in the project:", None))
        self.label_6.setText(QCoreApplication.translate("MainMenu", u"Valentine Surprise by:    https://aencreativestudio.com/", None))
        self.label_5.setText(QCoreApplication.translate("MainMenu", u"Lovely Balloon by:          https://aencreativestudio.com/", None))
        self.label_8.setText(QCoreApplication.translate("MainMenu", u"Fantastic Frames by:     https://www.pngtree.com/", None))
    # retranslateUi

