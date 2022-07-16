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
        MainWindow.resize(788, 625)
        self.action_Close = QAction(MainWindow)
        self.action_Close.setObjectName(u"action_Close")
        self.action_About_Qt = QAction(MainWindow)
        self.action_About_Qt.setObjectName(u"action_About_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: white;")
        self.verticalLayout_12 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_game = QFrame(self.centralwidget)
        self.frame_game.setObjectName(u"frame_game")
        self.frame_game.setEnabled(True)
        self.frame_game.setFrameShape(QFrame.StyledPanel)
        self.frame_game.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_game)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_state = QLabel(self.frame_game)
        self.label_state.setObjectName(u"label_state")
        font = QFont()
        font.setPointSize(21)
        self.label_state.setFont(font)
        self.label_state.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_state)

        self.verticalSpacer = QSpacerItem(0, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.line = QFrame(self.frame_game)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_10.addWidget(self.line)

        self.verticalSpacer_5 = QSpacerItem(0, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.label_player_2_name = QLabel(self.frame_game)
        self.label_player_2_name.setObjectName(u"label_player_2_name")
        font1 = QFont()
        font1.setPointSize(18)
        self.label_player_2_name.setFont(font1)
        self.label_player_2_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_player_2_name)


        self.verticalLayout_7.addLayout(self.verticalLayout_10)

        self.verticalSpacer_3 = QSpacerItem(0, 16, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_player_2_kalah = QPushButton(self.frame_game)
        self.pushButton_player_2_kalah.setObjectName(u"pushButton_player_2_kalah")
        self.pushButton_player_2_kalah.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_player_2_kalah.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_kalah.setSizePolicy(sizePolicy)
        self.pushButton_player_2_kalah.setMinimumSize(QSize(100, 160))
        self.pushButton_player_2_kalah.setMaximumSize(QSize(100, 160))
        font2 = QFont()
        font2.setPointSize(21)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_player_2_kalah.setFont(font2)
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
        self.label = QLabel(self.frame_game)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(17)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: blue;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.pushButton_player_2_cup_6 = QPushButton(self.frame_game)
        self.pushButton_player_2_cup_6.setObjectName(u"pushButton_player_2_cup_6")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_6.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_6.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_6.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_6.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_6.setFont(font2)
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

        self.pushButton_player_1_cup_1 = QPushButton(self.frame_game)
        self.pushButton_player_1_cup_1.setObjectName(u"pushButton_player_1_cup_1")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_1.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_1.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_1.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_1.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_1.setFont(font2)
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

        self.label_7 = QLabel(self.frame_game)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: red")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_game)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: blue;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.pushButton_player_2_cup_5 = QPushButton(self.frame_game)
        self.pushButton_player_2_cup_5.setObjectName(u"pushButton_player_2_cup_5")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_5.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_5.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_5.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_5.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_5.setFont(font2)
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

        self.pushButton_player_1_cup_2 = QPushButton(self.frame_game)
        self.pushButton_player_1_cup_2.setObjectName(u"pushButton_player_1_cup_2")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_2.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_2.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_2.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_2.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_2.setFont(font2)
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

        self.label_8 = QLabel(self.frame_game)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: red")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_game)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: blue;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.pushButton_player_2_cup_4 = QPushButton(self.frame_game)
        self.pushButton_player_2_cup_4.setObjectName(u"pushButton_player_2_cup_4")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_4.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_4.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_4.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_4.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_4.setFont(font2)
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

        self.pushButton_player_1_cup_3 = QPushButton(self.frame_game)
        self.pushButton_player_1_cup_3.setObjectName(u"pushButton_player_1_cup_3")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_3.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_3.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_3.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_3.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_3.setFont(font2)
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

        self.label_9 = QLabel(self.frame_game)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: red")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_9)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_game)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: blue;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.pushButton_player_2_cup_3 = QPushButton(self.frame_game)
        self.pushButton_player_2_cup_3.setObjectName(u"pushButton_player_2_cup_3")
        self.pushButton_player_2_cup_3.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_3.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_3.setFont(font2)
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

        self.pushButton_player_1_cup_4 = QPushButton(self.frame_game)
        self.pushButton_player_1_cup_4.setObjectName(u"pushButton_player_1_cup_4")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_4.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_4.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_4.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_4.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_4.setFont(font2)
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

        self.label_10 = QLabel(self.frame_game)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"color: red")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_10)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.frame_game)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: blue;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.pushButton_player_2_cup_2 = QPushButton(self.frame_game)
        self.pushButton_player_2_cup_2.setObjectName(u"pushButton_player_2_cup_2")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_2.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_2.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_2.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_2.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_2.setFont(font2)
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

        self.pushButton_player_1_cup_5 = QPushButton(self.frame_game)
        self.pushButton_player_1_cup_5.setObjectName(u"pushButton_player_1_cup_5")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_5.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_5.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_5.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_5.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_5.setFont(font2)
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

        self.label_11 = QLabel(self.frame_game)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"color: red")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(self.frame_game)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: blue;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6)

        self.pushButton_player_2_cup_1 = QPushButton(self.frame_game)
        self.pushButton_player_2_cup_1.setObjectName(u"pushButton_player_2_cup_1")
        sizePolicy.setHeightForWidth(self.pushButton_player_2_cup_1.sizePolicy().hasHeightForWidth())
        self.pushButton_player_2_cup_1.setSizePolicy(sizePolicy)
        self.pushButton_player_2_cup_1.setMinimumSize(QSize(80, 80))
        self.pushButton_player_2_cup_1.setMaximumSize(QSize(80, 80))
        self.pushButton_player_2_cup_1.setFont(font2)
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

        self.pushButton_player_1_cup_6 = QPushButton(self.frame_game)
        self.pushButton_player_1_cup_6.setObjectName(u"pushButton_player_1_cup_6")
        sizePolicy.setHeightForWidth(self.pushButton_player_1_cup_6.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_cup_6.setSizePolicy(sizePolicy)
        self.pushButton_player_1_cup_6.setMinimumSize(QSize(80, 80))
        self.pushButton_player_1_cup_6.setMaximumSize(QSize(80, 80))
        self.pushButton_player_1_cup_6.setFont(font2)
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

        self.label_12 = QLabel(self.frame_game)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"color: red")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_12)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(8, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pushButton_player_1_kalah = QPushButton(self.frame_game)
        self.pushButton_player_1_kalah.setObjectName(u"pushButton_player_1_kalah")
        self.pushButton_player_1_kalah.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_player_1_kalah.sizePolicy().hasHeightForWidth())
        self.pushButton_player_1_kalah.setSizePolicy(sizePolicy)
        self.pushButton_player_1_kalah.setMinimumSize(QSize(100, 160))
        self.pushButton_player_1_kalah.setMaximumSize(QSize(100, 160))
        self.pushButton_player_1_kalah.setFont(font2)
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

        self.verticalSpacer_4 = QSpacerItem(0, 16, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_player_1_name = QLabel(self.frame_game)
        self.label_player_1_name.setObjectName(u"label_player_1_name")
        font4 = QFont()
        font4.setPointSize(19)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_player_1_name.setFont(font4)
        self.label_player_1_name.setStyleSheet(u"color: red; font-size: 19pt; font-weight:bold;")
        self.label_player_1_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_player_1_name)


        self.verticalLayout_7.addLayout(self.verticalLayout_11)


        self.verticalLayout_9.addLayout(self.verticalLayout_7)


        self.verticalLayout_12.addWidget(self.frame_game)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_start_game = QPushButton(self.centralwidget)
        self.pushButton_start_game.setObjectName(u"pushButton_start_game")
        self.pushButton_start_game.setEnabled(True)
        self.pushButton_start_game.setMinimumSize(QSize(500, 100))
        self.pushButton_start_game.setMaximumSize(QSize(500, 100))
        font5 = QFont()
        font5.setPointSize(15)
        self.pushButton_start_game.setFont(font5)

        self.horizontalLayout.addWidget(self.pushButton_start_game)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 788, 21))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"pyKalah v1.5.0", None))
        self.action_Close.setText(QCoreApplication.translate("MainWindow", u"&Close", None))
        self.action_About_Qt.setText(QCoreApplication.translate("MainWindow", u"&About Qt", None))
        self.label_state.setText(QCoreApplication.translate("MainWindow", u"Welcome to Kalah", None))
        self.label_player_2_name.setText(QCoreApplication.translate("MainWindow", u"Player 2", None))
        self.pushButton_player_2_kalah.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"[6]", None))
        self.pushButton_player_2_cup_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_1.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"[1]", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"[5]", None))
        self.pushButton_player_2_cup_5.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_2.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"[2]", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"[4]", None))
        self.pushButton_player_2_cup_4.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_3.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"[3]", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"[3]", None))
        self.pushButton_player_2_cup_3.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_4.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"[4]", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"[2]", None))
        self.pushButton_player_2_cup_2.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_5.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"[5]", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"[1]", None))
        self.pushButton_player_2_cup_1.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_player_1_cup_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"[6]", None))
        self.pushButton_player_1_kalah.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_player_1_name.setText(QCoreApplication.translate("MainWindow", u"Player 1", None))
        self.pushButton_start_game.setText(QCoreApplication.translate("MainWindow", u"Start Game", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Help.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
    # retranslateUi

