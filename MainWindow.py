# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(337, 245)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Record_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Record_Button.setGeometry(QtCore.QRect(40, 170, 75, 23))
        self.Record_Button.setObjectName("Record_Button")
        self.Pause_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Pause_Button.setEnabled(False)
        self.Pause_Button.setGeometry(QtCore.QRect(220, 170, 75, 23))
        self.Pause_Button.setObjectName("Pause_Button")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 20, 261, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Text_plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.Text_plainTextEdit.setObjectName("Text_plainTextEdit")
        self.gridLayout.addWidget(self.Text_plainTextEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 337, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Record_Button.setText(_translate("MainWindow", "开始录音"))
        self.Pause_Button.setText(_translate("MainWindow", "暂停"))
        self.menu.setTitle(_translate("MainWindow", "选项"))
