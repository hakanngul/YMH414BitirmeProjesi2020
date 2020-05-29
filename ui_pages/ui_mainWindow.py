# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_pages\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1361, 646)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("")
        self.Window = QtWidgets.QWidget(MainWindow)
        self.Window.setStyleSheet("QWidget{background: #354152;}\n"
                                  "QLabel{color:white;}\n"
                                  "QTableWidget{background:white;}\n"
                                  "QTableWidget::item {\n"
                                  "    background-color: white;\n"
                                  "    color:black;\n"
                                  "}")
        self.Window.setObjectName("Window")
        self.kamera_ekrani = QtWidgets.QLabel(self.Window)
        self.kamera_ekrani.setGeometry(QtCore.QRect(0, 120, 800, 470))
        self.kamera_ekrani.setMinimumSize(QtCore.QSize(800, 470))
        self.kamera_ekrani.setMaximumSize(QtCore.QSize(800, 470))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.kamera_ekrani.setFont(font)
        self.kamera_ekrani.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.kamera_ekrani.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.kamera_ekrani.setStyleSheet("background-color: transparent;")
        self.kamera_ekrani.setAlignment(QtCore.Qt.AlignCenter)
        self.kamera_ekrani.setObjectName("kamera_ekrani")
        self.sinif_listesi = QtWidgets.QTableWidget(self.Window)
        self.sinif_listesi.setGeometry(QtCore.QRect(800, 120, 551, 491))
        self.sinif_listesi.setStyleSheet("selection-background-color: rgb(233, 185, 110);")
        self.sinif_listesi.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.sinif_listesi.setObjectName("sinif_listesi")
        self.sinif_listesi.setColumnCount(4)
        self.sinif_listesi.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.sinif_listesi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.sinif_listesi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sinif_listesi.setHorizontalHeaderItem(3, item)
        self.ogrenci_info = QtWidgets.QFrame(self.Window)
        self.ogrenci_info.setEnabled(True)
        self.ogrenci_info.setGeometry(QtCore.QRect(0, 0, 800, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ogrenci_info.sizePolicy().hasHeightForWidth())
        self.ogrenci_info.setSizePolicy(sizePolicy)
        self.ogrenci_info.setMinimumSize(QtCore.QSize(800, 80))
        self.ogrenci_info.setFrameShape(QtWidgets.QFrame.Box)
        self.ogrenci_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ogrenci_info.setLineWidth(1)
        self.ogrenci_info.setMidLineWidth(1)
        self.ogrenci_info.setObjectName("ogrenci_info")
        self.labelGirisCikis_3 = QtWidgets.QLabel(self.ogrenci_info)
        self.labelGirisCikis_3.setGeometry(QtCore.QRect(130, 5, 131, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelGirisCikis_3.setFont(font)
        self.labelGirisCikis_3.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.labelGirisCikis_3.setObjectName("labelGirisCikis_3")
        self.label_adiSoyadi = QtWidgets.QLabel(self.ogrenci_info)
        self.label_adiSoyadi.setGeometry(QtCore.QRect(270, 8, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_adiSoyadi.setFont(font)
        self.label_adiSoyadi.setObjectName("label_adiSoyadi")
        self.label_okulNo = QtWidgets.QLabel(self.ogrenci_info)
        self.label_okulNo.setGeometry(QtCore.QRect(270, 45, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_okulNo.setFont(font)
        self.label_okulNo.setObjectName("label_okulNo")
        self.label_girilenDers = QtWidgets.QLabel(self.ogrenci_info)
        self.label_girilenDers.setGeometry(QtCore.QRect(270, 80, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_girilenDers.setFont(font)
        self.label_girilenDers.setObjectName("label_girilenDers")
        self.profile_picture = QtWidgets.QLabel(self.ogrenci_info)
        self.profile_picture.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.profile_picture.setStyleSheet("background:white;")
        self.profile_picture.setText("")
        self.profile_picture.setPixmap(QtGui.QPixmap("personReal.png"))
        self.profile_picture.setScaledContents(True)
        self.profile_picture.setObjectName("profile_picture")
        self.label = QtWidgets.QLabel(self.ogrenci_info)
        self.label.setGeometry(QtCore.QRect(510, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.ogrenci_info)
        self.label_2.setGeometry(QtCore.QRect(510, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.ogrenci_info)
        self.label_3.setGeometry(QtCore.QRect(510, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lbl_duygu = QtWidgets.QLabel(self.ogrenci_info)
        self.lbl_duygu.setGeometry(QtCore.QRect(690, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_duygu.setFont(font)
        self.lbl_duygu.setObjectName("lbl_duygu")
        self.lbl_yas = QtWidgets.QLabel(self.ogrenci_info)
        self.lbl_yas.setGeometry(QtCore.QRect(690, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_yas.setFont(font)
        self.lbl_yas.setObjectName("lbl_yas")
        self.lbl_cinsiyet = QtWidgets.QLabel(self.ogrenci_info)
        self.lbl_cinsiyet.setGeometry(QtCore.QRect(690, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lbl_cinsiyet.setFont(font)
        self.lbl_cinsiyet.setObjectName("lbl_cinsiyet")
        self.ders_info = QtWidgets.QFrame(self.Window)
        self.ders_info.setGeometry(QtCore.QRect(800, 0, 551, 120))
        self.ders_info.setFrameShape(QtWidgets.QFrame.Box)
        self.ders_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ders_info.setMidLineWidth(1)
        self.ders_info.setObjectName("ders_info")
        self.labelGirisCikis_4 = QtWidgets.QLabel(self.ders_info)
        self.labelGirisCikis_4.setGeometry(QtCore.QRect(5, 3, 161, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelGirisCikis_4.setFont(font)
        self.labelGirisCikis_4.setStyleSheet("background-color: rgba(0,0,0,0%)")
        self.labelGirisCikis_4.setObjectName("labelGirisCikis_4")
        self.label_dersKodu = QtWidgets.QLabel(self.ders_info)
        self.label_dersKodu.setGeometry(QtCore.QRect(180, 45, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_dersKodu.setFont(font)
        self.label_dersKodu.setObjectName("label_dersKodu")
        self.label_sinifMevcudu = QtWidgets.QLabel(self.ders_info)
        self.label_sinifMevcudu.setGeometry(QtCore.QRect(180, 80, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_sinifMevcudu.setFont(font)
        self.label_sinifMevcudu.setObjectName("label_sinifMevcudu")
        self.label_dersAdi = QtWidgets.QLabel(self.ders_info)
        self.label_dersAdi.setGeometry(QtCore.QRect(180, 5, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_dersAdi.setFont(font)
        self.label_dersAdi.setObjectName("label_dersAdi")
        MainWindow.setCentralWidget(self.Window)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1361, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuEkle = QtWidgets.QMenu(self.menubar)
        self.menuEkle.setObjectName("menuEkle")
        self.menuAyarlar = QtWidgets.QMenu(self.menubar)
        self.menuAyarlar.setObjectName("menuAyarlar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStartCam = QtWidgets.QAction(MainWindow)
        self.actionStartCam.setObjectName("actionStartCam")
        self.actionStopCam = QtWidgets.QAction(MainWindow)
        self.actionStopCam.setObjectName("actionStopCam")
        self.OgrenciEkle = QtWidgets.QAction(MainWindow)
        self.OgrenciEkle.setObjectName("OgrenciEkle")
        self.OgretmenEkle = QtWidgets.QAction(MainWindow)
        self.OgretmenEkle.setObjectName("OgretmenEkle")
        self.actiondeneme5 = QtWidgets.QAction(MainWindow)
        self.actiondeneme5.setObjectName("actiondeneme5")
        self.action6 = QtWidgets.QAction(MainWindow)
        self.action6.setObjectName("action6")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.DersEkle = QtWidgets.QAction(MainWindow)
        self.DersEkle.setObjectName("DersEkle")
        self.action_OgrenciListesi = QtWidgets.QAction(MainWindow)
        self.action_OgrenciListesi.setObjectName("action_OgrenciListesi")
        self.action_OgrenciAra = QtWidgets.QAction(MainWindow)
        self.action_OgrenciAra.setObjectName("action_OgrenciAra")
        self.actionYoklamayiBitir = QtWidgets.QAction(MainWindow)
        self.actionYoklamayiBitir.setObjectName("actionYoklamayiBitir")
        self.menuMenu.addAction(self.actionStartCam)
        self.menuMenu.addAction(self.actionStopCam)
        self.menuMenu.addAction(self.actionYoklamayiBitir)
        self.menuEkle.addAction(self.OgrenciEkle)
        self.menuEkle.addAction(self.OgretmenEkle)
        self.menuEkle.addAction(self.DersEkle)
        self.menuAyarlar.addAction(self.actiondeneme5)
        self.menuAyarlar.addAction(self.action_OgrenciListesi)
        self.menuAyarlar.addAction(self.action_OgrenciAra)
        self.menuExit.addAction(self.actionExit)
        self.menuExit.addSeparator()
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuEkle.menuAction())
        self.menubar.addAction(self.menuAyarlar.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.kamera_ekrani.setText(_translate("MainWindow", "TextLabel"))
        self.sinif_listesi.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p>Öğrencilerin Bulunduğu Liste</p></body></html>"))
        item = self.sinif_listesi.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.sinif_listesi.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.sinif_listesi.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.sinif_listesi.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.sinif_listesi.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.sinif_listesi.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.sinif_listesi.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.sinif_listesi.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.sinif_listesi.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "10"))
        item = self.sinif_listesi.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "11"))
        item = self.sinif_listesi.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "12"))
        item = self.sinif_listesi.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "13"))
        item = self.sinif_listesi.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "14"))
        item = self.sinif_listesi.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "16"))
        item = self.sinif_listesi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Öğrenci No"))
        item = self.sinif_listesi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Adı Soyadı"))
        item = self.sinif_listesi.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Yoklama Durumu"))
        item = self.sinif_listesi.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tarih"))
        self.labelGirisCikis_3.setText(_translate("MainWindow",
                                                  "<html><head/><body><p>Adı Soyadı :</p><p>Okul No :</p><p>Girdiği Ders :</p></body></html>"))
        self.label_adiSoyadi.setText(_translate("MainWindow", "Adı Soyadı"))
        self.label_okulNo.setText(_translate("MainWindow", "Okul No"))
        self.label_girilenDers.setText(_translate("MainWindow", "Girilen Ders"))
        self.label.setText(_translate("MainWindow", "Duygu Durumu :"))
        self.label_2.setText(_translate("MainWindow", "Tahmini Yaşı :"))
        self.label_3.setText(_translate("MainWindow", "Tahmini Cinsiyeti :"))
        self.lbl_duygu.setText(_translate("MainWindow", "NULL"))
        self.lbl_yas.setText(_translate("MainWindow", "NULL"))
        self.lbl_cinsiyet.setText(_translate("MainWindow", "NULL"))
        self.labelGirisCikis_4.setText(_translate("MainWindow",
                                                  "<html><head/><body><p>Ders Adı :</p><p>Ders Kodu :</p><p>Sınıf Mevcudu :</p></body></html>"))
        self.label_dersKodu.setText(_translate("MainWindow", "Ders Kodu"))
        self.label_sinifMevcudu.setText(_translate("MainWindow", "Sınıf Mevcudu"))
        self.label_dersAdi.setText(_translate("MainWindow", "Ders Adı"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuEkle.setTitle(_translate("MainWindow", "Ekle"))
        self.menuAyarlar.setTitle(_translate("MainWindow", "Ayarlar"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionStartCam.setText(_translate("MainWindow", "Start Camera"))
        self.actionStopCam.setText(_translate("MainWindow", "Stop Camera"))
        self.OgrenciEkle.setText(_translate("MainWindow", "Öğrenci Ekle"))
        self.OgretmenEkle.setText(_translate("MainWindow", "Öğretmen Ekle"))
        self.actiondeneme5.setText(_translate("MainWindow", "Modelleri Yükle"))
        self.action6.setText(_translate("MainWindow", "deneme6"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.DersEkle.setText(_translate("MainWindow", "Ders Ekle"))
        self.action_OgrenciListesi.setText(_translate("MainWindow", "Öğrenci Listesi"))
        self.action_OgrenciAra.setText(_translate("MainWindow", "Öğrenci Ara"))
        self.actionYoklamayiBitir.setText(_translate("MainWindow", "Yoklamayı Bitir"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())