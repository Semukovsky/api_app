# Form implementation generated from reading ui file '.\ui_file.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RB_1 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.RB_1.setGeometry(QtCore.QRect(30, 10, 158, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RB_1.setFont(font)
        self.RB_1.setObjectName("RB_1")
        self.RB_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.RB_2.setGeometry(QtCore.QRect(30, 40, 158, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RB_2.setFont(font)
        self.RB_2.setObjectName("RB_2")
        self.RB_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.RB_3.setGeometry(QtCore.QRect(30, 70, 158, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RB_3.setFont(font)
        self.RB_3.setObjectName("RB_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.object = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.object.setGeometry(QtCore.QRect(10, 140, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.object.setFont(font)
        self.object.setObjectName("object")
        self.search = QtWidgets.QPushButton(parent=self.centralwidget)
        self.search.setGeometry(QtCore.QRect(10, 170, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.flip = QtWidgets.QPushButton(parent=self.centralwidget)
        self.flip.setGeometry(QtCore.QRect(10, 520, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.flip.setFont(font)
        self.flip.setObjectName("flip")
        self.information = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.information.setGeometry(QtCore.QRect(10, 210, 181, 271))
        self.information.setObjectName("information")
        self.index = QtWidgets.QPushButton(parent=self.centralwidget)
        self.index.setGeometry(QtCore.QRect(10, 490, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.index.setFont(font)
        self.index.setObjectName("index")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RB_1.setText(_translate("MainWindow", "схема"))
        self.RB_2.setText(_translate("MainWindow", "спутник"))
        self.RB_3.setText(_translate("MainWindow", "гибрид"))
        self.label.setText(_translate("MainWindow", "Требуемый объект:"))
        self.search.setText(_translate("MainWindow", "Искать"))
        self.flip.setText(_translate("MainWindow", "Сбросить"))
        self.index.setText(_translate("MainWindow", "Показать индекс"))
