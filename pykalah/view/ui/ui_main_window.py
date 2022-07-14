# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
        MainWindow.resize(786, 285)
        self.action_Close = QAction(MainWindow)
        self.action_Close.setObjectName(u"action_Close")
        self.action_About_Qt = QAction(MainWindow)
        self.action_About_Qt.setObjectName(u"action_About_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: white;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_player_2_name = QLabel(self.centralwidget)
        self.label_player_2_name.setObjectName(u"label_player_2_name")
        font = QFont()
        font.setPointSize(18)
        self.label_player_2_name.setFont(font)
        self.label_player_2_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_player_2_name)


        self.verticalLayout_7.addLayout(self.verticalLayout_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_player_2_kalah = QPushButton(self.centralwidget)
        self.pushButton_player_2_kalah.setObjectName(u"pushButton_player_2_kalah")
        self.pushButton_player_2_kalah.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_player_2_kalah.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_kalah.setSizePolicy(sizePolicy)
        self.pushButton_player_2_kalah.setMinimumSize(QSize(100, 160))
        self.pushButton_player_2_kalah.setMaximumSize(QSize(100, 160))
        font1 = QFont()
        font1.setPointSize(21)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_player_2_kalah.setFont(font1)
        self.pushButton_player_2_kalah.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_2_kalah.setStyleSheet(u"QPushButton{\n"
"border: 6px inset grey; \n"
"border-radius: 15px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_player_2_kalah)

        self.horizontalSpacer = QSpacerItem(8, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_player_2_cup_6 = QPushButton(self.centralwidget)
        self.pushButton_player_2_cup_6.setObjectName(u"pushButton_player_2_cup_6")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_6.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_6.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_6.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_6.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_6.setFont(font1)
        self.pushButton_player_2_cup_6.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_2_cup_6.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_player_2_cup_6)

        self.pushButton_player_1_cup_1 = QPushButton(self.centralwidget)
        self.pushButton_player_1_cup_1.setObjectName(u"pushButton_player_1_cup_1")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_1.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_1.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_1.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_1.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_1.setFont(font1)
        self.pushButton_player_1_cup_1.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_1_cup_1.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_player_1_cup_1)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_player_2_cup_5 = QPushButton(self.centralwidget)
        self.pushButton_player_2_cup_5.setObjectName(u"pushButton_player_2_cup_5")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_5.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_5.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_5.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_5.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_5.setFont(font1)
        self.pushButton_player_2_cup_5.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_2_cup_5.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_player_2_cup_5)

        self.pushButton_player_1_cup_2 = QPushButton(self.centralwidget)
        self.pushButton_player_1_cup_2.setObjectName(u"pushButton_player_1_cup_2")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_2.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_2.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_2.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_2.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_2.setFont(font1)
        self.pushButton_player_1_cup_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_1_cup_2.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_player_1_cup_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_player_2_cup_4 = QPushButton(self.centralwidget)
        self.pushButton_player_2_cup_4.setObjectName(u"pushButton_player_2_cup_4")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_4.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_4.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_4.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_4.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_4.setFont(font1)
        self.pushButton_player_2_cup_4.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_2_cup_4.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_player_2_cup_4)

        self.pushButton_player_1_cup_3 = QPushButton(self.centralwidget)
        self.pushButton_player_1_cup_3.setObjectName(u"pushButton_player_1_cup_3")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_3.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_3.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_3.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_3.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_3.setFont(font1)
        self.pushButton_player_1_cup_3.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_1_cup_3.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_player_1_cup_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_player_2_cup_3 = QPushButton(self.centralwidget)
        self.pushButton_player_2_cup_3.setObjectName(u"pushButton_player_2_cup_3")
        self.pushButton_player_2_cup_3.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_3.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_3.setFont(font1)
        self.pushButton_player_2_cup_3.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_2_cup_3.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_player_2_cup_3)

        self.pushButton_player_1_cup_4 = QPushButton(self.centralwidget)
        self.pushButton_player_1_cup_4.setObjectName(u"pushButton_player_1_cup_4")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_4.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_4.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_4.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_4.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_4.setFont(font1)
        self.pushButton_player_1_cup_4.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_1_cup_4.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_player_1_cup_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_player_2_cup_2 = QPushButton(self.centralwidget)
        self.pushButton_player_2_cup_2.setObjectName(u"pushButton_player_2_cup_2")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_2.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_2.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_2.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_2.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_2.setFont(font1)
        self.pushButton_player_2_cup_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_2_cup_2.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_player_2_cup_2)

        self.pushButton_player_1_cup_5 = QPushButton(self.centralwidget)
        self.pushButton_player_1_cup_5.setObjectName(u"pushButton_player_1_cup_5")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_5.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_5.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_5.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_5.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_5.setFont(font1)
        self.pushButton_player_1_cup_5.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_1_cup_5.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_player_1_cup_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_player_2_cup_1 = QPushButton(self.centralwidget)
        self.pushButton_player_2_cup_1.setObjectName(u"pushButton_player_2_cup_1")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_1.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_1.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_1.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_1.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_1.setFont(font1)
        self.pushButton_player_2_cup_1.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_2_cup_1.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton_player_2_cup_1)

        self.pushButton_player_1_cup_6 = QPushButton(self.centralwidget)
        self.pushButton_player_1_cup_6.setObjectName(u"pushButton_player_1_cup_6")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_6.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_6.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_6.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_6.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_6.setFont(font1)
        self.pushButton_player_1_cup_6.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_1_cup_6.setStyleSheet(u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton_player_1_cup_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(8, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_player_1_kalah = QPushButton(self.centralwidget)
        self.pushButton_player_1_kalah.setObjectName(u"pushButton_player_1_kalah")
        self.pushButton_player_1_kalah.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_player_1_kalah.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_kalah.setSizePolicy(sizePolicy)
        self.pushButton_player_1_kalah.setMinimumSize(QSize(100, 160))
        self.pushButton_player_1_kalah.setMaximumSize(QSize(100, 160))
        self.pushButton_player_1_kalah.setFont(font1)
        self.pushButton_player_1_kalah.setFocusPolicy(Qt.NoFocus)
        self.pushButton_player_1_kalah.setStyleSheet(u"QPushButton{\n"
"border: 6px inset grey; \n"
"border-radius: 15px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"}")

        self.verticalLayout_8.addWidget(self.pushButton_player_1_kalah)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_player_1_name = QLabel(self.centralwidget)
        self.label_player_1_name.setObjectName(u"label_player_1_name")
        self.label_player_1_name.setFont(font)
        self.label_player_1_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_player_1_name)


        self.verticalLayout_7.addLayout(self.verticalLayout_11)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 786, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Close)
        self.menu_Help.addAction(self.action_About_Qt)

        self.retranslateUi(MainWindow)
        self.action_Close.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"pyKalah v1.0.0", None))
        self.action_Close.setText(QCoreApplication.translate("MainWindow", u"&Close", None))
        self.action_About_Qt.setText(QCoreApplication.translate("MainWindow", u"&About Qt", None))
        self.label_player_2_name.setText(QCoreApplication.translate("MainWindow", u"Player 2", None))
        self.pushButton_player_2_kalah.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_player_2_cup_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_1.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_2_cup_5.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_2.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_2_cup_4.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_3.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_2_cup_3.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_4.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_2_cup_2.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_5.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_2_cup_1.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_kalah.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_player_1_name.setStyleSheet(QCoreApplication.translate("MainWindow", u"QPushButton{\n"
"border: 5px inset grey;\n"
"border-radius: 40px;\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px inset #445677;\n"
"background-color: #fff;\n"
"font-size: 24pt;\n"
"}", None))
        self.label_player_1_name.setText(QCoreApplication.translate("MainWindow", u"Player 1", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

