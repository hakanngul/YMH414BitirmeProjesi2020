# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\ogrenciAra.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OgrenciAraWindow(object):
    def setupUi(self, OgrenciAraWindow):
        OgrenciAraWindow.setObjectName("OgrenciAraWindow")
        OgrenciAraWindow.resize(561, 486)
        self.centralwidget = QtWidgets.QWidget(OgrenciAraWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"background: #354152;\n"
"}\n"
"\n"
"QLineEdit{\n"
" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:20px;\n"
"    padding-left:15px;\n"
"    height:42px;\n"
"    border-radius:15px;\n"
"    border-color: #303030;\n"
"    background: transparent;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
"padding: 8px 16px;\n"
"color: white;\n"
"font-size: 20px;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background: #008bd1\n"
"}\n"
"QCommandLinkButton{\n"
"font-size: 16px;\n"
"background: #4c5d75;\n"
"}\n"
"QCommandLinkButton:pressed{\n"
"    background-color: rgb(92, 186, 138);\n"
"}\n"
"\n"
"\n"
"QCheckBox{\n"
"font-size:16px;;\n"
"color:white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    min-width: 6em;\n"
"    font-size:20px;\n"
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
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_duzenle = QtWidgets.QPushButton(self.frame)
        self.btn_duzenle.setGeometry(QtCore.QRect(20, 370, 501, 42))
        self.btn_duzenle.setStyleSheet("")
        self.btn_duzenle.setObjectName("btn_duzenle")
        self.text_Bolum = QtWidgets.QLineEdit(self.frame)
        self.text_Bolum.setGeometry(QtCore.QRect(270, 190, 251, 42))
        self.text_Bolum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.text_Bolum.setObjectName("text_Bolum")
        self.txt_ogrNo = QtWidgets.QLineEdit(self.frame)
        self.txt_ogrNo.setGeometry(QtCore.QRect(270, 40, 251, 42))
        self.txt_ogrNo.setObjectName("txt_ogrNo")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 40, 221, 271))
        self.label.setStyleSheet("background:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_ara = QtWidgets.QPushButton(self.frame)
        self.btn_ara.setGeometry(QtCore.QRect(270, 260, 251, 41))
        self.btn_ara.setStyleSheet("")
        self.btn_ara.setObjectName("btn_ara")
        self.txt_AdSoyad = QtWidgets.QLineEdit(self.frame)
        self.txt_AdSoyad.setEnabled(False)
        self.txt_AdSoyad.setGeometry(QtCore.QRect(270, 110, 251, 46))
        self.txt_AdSoyad.setObjectName("txt_AdSoyad")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        OgrenciAraWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OgrenciAraWindow)
        self.statusbar.setObjectName("statusbar")
        OgrenciAraWindow.setStatusBar(self.statusbar)
        self.actionDers_Ekle = QtWidgets.QAction(OgrenciAraWindow)
        self.actionDers_Ekle.setObjectName("actionDers_Ekle")
        self.action_renci_Ekle = QtWidgets.QAction(OgrenciAraWindow)
        self.action_renci_Ekle.setObjectName("action_renci_Ekle")
        self.actionDerse_renci_Ekle = QtWidgets.QAction(OgrenciAraWindow)
        self.actionDerse_renci_Ekle.setObjectName("actionDerse_renci_Ekle")

        self.retranslateUi(OgrenciAraWindow)
        QtCore.QMetaObject.connectSlotsByName(OgrenciAraWindow)

    def retranslateUi(self, OgrenciAraWindow):
        _translate = QtCore.QCoreApplication.translate
        OgrenciAraWindow.setWindowTitle(_translate("OgrenciAraWindow", "MainWindow"))
        self.btn_duzenle.setText(_translate("OgrenciAraWindow", "Öğrenciyi Düzenle"))
        self.text_Bolum.setPlaceholderText(_translate("OgrenciAraWindow", "Bölüm"))
        self.txt_ogrNo.setPlaceholderText(_translate("OgrenciAraWindow", "Öğrenci No"))
        self.label.setText(_translate("OgrenciAraWindow", "TextLabel"))
        self.btn_ara.setText(_translate("OgrenciAraWindow", "Ara"))
        self.txt_AdSoyad.setPlaceholderText(_translate("OgrenciAraWindow", "Adı ve Soyadı"))
        self.actionDers_Ekle.setText(_translate("OgrenciAraWindow", "Ders Ekle"))
        self.action_renci_Ekle.setText(_translate("OgrenciAraWindow", "Öğrenci Ekle"))
        self.actionDerse_renci_Ekle.setText(_translate("OgrenciAraWindow", "Derse Öğrenci Ekle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OgrenciAraWindow = QtWidgets.QMainWindow()
    ui = Ui_OgrenciAraWindow()
    ui.setupUi(OgrenciAraWindow)
    OgrenciAraWindow.show()
    sys.exit(app.exec_())
