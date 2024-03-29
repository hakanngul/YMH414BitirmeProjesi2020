# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(549, 668)
        LoginForm.setFixedSize(553, 668)
        self.gridLayout = QtWidgets.QGridLayout(LoginForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(LoginForm)
        self.frame.setMouseTracking(True)
        self.frame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame.setAcceptDrops(False)
        self.frame.setToolTipDuration(0)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background: #354152;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 "color:white;\n"
                                 "border-radius:15px;\n"
                                 "border: 1px solid;\n"
                                 "border-color: #303030;\n"
                                 "background: transparent;\n"
                                 "padding-left: 15px;\n"
                                 "font-size: 16px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton{\n"
                                 "border-radius: 15px;\n"
                                 "    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
                                 "padding: 8px 16px;\n"
                                 "color: white;\n"
                                 "font-size: 20px;\n"
                                 "}\n"
                                 "QPushButton#btn_login:pressed{\n"
                                 "color: black;\n"
                                 "background: #008bd1\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QCommandLinkButton{\n"
                                 "font-size: 16px;\n"
                                 "background: #4c5d75;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QCommandLinkButton:pressed{\n"
                                 "\n"
                                 "    background-color: rgb(92, 186, 138);\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QGroupBox{\n"
                                 "border:none;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(70, 60, 400, 531))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 160, 411, 81))
        self.label_2.setStyleSheet("color: #7E8BA3;\n"
                                   "font: 44px \"Helvetica Neue\", sans-serif;\n"
                                   "margin: 0px 0px 16px;")
        self.label_2.setObjectName("label_2")
        self.text_Sifre = QtWidgets.QLineEdit(self.groupBox)
        self.text_Sifre.setGeometry(QtCore.QRect(40, 330, 336, 42))
        self.text_Sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_Sifre.setObjectName("text_Sifre")
        self.btn_login = QtWidgets.QPushButton(self.groupBox)
        self.btn_login.setGeometry(QtCore.QRect(40, 410, 336, 42))
        self.btn_login.setStyleSheet("")
        self.btn_login.setObjectName("btn_login")
        self.text_kullaniciAdi = QtWidgets.QLineEdit(self.groupBox)
        self.text_kullaniciAdi.setGeometry(QtCore.QRect(40, 260, 336, 42))
        self.text_kullaniciAdi.setObjectName("text_kullaniciAdi")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(140, 30, 121, 121))
        self.label.setStyleSheet("image: url(:/resimler/icons/damla.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.btn_kayit = QtWidgets.QCommandLinkButton(self.groupBox)
        self.btn_kayit.setGeometry(QtCore.QRect(270, 490, 121, 41))
        self.btn_kayit.setStyleSheet("")
        self.btn_kayit.setObjectName("btn_kayit")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)
        LoginForm.setTabOrder(self.text_kullaniciAdi, self.text_Sifre)
        LoginForm.setTabOrder(self.text_Sifre, self.btn_login)
        LoginForm.setTabOrder(self.btn_login, self.btn_kayit)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Form"))
        self.label_2.setText(_translate("LoginForm", "GİRİŞ SAYFASI"))
        self.text_Sifre.setPlaceholderText(_translate("LoginForm", "Şifre"))
        self.btn_login.setText(_translate("LoginForm", "GİRİŞ YAP"))
        self.text_kullaniciAdi.setPlaceholderText(_translate("LoginForm", "Kullanıcı Adı"))
        self.btn_kayit.setText(_translate("LoginForm", "KAYIT OL"))


from ui_pages import resoruces_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    ui.setupUi(LoginForm)
    LoginForm.show()
    sys.exit(app.exec_())
