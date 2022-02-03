
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
    def __init__(self,PhyName,PhyID,Contact,Mail):
        self.name=PhyName
        self.ID=PhyID
        self.Contact=Contact
        self.email=Mail
class Ui_MainWindow(object):    
    def file_save(self):
        # print("hello")
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        PhyName = self.nameedit.text()
        PhyID = self.addedit.text()
        Contact = (self.pid_2.text())
        Mail = self.emailedit.text()
        
        self.db = mdb.connect('localhost', 'root', '', 'smartworkflow')
        self.c=self.db.cursor()
        self.c1=self.db.cursor()
        self.c.execute("INSERT INTO physician values (%s,%s,%s,%s)",(PhyName,PhyID,Mail,Contact))
        
        self.listWidget.addItem("PHYSICIAN ENTERED SUCCESSFULLY")
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
        self.pid = QtWidgets.QLabel(self.frame)
        self.pid.setGeometry(QtCore.QRect(50, 120, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pid.setFont(font)
        self.pid.setObjectName("pid")
        self.contact = QtWidgets.QLabel(self.frame)
        self.contact.setGeometry(QtCore.QRect(50, 80, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.contact.setFont(font)
        self.contact.setObjectName("contact")
        
        self.email = QtWidgets.QLabel(self.frame)
        self.email.setGeometry(QtCore.QRect(50, 160, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setObjectName("email")
        

        
        self.nameedit = QtWidgets.QLineEdit(self.frame)
        self.nameedit.setGeometry(QtCore.QRect(430, 60, 321, 20))
        self.nameedit.setStyleSheet("")
        self.nameedit.setObjectName("nameedit")






        self.addedit = QtWidgets.QLineEdit(self.frame)
        self.addedit.setGeometry(QtCore.QRect(430, 100, 321, 20))
        self.addedit.setStyleSheet("")
        self.addedit.setObjectName("addedit")


        self.pid_2 = QtWidgets.QLineEdit(self.frame)
        self.pid_2.setGeometry(QtCore.QRect(430, 140, 321, 20))
        self.pid_2.setStyleSheet("")
        self.pid_2.setObjectName("pid_2")

        self.emailedit = QtWidgets.QLineEdit(self.frame)
        self.emailedit.setGeometry(QtCore.QRect(430, 180, 321, 20))
        self.emailedit.setStyleSheet("")
        self.emailedit.setObjectName("emailedit")

       

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Physician Check-In"))
        self.INFO.setText(_translate("MainWindow", "Welcome to SMART XRAY WORKFLOW"))
        self.name.setText(_translate("MainWindow", "ENTER YOUR NAME"))
        self.pid.setText(_translate("MainWindow", "ENTER YOUR ID NO."))
        self.contact.setText(_translate("MainWindow", "ENTER YOUR CONTACT NO"))
        self.email.setText(_translate("MainWindow", "ENTER YOUR EMAIL"))
        
        
        self.pushButton.setText(_translate("MainWindow", "✔"))
        


if __name__ == "__main__":
    import sys
    import atexit
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()






