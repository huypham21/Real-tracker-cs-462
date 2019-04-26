# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OptionsMenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

#Default values for counter system
roomOcc = 200 
EvName = "Event Name"


class Ui_Options(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 200)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(0, 25, 200, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(25, 0, 150, 25))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 60, 200, 25))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(55, 80, 80, 25))
        self.spinBox.setAccelerated(True)
        self.spinBox.setMaximum(1000)
        self.spinBox.setProperty("value", 200)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 120, 200, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setAutoDefault(False)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        self.spinBox.valueChanged.connect(self.valChange)
        self.lineEdit.returnPressed.connect(self.nameChange)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Event Name"))
        self.label.setText(_translate("Dialog", "Total Room Occupancy"))
        self.pushButton.setText(_translate("Dialog", "Done"))

    def valChange(self):
        roomOcc = self.spinBox.value()
        print("New Room Occupancy: " +str(roomOcc))

    def nameChange(self):
        EvName = self.lineEdit.text()
        self.lineEdit.setStyleSheet("background-color: rgb(85, 0, 0); color: rgb(255,255,255)")
        QtCore.QTimer.singleShot(250, lambda :self.lineEdit.setStyleSheet("background-color: rgb(255,255,255); color: rgb(0,0,0)") )
        self.lineEdit.setText("")
        print("New event name: " +EvName)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Options()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
