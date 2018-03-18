# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HW5_Sql_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from BabyNames_db import execQuery1 
from BabyNames_db import execQuery2 
#from outputWindow import Ui_outputWindow
class Ui_Dialog(object):
#==============================================================================
#     def openwindow(self):
#         self.window=QtWidgets.QMainWindow()
#         self.Ui =Ui_outputWindow()
#         self.Ui.setupUi(self.outputWindow)
#         self.window.show()
#==============================================================================
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(925, 492)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        self.label_byYear = QtWidgets.QLabel(Dialog)
        self.label_byYear.setGeometry(QtCore.QRect(50, 50, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_byYear.setFont(font)
        self.label_byYear.setObjectName("label_byYear")
        self.label_byName = QtWidgets.QLabel(Dialog)
        self.label_byName.setGeometry(QtCore.QRect(560, 60, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_byName.setFont(font)
        self.label_byName.setObjectName("label_byName")
        self.label_title1 = QtWidgets.QLabel(Dialog)
        self.label_title1.setGeometry(QtCore.QRect(10, 100, 441, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_title1.setFont(font)
        self.label_title1.setObjectName("label_title1")
        self.label_title2 = QtWidgets.QLabel(Dialog)
        self.label_title2.setGeometry(QtCore.QRect(560, 110, 391, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_title2.setFont(font)
        self.label_title2.setObjectName("label_title2")
        self.label_BirthYear = QtWidgets.QLabel(Dialog)
        self.label_BirthYear.setGeometry(QtCore.QRect(20, 170, 61, 16))
        self.label_BirthYear.setObjectName("label_BirthYear")
        self.label_popularity = QtWidgets.QLabel(Dialog)
        self.label_popularity.setGeometry(QtCore.QRect(20, 240, 47, 13))
        self.label_popularity.setObjectName("label_popularity")
        self.lineEdit_BirthYear = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_BirthYear.setGeometry(QtCore.QRect(120, 170, 113, 31))
        self.lineEdit_BirthYear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_BirthYear.setObjectName("lineEdit_BirthYear")
        
        
        self.label_Name = QtWidgets.QLabel(Dialog)
        self.label_Name.setGeometry(QtCore.QRect(570, 160, 47, 13))
        self.label_Name.setObjectName("label_Name")
        self.label_Years = QtWidgets.QLabel(Dialog)
        self.label_Years.setGeometry(QtCore.QRect(570, 230, 47, 13))
        self.label_Years.setObjectName("label_Years")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(650, 150, 161, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        
      
        
        self.comboBox_Years = QtWidgets.QComboBox(Dialog)
        self.comboBox_Years.setGeometry(QtCore.QRect(650, 220, 161, 31))
        self.comboBox_Years.setObjectName("comboBox_Years")
        
        
        self.comboBox_Years.addItem("")
        
        #########################################################
                  
              
        #self.comboBox_Years.addItem("2000 & later")
        self.comboBox_Years.addItem("1980 & later")
        self.comboBox_Years.addItem("1960 & later")
        self.comboBox_Years.addItem("1940 & later")
        self.comboBox_Years.addItem("1920 & later")
        self.comboBox_Years.addItem("1900 & later")
        
        #########################################################
        self.label_Gender_Name = QtWidgets.QLabel(Dialog)
        self.label_Gender_Name.setGeometry(QtCore.QRect(560, 290, 191, 21))
        self.label_Gender_Name.setObjectName("label_Gender_Name")
        self.radioButton_Male = QtWidgets.QRadioButton(Dialog)
        self.radioButton_Male.setGeometry(QtCore.QRect(570, 330, 141, 20))
        self.radioButton_Male.setObjectName("radioButton_Male")
        self.radioButton_Female = QtWidgets.QRadioButton(Dialog)
        self.radioButton_Female.setGeometry(QtCore.QRect(570, 370, 151, 20))
        self.radioButton_Female.setObjectName("radioButton_Female")
        self.pushButton_Go1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Go1.setGeometry(QtCore.QRect(40, 340, 75, 23))
        self.pushButton_Go1.setObjectName("pushButton_Go1")
        
         
        #################################################################
        print(self.lineEdit_BirthYear.text())
        self.pushButton_Go1.clicked.connect(lambda:execQuery1(self.lineEdit_BirthYear.text()))
        
        #################################################################
        
        
       # count = [lambda:0, lambda:N+1][count==N]()   # if(self.radioButton_Male.isChecked())]else 'F'
        
        self.pushButton_Reset1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Reset1.setGeometry(QtCore.QRect(190, 340, 75, 23))
        self.pushButton_Reset1.setObjectName("pushButton_Reset1")
        
        #################################################################
        #self.pushButton_Reset1.clicked.connect(self.openwindow)
        
        #################################################################
        
        #'Yes' if fruit == 'Apple' else 'No'        
        
        self.pushButton_Go2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Go2.setGeometry(QtCore.QRect(600, 440, 75, 23))
        self.pushButton_Go2.setObjectName("pushButton_Go2")
        
        #################################################################
        #if(self.radioButton_Male.isChecked()):
        #self.pushButton_Go2.clicked.connect(lambda:execQuery2(self.lineEdit_2.text(),self.comboBox_Years.currentIndex(), gender_value =['M','F'][self.radioButton_Male.isChecked()]))
        #else:
           # self.pushButton_Go2.clicked.connect(lambda:execQuery2(self.lineEdit_2.text(),self.comboBox_Years.currentIndex(),'F'))
        #count = 0 if count == N else N + 1
        self.pushButton_Go2.clicked.connect(lambda:execQuery2(self.lineEdit_2.text(),self.comboBox_Years.currentIndex(), gender_value = 'M' if(self.radioButton_Male.isChecked()) else 'F'))
        #self.pushButton_Go2.connect(self.create_new_library_window)
       
        #################################################################
        
        self.pushButton_Reset2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Reset2.setGeometry(QtCore.QRect(750, 440, 75, 23))
        self.pushButton_Reset2.setObjectName("pushButton_Reset2")
        
        
            
        #################################################################
       # self.pushButton_Reset2.clicked.connect(lambda:self.lineEdit_2.clear(), lambda:self.comboBox_Years.clear(),lambda:self.radioButton_Female.clear())
        #################################################################
        
        
        
        
        
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(340, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(423, 50, 20, 401))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "BabyNames"))
        self.label_byYear.setText(_translate("Dialog", "Popular Names by Birth Year"))
        self.label_byName.setText(_translate("Dialog", "Popularity of a Name"))
        self.label_title1.setText(_translate("Dialog", "Enter the Year and Popularity for a List of the Most Popular Names (year after 1879)"))
        self.label_title2.setText(_translate("Dialog", "See How the Popularity of a Name has Changed Over Time!"))
        self.label_BirthYear.setText(_translate("Dialog", "Birth Year"))
        self.label_popularity.setText(_translate("Dialog", "Popularity"))
        self.lineEdit_BirthYear.setText(_translate("Dialog", "2016"))
        self.label_Name.setText(_translate("Dialog", "Name"))
        self.label_Years.setText(_translate("Dialog", "Years"))
        self.comboBox_Years.setItemText(0, _translate("Dialog", "2000 & later"))
        self.label_Gender_Name.setText(_translate("Dialog", "Gender associated with the name"))
        self.radioButton_Male.setText(_translate("Dialog", "              Male"))
        self.radioButton_Female.setText(_translate("Dialog", "              Female"))
        self.pushButton_Go1.setText(_translate("Dialog", "Go"))
        self.pushButton_Reset1.setText(_translate("Dialog", "Reset"))
        self.pushButton_Go2.setText(_translate("Dialog", "Go"))
        self.pushButton_Reset2.setText(_translate("Dialog", "Reset"))
        self.label_title.setText(_translate("Dialog", "          Items of Interests"))
#######################################################################
    #def create_new_library_window(self):
      #  self.new_lib = newlib.NewLibrary()
       # self.new_lib.show()
################################################################################    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

