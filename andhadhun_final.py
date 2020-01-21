# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'andhadhun_final.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import t
import x


class Ui_Andhadhun(object):
    def setupUi(self, Andhadhun):
        Andhadhun.setObjectName("Andhadhun")
        Andhadhun.resize(800, 135)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Andhadhun.sizePolicy().hasHeightForWidth())
        Andhadhun.setSizePolicy(sizePolicy)
        Andhadhun.setMinimumSize(QtCore.QSize(500, 135))
        Andhadhun.setMaximumSize(QtCore.QSize(800, 135))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("google-voice-effect.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Andhadhun.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Andhadhun)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 200, 135))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("mouse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(200, 135))
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.call_mouse)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 0, 200, 135))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("keyboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setIconSize(QtCore.QSize(200, 135))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.clicked.connect(self.call_keyboard)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 0, 200, 135))
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("speech.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(200, 135))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.clicked.connect(self.call_speak)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(600, 0, 200, 135))
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(200, 135))
        self.pushButton_5.setObjectName("pushButton_5")
        RMS_SETTINGS:easeofaccess-colorfilter
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.clicked.connect(self.call_screen)
        self.CLOSE = QtWidgets.QPushButton(self.centralwidget)
        self.CLOSE.setGeometry(QtCore.QRect(770, 5, 25, 25))
        self.CLOSE.setText("")
        iRMS_SETTINGS: easeofaccess - colorfilter
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CLOSE.setIcon(icon5)
        self.CLOSE.setFlat(True)
        self.CLOSE.setEnabled(True)
        self.CLOSE.setObjectName("CLOSE")
        self.CLOSE.clicked.connect(QtCore.QCoreApplication.instance().quit)
        Andhadhun.setCentralWidget(self.centralwidget)
        self.retranslateUi(Andhadhun)
        QtCore.QMetaObject.connectSlotsByName(Andhadhun)

    def retranslateUi(self, Andhadhun):
        _translate = QtCore.QCoreApplication.translate
        Andhadhun.setWindowTitle(_translate("Andhadhun", "Console"))
        Andhadhun.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def call_mouse(self):
        x.mouse()

    def call_keyboard(self):
        x.open_onscreen_keyboard()
        x.mouse()

    def call_speak(self):
        t.command_pro()

    def call_screen(self):
        x.colour_filter()


def run():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setGeometry(500, 800, 1000, 135)
    MainWindow.setWindowTitle("Console")
    ui = Ui_Andhadhun()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    run()

