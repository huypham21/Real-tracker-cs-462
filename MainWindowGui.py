# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowGui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime
#Default values for counter system
roomOcc = 200 
EvName = "Event Name"
avg = 0
currOcc = 0
maxOcc = 0

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


############################################################################
class Ui_New(object):
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
        self.progressBar.setGeometry(QtCore.QRect(0, 235, 300, 50))
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
        self.quitButton.clicked.connect(lambda: self.save(Dialog))
        self.optionsButton.clicked.connect(self.optionMenu)
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
        self.quitButton.setText(_translate("Dialog", "Save and Quit"))
        self.label_5.setText(_translate("Dialog", "Event Name"))
    
    def save(self, Dialog):
        file = open('data.json', 'a')
        date = datetime.datetime.now()
        toWrite = '{"EventName": '+str(EvName) +', "Time": ' +str(date) +', "EndAttend": ' +str(currOcc) +', "AvgAttend": ' +str(avg) +', "MaxAttend": ' +str(maxOcc) +', "RoomOcc": ' +str(roomOcc) +'}\n'
        file.write(toWrite)
        print("Wrote" +toWrite)
        file.close()
        Dialog.close()
    
    def end(self, Dialog):
        self.save
        Dialog.close()
    
    def optionMenu(self):
        opt = QtWidgets.QDialog()
        options = Ui_Options()
        options.setupUi(opt)
        opt.exec_()
    
############################################################################


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startNewButton = QtWidgets.QPushButton(self.centralwidget)
        self.startNewButton.setGeometry(QtCore.QRect(0, 0, 200, 50))
        self.startNewButton.setAutoFillBackground(False)
        self.startNewButton.setObjectName("startNewButton")
        self.optionButton = QtWidgets.QPushButton(self.centralwidget)
        self.optionButton.setGeometry(QtCore.QRect(0, 55, 200, 50))
        self.optionButton.setObjectName("optionButton")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(0, 110, 200, 50))
        self.quitButton.setObjectName("quitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quitButton.clicked.connect(MainWindow.close)
        self.optionButton.clicked.connect(self.optionMenu)
        self.startNewButton.clicked.connect(self.startNew)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startNewButton.setText(_translate("MainWindow", "Start New"))
        self.optionButton.setText(_translate("MainWindow", "Options"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))

    def optionMenu(self):
        opt = QtWidgets.QDialog()
        options = Ui_Options()
        options.setupUi(opt)
        #opt.show()
        opt.exec_()

    def startNew(self):
        new = QtWidgets.QDialog()
        counter = Ui_New()
        counter.setupUi(new)
        new.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
