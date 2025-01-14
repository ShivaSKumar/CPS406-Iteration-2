# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrontScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrontScreen(object):
    def setupUi(self, FrontScreen):
        FrontScreen.setObjectName("FrontScreen")
        FrontScreen.resize(811, 468)
        FrontScreen.setWindowTitle("Cypress")
        FrontScreen.setWindowOpacity(2.0)
        FrontScreen.setAutoFillBackground(False)
        FrontScreen.setStyleSheet("")
        FrontScreen.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(FrontScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(290, 10, 261, 71))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Header.setFont(font)
        self.Header.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Header.setAutoFillBackground(False)
        self.Header.setLineWidth(1)
        self.Header.setMidLineWidth(0)
        self.Header.setWordWrap(False)
        self.Header.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.Header.setObjectName("Header")
        self.english_button = QtWidgets.QPushButton(self.centralwidget)
        self.english_button.setGeometry(QtCore.QRect(150, 320, 89, 25))
        self.english_button.setFlat(False)
        self.english_button.setObjectName("english_button")
        self.french_button = QtWidgets.QPushButton(self.centralwidget)
        self.french_button.setGeometry(QtCore.QRect(570, 320, 89, 25))
        self.french_button.setObjectName("french_button")
        self.main_screen_text = QtWidgets.QLabel(self.centralwidget)
        self.main_screen_text.setGeometry(QtCore.QRect(280, 270, 271, 31))
        font = QtGui.QFont()
        font.setFamily("FreeSans")
        font.setPointSize(20)
        self.main_screen_text.setFont(font)
        self.main_screen_text.setAlignment(QtCore.Qt.AlignCenter)
        self.main_screen_text.setObjectName("main_screen_text")
        self.faq_button = QtWidgets.QPushButton(self.centralwidget)
        self.faq_button.setGeometry(QtCore.QRect(730, 410, 71, 21))
        self.faq_button.setFlat(True)
        self.faq_button.setObjectName("faq_button")
        self.toronto_logo_label = QtWidgets.QLabel(self.centralwidget)
        self.toronto_logo_label.setGeometry(QtCore.QRect(340, 140, 141, 91))
        self.toronto_logo_label.setText("")
        self.toronto_logo_label.setPixmap(QtGui.QPixmap("images/toronto_logo.jpg"))
        self.toronto_logo_label.setObjectName("toronto_logo_label")
        FrontScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FrontScreen)
        self.statusbar.setObjectName("statusbar")
        FrontScreen.setStatusBar(self.statusbar)

        self.retranslateUi(FrontScreen)
        QtCore.QMetaObject.connectSlotsByName(FrontScreen)

    def retranslateUi(self, FrontScreen):
        _translate = QtCore.QCoreApplication.translate
        self.Header.setText(_translate("FrontScreen", "CYPRESS"))
        self.english_button.setText(_translate("FrontScreen", "English"))
        self.french_button.setText(_translate("FrontScreen", "French"))
        self.main_screen_text.setText(_translate("FrontScreen", "City of Toronto"))
        self.faq_button.setText(_translate("FrontScreen", "FAQ"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrontScreen = QtWidgets.QMainWindow()
    ui = Ui_FrontScreen()
    ui.setupUi(FrontScreen)
    FrontScreen.show()
    sys.exit(app.exec_())


