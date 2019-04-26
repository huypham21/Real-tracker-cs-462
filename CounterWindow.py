# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CounterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 35, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 145, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lcdNumber_Count = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_Count.setGeometry(QtCore.QRect(200, 35, 50, 50))
        self.lcdNumber_Count.setObjectName("lcdNumber_Count")
        self.lcdNumber_Total = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_Total.setGeometry(QtCore.QRect(200, 90, 50, 50))
        self.lcdNumber_Total.setObjectName("lcdNumber_Total")
        self.lcdNumber_Average = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_Average.setGeometry(QtCore.QRect(200, 145, 50, 50))
        self.lcdNumber_Average.setObjectName("lcdNumber_Average")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(0, 225, 300, 50))
        self.progressBar.setStatusTip("")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 195, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.optionsButton = QtWidgets.QPushButton(Dialog)
        self.optionsButton.setGeometry(QtCore.QRect(0, 285, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.optionsButton.setFont(font)
        self.optionsButton.setObjectName("optionsButton")
        self.quitButton = QtWidgets.QPushButton(Dialog)
        self.quitButton.setGeometry(QtCore.QRect(0, 335, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 300, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "People Currently:"))
        self.label_2.setText(_translate("Dialog", "Total Attendance:"))
        self.label_3.setText(_translate("Dialog", "Average Number Present:"))
        self.progressBar.setWhatsThis(_translate("Dialog", "Room Capacity"))
        self.label_4.setText(_translate("Dialog", "Room Occupancy:"))
        self.optionsButton.setText(_translate("Dialog", "Options"))
        self.quitButton.setText(_translate("Dialog", "Quit"))
        self.label_5.setText(_translate("Dialog", "Event Name"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
