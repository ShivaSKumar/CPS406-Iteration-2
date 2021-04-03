# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SQ_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SQ_Dialog(object):
    def setupUi(self, SQ_Dialog):
        SQ_Dialog.setObjectName("SQ_Dialog")
        SQ_Dialog.resize(640, 480)
        self.security_answer = QtWidgets.QLineEdit(SQ_Dialog)
        self.security_answer.setGeometry(QtCore.QRect(190, 300, 381, 51))
        self.security_answer.setObjectName("security_answer")
        self.question_label = QtWidgets.QLabel(SQ_Dialog)
        self.question_label.setGeometry(QtCore.QRect(20, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.question_label.setFont(font)
        self.question_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.question_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.question_label.setObjectName("question_label")
        self.answer_label = QtWidgets.QLabel(SQ_Dialog)
        self.answer_label.setGeometry(QtCore.QRect(50, 310, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.answer_label.setFont(font)
        self.answer_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.answer_label.setObjectName("answer_label")
        self.description_label = QtWidgets.QLabel(SQ_Dialog)
        self.description_label.setEnabled(True)
        self.description_label.setGeometry(QtCore.QRect(60, 30, 531, 121))
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(14)
        self.description_label.setFont(font)
        self.description_label.setStyleSheet("color:rgb(115, 210, 22)")
        self.description_label.setText("")
        self.description_label.setWordWrap(True)
        self.description_label.setObjectName("description_label")
        self.security_question = QtWidgets.QLineEdit(SQ_Dialog)
        self.security_question.setGeometry(QtCore.QRect(190, 170, 381, 51))
        self.security_question.setObjectName("security_question")
        self.OK_Button = QtWidgets.QPushButton(SQ_Dialog)
        self.OK_Button.setGeometry(QtCore.QRect(300, 410, 89, 25))
        self.OK_Button.setObjectName("OK_Button")

        #self.retranslateUi(SQ_Dialog)
        QtCore.QMetaObject.connectSlotsByName(SQ_Dialog)

    def retranslateUi_english(self, SQ_Dialog):
        _translate = QtCore.QCoreApplication.translate
        SQ_Dialog.setWindowTitle(_translate("SQ_Dialog", "Cypress"))
        self.question_label.setText(_translate("SQ_Dialog", "Your Question:"))
        self.answer_label.setText(_translate("SQ_Dialog", "Your Answer:"))
        self.OK_Button.setText(_translate("SQ_Dialog", "OK"))

    def retranslateUi_french(self, SQ_Dialog):
        _translate = QtCore.QCoreApplication.translate
        SQ_Dialog.setWindowTitle(_translate("SQ_Dialog", "Cypress"))
        self.question_label.setText(_translate("SQ_Dialog", "Votre question:"))
        self.OK_Button.setText(_translate("SQ_Dialog", "OK:"))

