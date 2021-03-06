# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(633, 387)
        Form.setMinimumSize(QtCore.QSize(633, 387))
        Form.setMaximumSize(QtCore.QSize(633, 387))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 391))
        self.label.setMinimumSize(QtCore.QSize(641, 391))
        self.label.setMaximumSize(QtCore.QSize(641, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/login/images/fioletovyi-fon-uzor-tekstura-purple-abstract-ornamental-flow.jpg"))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(4, 7, 615, 369))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.ReadButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.ReadButton_3.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ReadButton_3.setFont(font)
        self.ReadButton_3.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.ReadButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/login/images/640824_document_512x512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ReadButton_3.setIcon(icon)
        self.ReadButton_3.setIconSize(QtCore.QSize(70, 70))
        self.ReadButton_3.setObjectName("ReadButton_3")
        self.verticalLayout_5.addWidget(self.ReadButton_3)
        self.BrowseButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.BrowseButton_2.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.BrowseButton_2.setFont(font)
        self.BrowseButton_2.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"")
        self.BrowseButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/1935395-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BrowseButton_2.setIcon(icon1)
        self.BrowseButton_2.setIconSize(QtCore.QSize(70, 70))
        self.BrowseButton_2.setObjectName("BrowseButton_2")
        self.verticalLayout_5.addWidget(self.BrowseButton_2)
        self.ReadButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.ReadButton_4.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ReadButton_4.setFont(font)
        self.ReadButton_4.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.ReadButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/login/images/audio-1570013-1329744.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ReadButton_4.setIcon(icon2)
        self.ReadButton_4.setIconSize(QtCore.QSize(70, 70))
        self.ReadButton_4.setObjectName("ReadButton_4")
        self.verticalLayout_5.addWidget(self.ReadButton_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.PathTextBox_2 = QtWidgets.QLabel(self.layoutWidget)
        self.PathTextBox_2.setMinimumSize(QtCore.QSize(501, 211))
        self.PathTextBox_2.setStyleSheet("background-color: rgb(51, 0, 77);")
        self.PathTextBox_2.setText("")
        self.PathTextBox_2.setObjectName("PathTextBox_2")
        self.verticalLayout_6.addWidget(self.PathTextBox_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.ResultTextBox_2 = QtWidgets.QLabel(self.layoutWidget)
        self.ResultTextBox_2.setMinimumSize(QtCore.QSize(501, 91))
        self.ResultTextBox_2.setStyleSheet("background-color: rgb(51, 0, 77);")
        self.ResultTextBox_2.setText("")
        self.ResultTextBox_2.setObjectName("ResultTextBox_2")
        self.verticalLayout_6.addWidget(self.ResultTextBox_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OCR App"))
        self.label_3.setText(_translate("Form", "OCR APP"))
import app_resources_rc
