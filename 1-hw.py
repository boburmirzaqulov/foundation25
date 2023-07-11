import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
os.system("cls")

class project(QMainWindow):
    res=""
    country=["Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Côte d'Ivoire","Cabo Verde","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo (Congo-Brazzaville)","Costa Rica","Croatia","Cuba","Cyprus","Czechia (Czech Republic)","Democratic Republic of the Congo","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini (fmr. Swaziland)","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Jordan","Kazakhstan","Kenya","Kiribati","Kuwait","Kyrgyzstan",'Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Lithuania','Luxembourg','Madagascar','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar (formerly Burma)','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','North Korea','North Macedonia','Norway','Oman','Pakistan','Palau','Palestine State','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Korea','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Tajikistan','Tanzania','Thailand','Timor-Leste','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States of America','Uruguay','Uzbekistan','Vanuatu','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']
    def __init__(self):
        super().__init__()
        self.setMaximumSize(550,670)
        self.setMinimumSize(550,670)
        self.setWindowTitle("Registration")
        self.setStyleSheet("background-color: rgb(112,128,144)")

        #QLabelname
        self.name=self.init_label("Isim:")
        self.name.setGeometry(30,20,130,40)

        #QLineEditname
        self.name_edit=self.init_line_edit()
        self.name_edit.setGeometry(160,20,250,40)
        
        
        #QLabelsurname
        self.surname=self.init_label("Familiya:")
        self.surname.setGeometry(30,70,130,40)

        #QlineEdirsurname
        self.surname_edit=self.init_line_edit()
        self.surname_edit.setGeometry(160,70,250,40)

        #Qlabel sex
        self.sex=self.init_label("Jinsi: ")
        self.sex.setGeometry(30,120,70,40)
        #QRadioButton sex
        self.sex1=QRadioButton(self)
        self.sex1.setFont(QFont("Times New Roman",18))
        self.sex1.setGeometry(110,120,100,40)
        self.sex1.setStyleSheet("""background-color: rgb(255,235,205);color: rgb(0,0,128);border-radius: 10px;
                                border-color: Lime;border-style: solid;border-width: 3px""")
        self.sex1.setText("Ayol")
        self.sex2=QRadioButton(self)
        self.sex2.setFont(QFont("Times New Roman",18))
        self.sex2.setGeometry(220,120,100,40)
        self.sex2.setStyleSheet("""background-color: rgb(255,235,205);color: rgb(0,0,128);border-radius: 10px;
                                border-color: Lime;border-style: solid;border-width: 3px""")
        self.sex2.setText("Erkak")

        #Qlabelogin
        self.login=self.init_label("Login:")
        self.login.setGeometry(30,180,100,40)
        #QLineEditlogin
        self.login_edit=self.init_line_edit()
        self.login_edit.setGeometry(160,170,250,40)    
        #Qlabeparol
        self.parol=self.init_label("Parol:")
        self.parol.setGeometry(30,230,100,40)
       
        #QLineEditparol
        self.parol_edit=self.init_line_edit()
        self.parol_edit.setGeometry(160,230,250,40)
        #Qlabeparol
        self.parol1=self.init_label("Parol_:")
        self.parol1.setGeometry(30,280,100,40)
        #QLineEditparol
        self.parol1_edit=self.init_line_edit()
        self.parol1_edit.setGeometry(160,280,250,40)
        #QLeblecombo
        self.labelcom=self.init_label("Country:")
        self.labelcom.setGeometry(30,330,200,40)
        #QComboBox
        self.com=QComboBox(self)
        self.com.setGeometry(170,330,250,40)
        self.com.setFont(QFont("Times New Roman",18))
        self.com.setStyleSheet("color: rgb(0,0,128);background-color: white;")
        self.com.addItems(project.country)
        self.result=QLabel(self)
        self.result.setGeometry(130,560,250,50)
        self.result.setFont(QFont("Times New Roman",20))
        self.result.setStyleSheet("color: red")
        #QChexBox
        self.chxb=QCheckBox("\t\t\tMa'limotlarni faylga\n\t\t\tyozishga roziman",self)
        self.chxb.setGeometry(30,380,250,80)
        self.chxb.setFont(QFont("Times New Roman",14))
        self.chxb.setStyleSheet("color: Lime")

        #QButton
        self.bt=QPushButton("Registr",self)
        self.bt.setGeometry(150,500,150,50)
        self.bt.setFont(QFont("Times New Roman",22))
        self.bt.setStyleSheet("background-color: Black;color: Lime;border-radius: 10px;border-color: Lime;border-width: 3px;")
        self.bt.clicked.connect(self.registret)
    def init_label(self,n):
        temp=QLabel(n,self)
        temp.setFont(QFont("Times New Roman",20))
        temp.setStyleSheet("color: rgb(0,250,0)")
        return temp
    
    def init_line_edit(self):
        temp=QLineEdit(self)
        temp.setFont(QFont("Times New Roman",18))
        temp.setStyleSheet("""background-color: rgb(255,255,255);color: rgb(0,0,128);
        border-color: rgb(0,255,0);border-radius: 10px;border-style: solid;border-width: 3px;""")
        return temp
    
    def registret(self):
        if self.chxb.isChecked():
            f=open("Regisratsiya.txt","a+")
            project.res+=self.name.text()+self.name_edit.text()+"\n"
            project.res+=self.surname.text()+self.surname_edit.text()+"\n"
            if self.sex1.isChecked():
                project.res+=self.sex.text()+self.sex1.text()+"\n"
            else:
                project.res+=self.sex.text()+self.sex2.text()+"\n" 
            project.res+=self.login.text()+self.login_edit.text()+"\n"
            project.res+=self.parol.text()+self.parol_edit.text()+"\n"
            project.res+=self.parol1.text()+self.parol1_edit.text()+"\n"
            project.res+=self.labelcom.text()+self.com.currentText()+"\n"
            print(project.res)
            self.result.setText("Faylga yozildi")
            f.writelines(project.res)
        else:
            self.result.setText("Faylga yozilmadi")

app=QApplication(sys.argv)
registration=project()
registration.show()
sys.exit(app.exec_())