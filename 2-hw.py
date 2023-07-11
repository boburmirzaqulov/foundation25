import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
os.system("cls")

class flag(QMainWindow):
    country=["Afghanistan""Argentina","Belgium","Brazil","Canada","Chile","China","Czechia (Czech Republic)","Denmark","France","Germany","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Kazakhstan","Kuwait","Kyrgyzstan",'Malaysia','Mexico','Monaco','Mongolia','Panama','Paraguay','Poland','Portugal','Qatar','Russia','Saudi Arabia','Singapore','South Korea','Spain','Switzerland','Tajikistan','Turkey','Turkmenistan','Ukraine','United Arab Emirates','United Kingdom','United States of America','Uruguay','Uzbekistan']
    def __init__(self):
        super().__init__()
        self.setMaximumSize(640,480)
        self.setMinimumSize(640,480)
        self.setWindowTitle("Flag found")
        self.setStyleSheet("background-color:  rgb(220,220,220)")
        #QLabel
        self.coun=QLabel("Country:",self)
        self.coun.setGeometry(30,30,150,50)
        self.coun.setFont(QFont("Times New Roman",20))
        #QComboBox
        self.com=QComboBox(self)
        self.com.setGeometry(200,30,350,50)
        self.com.setFont(QFont("Times New Roman",20))
        self.com.setStyleSheet("color: rgb(0,0,0);background-color:  rgb(0,255,255)")
        self.com.addItems(flag.country)
        #QButton
        self.bt=QPushButton("Click",self)
        self.bt.setGeometry(300,300,100,50)
        self.bt.setFont(QFont("Times New Roman",22))
        self.bt.setStyleSheet("background-color: rgb(0,0,128);color: Lime;border-radius: 15px;")
        self.bt.clicked.connect(lambda: self.found_flag(self.com.currentText()))
        #QLabel
        self.lb=QLabel("Flag:",self)
        self.lb.setGeometry(30,150,100,50)
        self.lb.setFont(QFont("imes New Roman",20))
        self.temp=QLabel(self)
        self.temp.setGeometry(200,90,400,200)
  
    def found_flag(self,f):
        self.temp.setPixmap(QPixmap ("flags\\"+f+".png"))
        print(f)

app=QApplication(sys.argv)
f=flag()
f.show()
sys.exit(app.exec_())