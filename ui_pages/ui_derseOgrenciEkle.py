# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\derseOgrenciEkle.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DerseOgrenciEkleForm(object):
    def setupUi(self, DerseOgrenciEkleForm):
        DerseOgrenciEkleForm.setObjectName("DerseOgrenciEkleForm")
        DerseOgrenciEkleForm.resize(575, 536)
        DerseOgrenciEkleForm.setFixedSize(575, 536)
        self.gridLayout = QtWidgets.QGridLayout(DerseOgrenciEkleForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(DerseOgrenciEkleForm)
        self.frame.setStyleSheet("QFrame{\n"
                                 "\n"
                                 "background: #354152;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 "    border: 2px solid gray;\n"
                                 "    border-color:white;\n"
                                 "    border-radius: 10px;\n"
                                 "    min-width: 6em;\n"
                                 "    font-size:20px;\n"
                                 "    padding-left:15px;\n"
                                 "    height:42px;\n"
                                 "    border-radius:15px;\n"
                                 "    border-color: #303030;\n"
                                 "    background: transparent;\n"
                                 "    color:#ffffffff;\n"
                                 "\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "QComboBox {\n"
                                 "    border: 2px solid gray;\n"
                                 "    border-radius: 10px;\n"
                                 "    min-width: 6em;\n"
                                 "    font-size:20px;\n"
                                 "    border-color: rgb(255, 255, 255);\n"
                                 "    padding-left:15px;\n"
                                 "    height:42px;\n"
                                 "    border-radius:15px;\n"
                                 "    border-color: #303030;\n"
                                 "    background: transparent;\n"
                                 "    color:white;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:on {\n"
                                 "    border-bottom-left-radius: 0px;\n"
                                 "    border-bottom-right-radius: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView {\n"
                                 "    border-bottom-right-radius: 10px;\n"
                                 "    border-bottom-left-radius: 10px;\n"
                                 "    background: #354152;\n"
                                 "    border: 1px solid gray;\n"
                                 "    color:white;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down {\n"
                                 "    border-color: white;\n"
                                 "}\n"
                                 "QPushButton{\n"
                                 "border-radius: 15px;\n"
                                 "background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
                                 "padding: 8px 16px;\n"
                                 "color: white;\n"
                                 "font-size: 20px;\n"
                                 "height:42px;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "color: black;\n"
                                 "background: #008bd1\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.txt_OgrNo = QtWidgets.QLineEdit(self.frame)
        self.txt_OgrNo.setGeometry(QtCore.QRect(300, 30, 261, 46))
        self.txt_OgrNo.setObjectName("txt_OgrNo")
        self.txt_AdSoyad = QtWidgets.QLineEdit(self.frame)
        self.txt_AdSoyad.setEnabled(False)
        self.txt_AdSoyad.setGeometry(QtCore.QRect(300, 110, 261, 46))
        self.txt_AdSoyad.setObjectName("txt_AdSoyad")
        self.txt_Bolum = QtWidgets.QLineEdit(self.frame)
        self.txt_Bolum.setEnabled(False)
        self.txt_Bolum.setGeometry(QtCore.QRect(300, 190, 261, 46))
        self.txt_Bolum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txt_Bolum.setObjectName("txt_Bolum")
        self.btn_ara = QtWidgets.QPushButton(self.frame)
        self.btn_ara.setGeometry(QtCore.QRect(310, 260, 241, 41))
        self.btn_ara.setStyleSheet("")
        self.btn_ara.setObjectName("btn_ara")
        self.cmb_Dersler = QtWidgets.QComboBox(self.frame)
        self.cmb_Dersler.setGeometry(QtCore.QRect(12, 350, 541, 46))
        self.cmb_Dersler.setObjectName("cmb_Dersler")
        self.cmb_Dersler.addItem("")
        self.btn_Ekle = QtWidgets.QPushButton(self.frame)
        self.btn_Ekle.setGeometry(QtCore.QRect(12, 437, 541, 41))
        self.btn_Ekle.setStyleSheet("")
        self.btn_Ekle.setObjectName("btn_Ekle")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 272, 292))
        self.label.setStyleSheet("background:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(DerseOgrenciEkleForm)
        QtCore.QMetaObject.connectSlotsByName(DerseOgrenciEkleForm)

    def retranslateUi(self, DerseOgrenciEkleForm):
        _translate = QtCore.QCoreApplication.translate
        DerseOgrenciEkleForm.setWindowTitle(_translate("DerseOgrenciEkleForm", "Form"))
        self.txt_OgrNo.setPlaceholderText(_translate("DerseOgrenciEkleForm", "Öğrenci No"))
        self.txt_AdSoyad.setPlaceholderText(_translate("DerseOgrenciEkleForm", "Adı ve Soyadı"))
        self.txt_Bolum.setPlaceholderText(_translate("DerseOgrenciEkleForm", "Bölüm"))
        self.btn_ara.setText(_translate("DerseOgrenciEkleForm", "Ara"))
        self.cmb_Dersler.setItemText(0, _translate("DerseOgrenciEkleForm", "Öğretmene Ait Ders Kaydı Bulunamadı"))
        self.btn_Ekle.setText(_translate("DerseOgrenciEkleForm", "Öğrenciyi Derse Ekle"))
        self.label.setText(_translate("DerseOgrenciEkleForm", "TextLabel"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    DerseOgrenciEkleForm = QtWidgets.QWidget()
    ui = Ui_DerseOgrenciEkleForm()
    ui.setupUi(DerseOgrenciEkleForm)
    DerseOgrenciEkleForm.show()
    sys.exit(app.exec_())
