# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\email.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EMailForm(object):
    def setupUi(self, EMailForm):
        EMailForm.setObjectName("EMailForm")
        EMailForm.resize(455, 526)
        self.gridLayout = QtWidgets.QGridLayout(EMailForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(EMailForm)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background: #354152;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 "    height:42px;\n"
                                 "     border: 1px solid gray;\n"
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
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 160, 394, 321))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.formLayout.setContentsMargins(0, 10, 0, 0)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font-size:24px;\n"
                                   "color:white;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_oldMail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_oldMail.setEnabled(False)
        self.txt_oldMail.setPlaceholderText("")
        self.txt_oldMail.setObjectName("txt_oldMail")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_oldMail)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font-size:24px;\n"
                                   "color:white;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_NewMail = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_NewMail.setEnabled(True)
        self.txt_NewMail.setPlaceholderText("")
        self.txt_NewMail.setObjectName("txt_NewMail")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_NewMail)
        self.btn_login = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_login.setStyleSheet("\n"
                                     "QPushButton{\n"
                                     "border-radius: 15px;\n"
                                     "    background-color: qlineargradient(spread:reflect, x1:1, y1:0.466409, x2:0.188, y2:0.482727, stop:0.823864 rgba(82, 185, 143, 255), stop:1 rgba(115, 185, 153, 255));\n"
                                     "padding: 8px 16px;\n"
                                     "color: white;\n"
                                     "font-size: 20px;\n"
                                     "height:42px;\n"
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
                                     "}")
        self.btn_login.setObjectName("btn_login")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btn_login)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 10, 120, 150))
        self.label.setStyleSheet("image: url(:/resimler/icons/damla.png);\n"
                                 "height:150px;\n"
                                 "width:120px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(EMailForm)
        QtCore.QMetaObject.connectSlotsByName(EMailForm)

    def retranslateUi(self, EMailForm):
        _translate = QtCore.QCoreApplication.translate
        EMailForm.setWindowTitle(_translate("EMailForm", "Form"))
        self.label_2.setText(_translate("EMailForm", "Mail Adresi"))
        self.label_3.setText(_translate("EMailForm", "Yeni Mail Adresi"))
        self.btn_login.setText(_translate("EMailForm", "Yoklamayı Gönder"))


import resoruces_rc
