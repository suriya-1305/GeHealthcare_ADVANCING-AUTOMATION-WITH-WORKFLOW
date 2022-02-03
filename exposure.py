from PyQt5.QtWidgets import *
import sys
class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Exposure Chart")
        self.setGeometry(100, 100, 300, 400)
        self.formGroupBox = QGroupBox("kVp and mAs estimation")
        self.cm = QSpinBox()
        self.type = QLineEdit()
        self.Bodypart = QLineEdit()
        self.createForm()
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.getInfo)
        self.buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)
    def getInfo(self):
        print("Enter Body part to be examine : {0}".format(self.Bodypart.text()))
        print("Type of body(based on CM) : {0}".format(self.type.text()))
        print("CM : {0}".format(self.cm.text()))
        if self.Bodypart.text()=="ChestPA" and self.type.text()=="Small" and self.cm.text()=="14" or self.cm.text()=="15" :
            self.kvp=85
            self.mAs=4
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)            
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Small" and self.cm.text()=="16" or self.cm.text()=="17" :
            self.kvp=85
            self.mAs=6
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Small" and self.cm.text()=="18" or self.cm.text()=="19" :
            self.kvp=85
            self.mAs=8
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Medium" and self.cm.text()=="20" or self.cm.text()=="21" :
            self.kvp=100
            self.mAs=2
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Medium" and self.cm.text()=="22" or self.cm.text()=="23" :
            self.kvp=100
            self.mAs=3
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Medium" and self.cm.text()=="24" or self.cm.text()=="25" :
            self.kvp=85
            self.mAs=4
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Large" and self.cm.text()=="26" or self.cm.text()=="27" :
            self.kvp=110
            self.mAs=6
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Large" and self.cm.text()=="28" or self.cm.text()=="29" :
            self.kvp=110
            self.mAs=9
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Large" and self.cm.text()=="30" or self.cm.text()=="31" :
            self.kvp=110
            self.mAs=12
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Large" and self.cm.text()=="32" or self.cm.text()=="33" :
            self.kvp=110
            self.mAs=18
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="ChestPA" and self.type.text()=="Large" and self.cm.text()=="34" or self.cm.text()=="35" :
            self.kvp=110
            self.mAs=24
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)  

        elif self.Bodypart.text()=="HipAP" and self.type.text()=="Small" and self.cm.text()=="13" or self.cm.text()=="14" :
            self.kvp=72
            self.mAs=15
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="HipAP" and self.type.text()=="Small" and self.cm.text()=="15" or self.cm.text()=="16" :
            self.kvp=72
            self.mAs=22.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="HipAP" and self.type.text()=="Small" and self.cm.text()=="17" or self.cm.text()=="18" :
            self.kvp=72
            self.mAs=30
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="HipAP" and self.type.text()=="Medium" and self.cm.text()=="19" or self.cm.text()=="20" :
            self.kvp=78
            self.mAs=30
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="HipAP" and self.type.text()=="Medium" and self.cm.text()=="21" or self.cm.text()=="22" :
            self.kvp=78
            self.mAs=45
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="HipAP" and self.type.text()=="Medium" and self.cm.text()=="23" or self.cm.text()=="24" :
            self.kvp=78
            self.mAs=60
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="HipAP" and self.type.text()=="Large" and self.cm.text()=="25" or self.cm.text()=="26" :
            self.kvp=84
            self.mAs=60
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="HipAP" and self.type.text()=="Large" and self.cm.text()=="27" or self.cm.text()=="28" :
            self.kvp=84
            self.mAs=90
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="HipAP" and self.type.text()=="Large" and self.cm.text()=="29" or self.cm.text()=="30" :
            self.kvp=84
            self.mAs=120
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    

        elif self.Bodypart.text()=="KneeAP" and self.type.text()=="Small" and self.cm.text()=="7" or self.cm.text()=="8" :
            self.kvp=66
            self.mAs=11.3
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="KneeAP" and self.type.text()=="Small" and self.cm.text()=="9" or self.cm.text()=="10" :
            self.kvp=66
            self.mAs=15
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="KneeAP" and self.type.text()=="Medium" and self.cm.text()=="11" or self.cm.text()=="12" :
            self.kvp=66
            self.mAs=15
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="KneeAP" and self.type.text()=="Medium" and self.cm.text()=="13" or self.cm.text()=="14" :
            self.kvp=70
            self.mAs=22.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="KneeAP" and self.type.text()=="Large" and self.cm.text()=="15" or self.cm.text()=="16" :
            self.kvp=70
            self.mAs=30
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="KneeAP" and self.type.text()=="Large" and self.cm.text()=="17" or self.cm.text()=="18" :
            self.kvp=0
            self.mAs=45
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 


        elif self.Bodypart.text()=="LegAP" and self.type.text()=="Small" and self.cm.text()=="5" or self.cm.text()=="6" :
            self.kvp=66
            self.mAs=3
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="LegAP" and self.type.text()=="Small" and self.cm.text()=="7" or self.cm.text()=="8" :
            self.kvp=66
            self.mAs=4
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="LegAP" and self.type.text()=="Medium" and self.cm.text()=="9" or self.cm.text()=="10" :
            self.kvp=70
            self.mAs=4
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)  

        elif self.Bodypart.text()=="LegAP" and self.type.text()=="Medium" and self.cm.text()=="11" or self.cm.text()=="12" :
            self.kvp=70
            self.mAs=6
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="LegAP" and self.type.text()=="Large" and self.cm.text()=="13" or self.cm.text()=="14" :
            self.kvp=74
            self.mAs=6
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="LegAP" and self.type.text()=="Large" and self.cm.text()=="15" or self.cm.text()=="16" :
            self.kvp=74
            self.mAs=9
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 


        elif self.Bodypart.text()=="AnkleAP" and self.type.text()=="Small" and self.cm.text()=="5" or self.cm.text()=="6" :
            self.kvp=56
            self.mAs=1
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="AnkleAP" and self.type.text()=="Medium" and self.cm.text()=="7" or self.cm.text()=="8" :
            self.kvp=60
            self.mAs=1
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="AnkleAP" and self.type.text()=="Medium" and self.cm.text()=="9" or self.cm.text()=="10" :
            self.kvp=60
            self.mAs=1.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="AnkleAP" and self.type.text()=="Large" and self.cm.text()=="11" or self.cm.text()=="12" :
            self.kvp=64
            self.mAs=1.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="AnkleAP" and self.type.text()=="Large" and self.cm.text()=="13" or self.cm.text()=="14" :
            self.kvp=64
            self.mAs=2.3
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 


        elif self.Bodypart.text()=="FootAP" and self.type.text()=="Small" and self.cm.text()=="4" or self.cm.text()=="5" :
            self.kvp=56
            self.mAs=1
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="FootAP" and self.type.text()=="Medium" and self.cm.text()=="6" or self.cm.text()=="7" :
            self.kvp=60
            self.mAs=1
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="FootAP" and self.type.text()=="Medium" and self.cm.text()=="8" or self.cm.text()=="9" :
            self.kvp=60
            self.mAs=1.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)  

        elif self.Bodypart.text()=="FootAP" and self.type.text()=="Large" and self.cm.text()=="10" or self.cm.text()=="11" :
            self.kvp=64
            self.mAs=1.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="FootAP" and self.type.text()=="Large" and self.cm.text()=="12" or self.cm.text()=="13" :
            self.kvp=64
            self.mAs=2
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)  


        elif self.Bodypart.text()=="ForearmAP" and self.type.text()=="Small" and self.cm.text()=="2" or self.cm.text()=="3" :
            self.kvp=62
            self.mAs=1.125
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 


        elif self.Bodypart.text()=="ForearmAP" and self.type.text()=="Small" and self.cm.text()=="4" or self.cm.text()=="5" :
            self.kvp=62
            self.mAs=1.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="ForearmAP" and self.type.text()=="Medium" and self.cm.text()=="6" or self.cm.text()=="7" :
            self.kvp=66
            self.mAs=1.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="ForearmAP" and self.type.text()=="Medium" and self.cm.text()=="8" or self.cm.text()=="9" :
            self.kvp=66
            self.mAs=2.25
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="ForearmAP" and self.type.text()=="Large" and self.cm.text()=="10" or self.cm.text()=="11" :
            self.kvp=66
            self.mAs=3
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="ForearmAP" and self.type.text()=="Large" and self.cm.text()=="12" or self.cm.text()=="13" :
            self.kvp=66
            self.mAs=4.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
  

        elif self.Bodypart.text()=="ForearmAP" and self.type.text()=="Small" and self.cm.text()=="2" or self.cm.text()=="3" :
            self.kvp=62
            self.mAs=1.125
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 


        elif self.Bodypart.text()=="HandAP" and self.type.text()=="Small" and self.cm.text()=="1" or self.cm.text()=="2" :
            self.kvp=53
            self.mAs=1
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="HandAP" and self.type.text()=="Medium" and self.cm.text()=="3" or self.cm.text()=="4" :
            self.kvp=57
            self.mAs=1
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 
        elif self.Bodypart.text()=="HandAP" and self.type.text()=="Medium" and self.cm.text()=="5" or self.cm.text()=="6" :
            self.kvp=57
            self.mAs=1.5
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="HandAP" and self.type.text()=="Large" and self.cm.text()=="7" or self.cm.text()=="8" :
            self.kvp=57
            self.mAs=2
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok)    
        elif self.Bodypart.text()=="HandAP" and self.type.text()=="Large" and self.cm.text()=="9" or self.cm.text()=="10" :
            self.kvp=57
            self.mAs=3
            print(self.kvp,self.mAs)
            QMessageBox.question(self, 'Exposure Confirmation', "KVP: " + str(self.kvp) + "\nMAS: " + str(self.mAs), QMessageBox.Ok, QMessageBox.Ok) 

        self.close()
    def createForm(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Enter Body part to be examine"), self.Bodypart)
        layout.addRow(QLabel("Type of body(based on CM)"), self.type)
        layout.addRow(QLabel("CM"), self.cm)
        self.formGroupBox.setLayout(layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec())
