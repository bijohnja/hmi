# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hmi1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 140, 318, 301))

        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(4)

        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)

        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)

        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.lcdsa2 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdsa2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lcdsa2.setAutoFillBackground(False)

        self.lcdsa2.setObjectName("lcdsa2")
        self.gridLayout.addWidget(self.lcdsa2, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)

        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)

        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.sa2button = QtWidgets.QPushButton(self.gridLayoutWidget)

        self.sa2button.setObjectName("sa2button")
        self.gridLayout.addWidget(self.sa2button, 5, 1, 1, 1)
        self.sa1button = QtWidgets.QPushButton(self.gridLayoutWidget)

        self.sa1button.setObjectName("sa1button")
        self.gridLayout.addWidget(self.sa1button, 3, 1, 1, 1)
        self.lcdsa1 = QtWidgets.QLCDNumber(self.gridLayoutWidget)

        self.lcdsa1.setObjectName("lcdsa1")
        self.gridLayout.addWidget(self.lcdsa1, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(140, 460, 291, 16))
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(140, 110, 291, 16))
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(110, 130, 20, 331))
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(450, 130, 20, 331))
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_4.setObjectName("line_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 60, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setLineWidth(3)

        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #metodos para los botones de las señales digitales 
        self.sa1button.clicked.connect(self.activar_sd1)
        self.sa2button.clicked.connect(self.activar_sd2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Señal Analoga 2"))
        self.label_4.setText(_translate("MainWindow", "Señal Digital 2"))
        self.label.setText(_translate("MainWindow", "Señal Analoga 1"))
        self.label_3.setText(_translate("MainWindow", "Señal Digital 1"))
        self.sa2button.setText(_translate("MainWindow", "Activar"))
        self.sa1button.setText(_translate("MainWindow", "Activar"))
        self.label_5.setText(_translate("MainWindow", "H.M.I."))
    
    #metodos para agregar las 
    def activar_sd1(self):
        raise

    def activar_sd2(self):
        raise
    
    def activar_sa1(self):
        raise

    def activar_sa2(self):
        raise


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
