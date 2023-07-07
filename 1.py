import os
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

os.system("cls")


class calculate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(290, 500)
        self.setMaximumSize(290, 500)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon(os.getcwd() + "\\resource\\Iphone.ico"))
        self.setStyleSheet("background-color: rgb(28,28,28)")
        # Button C
        bcc = QPushButton("C", self)
        bcc.setGeometry(10, 150, 60, 60)
        bcc.setFont(QFont("Microsoft Sans Serif", 18))
        bcc.setStyleSheet("background-color: rgb(212,212,210);color: rgb(28,28,28);border-radius:30px")
        bcc.clicked.connect(self.calcul)
        # +/-
        bci = QPushButton("+/-", self)
        bci.setGeometry(80, 150, 60, 60)
        bci.setStyleSheet("background-color: rgb(212,212,210);color: rgb(28,28,28);border-radius:30px")
        bci.setFont(QFont("Microsoft Sans Serif", 18))
        bci.clicked.connect(self.calcul)
        # %
        bcf = QPushButton("%", self)
        bcf.setGeometry(150, 150, 60, 60)
        bcf.setFont(QFont("Microsoft Sans Serif", 18))
        bcf.setStyleSheet("background-color: rgb(212,212,210);color:rgb(28,28,28);border-radius:30px")
        bcf.clicked.connect(self.calcul)
        # ÷
        bcb = QPushButton("÷", self)
        bcb.setGeometry(220, 150, 60, 60)
        bcb.setFont(QFont("Microsoft Sans Serif", 25))
        bcb.setStyleSheet("background-color: rgb(255,149,0);color: rgb(212,212,210);border-radius:30px")
        bcb.clicked.connect(self.calcul)
        # Button 7
        bc7 = self.initBtnNum("7")
        bc7.setGeometry(10, 220, 60, 60)
        # Button 8
        bc8 = self.initBtnNum("8")
        bc8.setGeometry(80, 220, 60, 60)
        # Button 9
        bc9 = self.initBtnNum("9")
        bc9.setGeometry(150, 220, 60, 60)
        # Button ×
        bck = QPushButton("×", self)
        bck.setGeometry(220, 220, 60, 60)
        bck.setStyleSheet("background-color: rgb(255,146,0);color: rgb(212,212,210);border-radius: 30px")
        bck.setFont(QFont("Microsoft Sans Serif", 25))
        bck.clicked.connect(self.calcul)
        # Button 4
        bc4 = self.initBtnNum("4")
        bc4.setGeometry(10, 290, 60, 60)
        # Button 5
        bc5 = self.initBtnNum("5")
        bc5.setGeometry(80, 290, 60, 60)

        # Button 6
        bc6 = self.initBtnNum("6")
        bc6.setGeometry(150, 290, 60, 60)
        # Button -
        bca = QPushButton("-", self)
        bca.setGeometry(220, 290, 60, 60)
        bca.setFont(QFont("Microsoft Sans Serif", 25))
        bca.setStyleSheet("background-color: rgb(255,146,0);color: rgb(212,212,210);border-radius: 30px")
        bca.clicked.connect(self.calcul)
        # Button 1
        bc1 = self.initBtnNum("1")
        bc1.setGeometry(10, 360, 60, 60)
        # Button 2
        bc2 = self.initBtnNum("2")
        bc2.setGeometry(80, 360, 60, 60)
        # Button 3
        bc3 = self.initBtnNum("3");
        bc3.setGeometry(150, 360, 60, 60)
        # Button +
        bcq = QPushButton("+", self)
        bcq.setGeometry(220, 360, 60, 60)
        bcq.setFont(QFont("Microsoft Sans Serif", 18))
        bcq.setStyleSheet("background-color: rgb(255,146,0);color: rgb(212,212,210);border-radius: 30px")
        bcq.clicked.connect(self.calcul)
        # Button 0
        bc0 = QPushButton("0", self)
        bc0.setGeometry(10, 430, 130, 60)
        bc0.setFont(QFont("Arial", 18))
        bc0.setStyleSheet("background-color: rgb(85,85,85);color: rgb(212,212,210);border-radius: 28px")
        bc0.clicked.connect(self.calcul)
        # Button .
        bcv = QPushButton(".", self)
        bcv.setGeometry(150, 430, 60, 60)
        bcv.setFont(QFont("Arial", 18))
        bcv.setStyleSheet("background-color: rgb(85,85,85);color: rgb(212,212,210);border-radius: 30px")
        bcv.clicked.connect(self.calcul)
        # Button =
        bct = QPushButton("=", self)
        bct.setGeometry(220, 430, 60, 60)
        bct.setFont(QFont("Microsoft Sans Senif", 18))
        bct.setStyleSheet("background-color: rgb(255,146,0);color: rgb(212,212,210);border-radius: 30px")
        bct.clicked.connect(self.calcul)

    def calcul(self):
        print("Salom")

    def initBtnNum(self, n):
        bc = QPushButton(n, self)
        bc.setFont(QFont("Arial", 18))
        bc.setStyleSheet("background-color: rgb(85,85,85);color: rgb(212,212,210);border-radius: 30px")
        bc.clicked.connect(self.calcul)
        return bc


app = QApplication(sys.argv)
cal = calculate()
cal.show()
sys.exit(app.exec_())
