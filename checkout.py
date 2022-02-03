from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pickle
import sys
import os
from subprocess import call
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtSql
from PyQt5.QtSql import *
import MySQLdb as mdb
import time
import datetime
import smtplib

class save:
    def __init__(self, PhyName, PhyID, Contact,Mail):
        self.name=PhyName
        self.PhyID=PhyID
        self.Contact=Contact
        self.email=Mail



class Ui_MainWindow(object):
    def file_save(self):
        # print("hello")
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        PhyName = self.nameedit.text()
        # PhyID = self.addedit.text()
        Contact = (self.cno_2.text())
        # Mail = self.daysedit.text()
        Physician = self.PHYSICIANedit.text()
        self.db = mdb.connect('localhost', 'root', '', 'smartworkflow')
        self.c=self.db.cursor()
        self.c1=self.db.cursor()
        
        self.c.execute("UPDATE patient SET Check_out = %s WHERE name= %s and physician=%s and phone=%s",(now,PhyName,Physician,Contact))
        
        
        data1=['Name:','Physician ID:', 'Phone:' ,'Email:','PHYSICIAN:','Check-in:','Check-out:']
        
        
        self.c1.execute("select * from patient where name= %s and physician=%s and phone=%s",(PhyName,Physician,Contact))
        self.data=self.c1.fetchone()
        if not self.data:
            self.listWidget.addItem('Check patient details once again')
            return None
        self.listWidget.addItem("PATIENT DETAILS")
        for i in range(0,7):
                self.listWidget.addItem(data1[i] +" "+ str(self.data[i]))
        
        self.db.commit()
        self.c.close()
        self.db.close()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(892, 639)
        MainWindow.setMinimumSize(QtCore.QSize(892, 639))
        MainWindow.setMaximumSize(QtCore.QSize(892, 639))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 901, 641))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{background-color: #3F9CED\n"
";\n"
"\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.INFO = QtWidgets.QLabel(self.frame)
        self.INFO.setGeometry(QtCore.QRect(120, 0, 611, 51))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.INFO.setFont(font)
        self.INFO.setObjectName("INFO")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(50, 40, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.cno = QtWidgets.QLabel(self.frame)
        self.cno.setGeometry(QtCore.QRect(50, 120, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cno.setFont(font)
        self.cno.setObjectName("cno")
        self.PhyID = QtWidgets.QLabel(self.frame)
        self.PhyID.setGeometry(QtCore.QRect(50, 80, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.PhyID.setFont(font)
        self.PhyID.setObjectName("PhyID")
        
        
        

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 199, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.nameedit = QtWidgets.QLineEdit(self.frame)
        self.nameedit.setGeometry(QtCore.QRect(430, 60, 321, 20))
        self.nameedit.setStyleSheet("")
        self.nameedit.setObjectName("nameedit")




        self.cno_2 = QtWidgets.QLineEdit(self.frame)
        self.cno_2.setGeometry(QtCore.QRect(430, 140, 321, 20))
        self.cno_2.setStyleSheet("")
        self.cno_2.setObjectName("cno_2")

      

        self.PHYSICIANedit = QtWidgets.QLineEdit(self.frame)
        self.PHYSICIANedit.setGeometry(QtCore.QRect(430, 220, 321, 20))
        self.PHYSICIANedit.setStyleSheet("")
        self.PHYSICIANedit.setObjectName("daysedit")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(690, 380, 91, 31))
        self.pushButton.setStyleSheet("QPushButton:active:after{\n"
"\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    opacity: 1;\n"
"    transition: 1s;\n"
"-webkit-transition-duration: 0.4s;\n"
"    transition-duration: 0.4s;\n"
"\n"
"    background-color:#19707D;\n"
"    color: white;\n"
"\n"
"   }\n"
"")
        self.pushButton.clicked.connect(self.file_save)
        self.pushButton.setObjectName("pushButton")


        self.listWidget = QtWidgets.QListWidget(self.frame)

        self.listWidget.setGeometry(QtCore.QRect(20, 420, 871, 211))
        self.listWidget.setStyleSheet("QListView{\n"
"background-color: white;\n"
"\n"
"border-radius:10px;\n"
"padding:10px;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"")
        self.listWidget.setObjectName("listWidget")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patient Check-Out"))
        self.INFO.setText(_translate("MainWindow", "Enter Patient Details"))
        self.name.setText(_translate("MainWindow", "ENTER PATIENT NAME"))
        self.cno.setText(_translate("MainWindow", "ENTER PATIENT CONTACT NO."))
        self.label_3.setText(_translate("MainWindow", "ENTER PHYSICIAN"))
        self.pushButton.setText(_translate("MainWindow", "✔"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

