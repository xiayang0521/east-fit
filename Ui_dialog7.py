# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog7.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog7(object):
    def setupUi(self, Dialog7):
        Dialog7.setObjectName(_fromUtf8("Dialog7"))
        Dialog7.resize(680, 337)
        Dialog7.setMaximumSize(QtCore.QSize(680, 337))
        self.gridLayout = QtGui.QGridLayout(Dialog7)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setVerticalSpacing(0)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.spb7 = QtGui.QSpinBox(Dialog7)
        self.spb7.setObjectName(_fromUtf8("spb7"))
        self.horizontalLayout_8.addWidget(self.spb7)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.spb8 = QtGui.QSpinBox(Dialog7)
        self.spb8.setObjectName(_fromUtf8("spb8"))
        self.horizontalLayout_8.addWidget(self.spb8)
        self.formLayout_4.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_8)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(16)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.lNm4 = QtGui.QLabel(Dialog7)
        self.lNm4.setObjectName(_fromUtf8("lNm4"))
        self.horizontalLayout_7.addWidget(self.lNm4)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.lDig4 = QtGui.QLabel(Dialog7)
        self.lDig4.setObjectName(_fromUtf8("lDig4"))
        self.horizontalLayout_7.addWidget(self.lDig4)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.chb4 = QtGui.QCheckBox(Dialog7)
        self.chb4.setText(_fromUtf8(""))
        self.chb4.setObjectName(_fromUtf8("chb4"))
        self.horizontalLayout_7.addWidget(self.chb4)
        self.formLayout_4.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_7)
        self.sld4 = QtGui.QSlider(Dialog7)
        self.sld4.setOrientation(QtCore.Qt.Horizontal)
        self.sld4.setObjectName(_fromUtf8("sld4"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.SpanningRole, self.sld4)
        self.gridLayout.addLayout(self.formLayout_4, 1, 0, 1, 1)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setVerticalSpacing(0)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.spb9 = QtGui.QSpinBox(Dialog7)
        self.spb9.setObjectName(_fromUtf8("spb9"))
        self.horizontalLayout_10.addWidget(self.spb9)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.spb10 = QtGui.QSpinBox(Dialog7)
        self.spb10.setObjectName(_fromUtf8("spb10"))
        self.horizontalLayout_10.addWidget(self.spb10)
        self.formLayout_5.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_10)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(16)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.lNm5 = QtGui.QLabel(Dialog7)
        self.lNm5.setObjectName(_fromUtf8("lNm5"))
        self.horizontalLayout_9.addWidget(self.lNm5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.lDig5 = QtGui.QLabel(Dialog7)
        self.lDig5.setObjectName(_fromUtf8("lDig5"))
        self.horizontalLayout_9.addWidget(self.lDig5)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.chb5 = QtGui.QCheckBox(Dialog7)
        self.chb5.setText(_fromUtf8(""))
        self.chb5.setObjectName(_fromUtf8("chb5"))
        self.horizontalLayout_9.addWidget(self.chb5)
        self.formLayout_5.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_9)
        self.sld5 = QtGui.QSlider(Dialog7)
        self.sld5.setOrientation(QtCore.Qt.Horizontal)
        self.sld5.setObjectName(_fromUtf8("sld5"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.SpanningRole, self.sld5)
        self.gridLayout.addLayout(self.formLayout_5, 1, 1, 1, 1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.spb3 = QtGui.QSpinBox(Dialog7)
        self.spb3.setObjectName(_fromUtf8("spb3"))
        self.horizontalLayout_4.addWidget(self.spb3)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.spb4 = QtGui.QSpinBox(Dialog7)
        self.spb4.setObjectName(_fromUtf8("spb4"))
        self.horizontalLayout_4.addWidget(self.spb4)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lNm2 = QtGui.QLabel(Dialog7)
        self.lNm2.setObjectName(_fromUtf8("lNm2"))
        self.horizontalLayout_3.addWidget(self.lNm2)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.lDig2 = QtGui.QLabel(Dialog7)
        self.lDig2.setObjectName(_fromUtf8("lDig2"))
        self.horizontalLayout_3.addWidget(self.lDig2)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.chb2 = QtGui.QCheckBox(Dialog7)
        self.chb2.setText(_fromUtf8(""))
        self.chb2.setObjectName(_fromUtf8("chb2"))
        self.horizontalLayout_3.addWidget(self.chb2)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_3)
        self.sld2 = QtGui.QSlider(Dialog7)
        self.sld2.setOrientation(QtCore.Qt.Horizontal)
        self.sld2.setObjectName(_fromUtf8("sld2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.sld2)
        self.gridLayout.addLayout(self.formLayout_2, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog7)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 3)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setVerticalSpacing(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.spb5 = QtGui.QSpinBox(Dialog7)
        self.spb5.setObjectName(_fromUtf8("spb5"))
        self.horizontalLayout_6.addWidget(self.spb5)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem13)
        self.spb6 = QtGui.QSpinBox(Dialog7)
        self.spb6.setObjectName(_fromUtf8("spb6"))
        self.horizontalLayout_6.addWidget(self.spb6)
        self.formLayout_3.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(16)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lNm3 = QtGui.QLabel(Dialog7)
        self.lNm3.setObjectName(_fromUtf8("lNm3"))
        self.horizontalLayout_5.addWidget(self.lNm3)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.lDig3 = QtGui.QLabel(Dialog7)
        self.lDig3.setObjectName(_fromUtf8("lDig3"))
        self.horizontalLayout_5.addWidget(self.lDig3)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.chb3 = QtGui.QCheckBox(Dialog7)
        self.chb3.setText(_fromUtf8(""))
        self.chb3.setObjectName(_fromUtf8("chb3"))
        self.horizontalLayout_5.addWidget(self.chb3)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_5)
        self.sld3 = QtGui.QSlider(Dialog7)
        self.sld3.setOrientation(QtCore.Qt.Horizontal)
        self.sld3.setObjectName(_fromUtf8("sld3"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.SpanningRole, self.sld3)
        self.gridLayout.addLayout(self.formLayout_3, 0, 2, 1, 1)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setVerticalSpacing(0)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.spb11 = QtGui.QSpinBox(Dialog7)
        self.spb11.setObjectName(_fromUtf8("spb11"))
        self.horizontalLayout_12.addWidget(self.spb11)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem16)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem17)
        self.spb12 = QtGui.QSpinBox(Dialog7)
        self.spb12.setObjectName(_fromUtf8("spb12"))
        self.horizontalLayout_12.addWidget(self.spb12)
        self.formLayout_6.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_12)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(16)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.lNm6 = QtGui.QLabel(Dialog7)
        self.lNm6.setObjectName(_fromUtf8("lNm6"))
        self.horizontalLayout_11.addWidget(self.lNm6)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem18)
        self.lDig6 = QtGui.QLabel(Dialog7)
        self.lDig6.setObjectName(_fromUtf8("lDig6"))
        self.horizontalLayout_11.addWidget(self.lDig6)
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem19)
        self.chb6 = QtGui.QCheckBox(Dialog7)
        self.chb6.setText(_fromUtf8(""))
        self.chb6.setObjectName(_fromUtf8("chb6"))
        self.horizontalLayout_11.addWidget(self.chb6)
        self.formLayout_6.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_11)
        self.sld6 = QtGui.QSlider(Dialog7)
        self.sld6.setOrientation(QtCore.Qt.Horizontal)
        self.sld6.setObjectName(_fromUtf8("sld6"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.SpanningRole, self.sld6)
        self.gridLayout.addLayout(self.formLayout_6, 1, 2, 1, 1)
        self.formLayout_1 = QtGui.QFormLayout()
        self.formLayout_1.setVerticalSpacing(0)
        self.formLayout_1.setObjectName(_fromUtf8("formLayout_1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.spb1 = QtGui.QSpinBox(Dialog7)
        self.spb1.setObjectName(_fromUtf8("spb1"))
        self.horizontalLayout_2.addWidget(self.spb1)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem20)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem21)
        self.spb2 = QtGui.QSpinBox(Dialog7)
        self.spb2.setObjectName(_fromUtf8("spb2"))
        self.horizontalLayout_2.addWidget(self.spb2)
        self.formLayout_1.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.horizontalLayout_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_1.setSpacing(16)
        self.horizontalLayout_1.setObjectName(_fromUtf8("horizontalLayout_1"))
        self.lNm1 = QtGui.QLabel(Dialog7)
        self.lNm1.setObjectName(_fromUtf8("lNm1"))
        self.horizontalLayout_1.addWidget(self.lNm1)
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem22)
        self.lDig1 = QtGui.QLabel(Dialog7)
        self.lDig1.setObjectName(_fromUtf8("lDig1"))
        self.horizontalLayout_1.addWidget(self.lDig1)
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_1.addItem(spacerItem23)
        self.chb1 = QtGui.QCheckBox(Dialog7)
        self.chb1.setText(_fromUtf8(""))
        self.chb1.setObjectName(_fromUtf8("chb1"))
        self.horizontalLayout_1.addWidget(self.chb1)
        self.formLayout_1.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_1)
        self.sld1 = QtGui.QSlider(Dialog7)
        self.sld1.setOrientation(QtCore.Qt.Horizontal)
        self.sld1.setObjectName(_fromUtf8("sld1"))
        self.formLayout_1.setWidget(1, QtGui.QFormLayout.SpanningRole, self.sld1)
        self.gridLayout.addLayout(self.formLayout_1, 0, 0, 1, 1)
        self.formLayout_7 = QtGui.QFormLayout()
        self.formLayout_7.setVerticalSpacing(0)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.spb13 = QtGui.QSpinBox(Dialog7)
        self.spb13.setObjectName(_fromUtf8("spb13"))
        self.horizontalLayout_14.addWidget(self.spb13)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem24)
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem25)
        self.spb14 = QtGui.QSpinBox(Dialog7)
        self.spb14.setObjectName(_fromUtf8("spb14"))
        self.horizontalLayout_14.addWidget(self.spb14)
        self.formLayout_7.setLayout(2, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_14)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(16)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.lNm7 = QtGui.QLabel(Dialog7)
        self.lNm7.setObjectName(_fromUtf8("lNm7"))
        self.horizontalLayout_13.addWidget(self.lNm7)
        spacerItem26 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem26)
        self.lDig7 = QtGui.QLabel(Dialog7)
        self.lDig7.setObjectName(_fromUtf8("lDig7"))
        self.horizontalLayout_13.addWidget(self.lDig7)
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem27)
        self.chb7 = QtGui.QCheckBox(Dialog7)
        self.chb7.setText(_fromUtf8(""))
        self.chb7.setObjectName(_fromUtf8("chb7"))
        self.horizontalLayout_13.addWidget(self.chb7)
        self.formLayout_7.setLayout(0, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_13)
        self.sld7 = QtGui.QSlider(Dialog7)
        self.sld7.setOrientation(QtCore.Qt.Horizontal)
        self.sld7.setObjectName(_fromUtf8("sld7"))
        self.formLayout_7.setWidget(1, QtGui.QFormLayout.SpanningRole, self.sld7)
        self.gridLayout.addLayout(self.formLayout_7, 2, 0, 1, 1)

        self.retranslateUi(Dialog7)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog7.reject)
        QtCore.QObject.connect(self.sld1, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lDig1.setNum)
        QtCore.QObject.connect(self.sld2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lDig2.setNum)
        QtCore.QObject.connect(self.sld3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lDig3.setNum)
        QtCore.QObject.connect(self.sld4, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lDig4.setNum)
        QtCore.QObject.connect(self.sld6, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lDig6.setNum)
        QtCore.QObject.connect(self.sld5, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lDig5.setNum)
        QtCore.QObject.connect(self.sld7, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lDig7.setNum)
        QtCore.QMetaObject.connectSlotsByName(Dialog7)

    def retranslateUi(self, Dialog7):
        Dialog7.setWindowTitle(_translate("Dialog7", "Manual Fit", None))
        self.spb7.setToolTip(_translate("Dialog7", "Max Value", None))
        self.spb8.setToolTip(_translate("Dialog7", "Min Value", None))
        self.lNm4.setToolTip(_translate("Dialog7", "OFFSET", None))
        self.lNm4.setText(_translate("Dialog7", "param No.4", None))
        self.lDig4.setText(_translate("Dialog7", "TextLabel", None))
        self.chb4.setToolTip(_translate("Dialog7", "CHECKED FIXES THE PARAMETER\n"
"UNCHECKED MAKES THE PARAMETER FREE.", None))
        self.sld4.setToolTip(_translate("Dialog7", "OFFSET", None))
        self.spb9.setToolTip(_translate("Dialog7", "Max Value", None))
        self.spb10.setToolTip(_translate("Dialog7", "Min Value", None))
        self.lNm5.setToolTip(_translate("Dialog7", "SLOPE INNER", None))
        self.lNm5.setText(_translate("Dialog7", "param No.5", None))
        self.lDig5.setText(_translate("Dialog7", "TextLabel", None))
        self.chb5.setToolTip(_translate("Dialog7", "CHECKED FIXES THE PARAMETER\n"
"UNCHECKED MAKES THE PARAMETER FREE.", None))
        self.sld5.setToolTip(_translate("Dialog7", "SLOPE INNER", None))
        self.spb3.setToolTip(_translate("Dialog7", "Max Value", None))
        self.spb4.setToolTip(_translate("Dialog7", "Min Value", None))
        self.lNm2.setToolTip(_translate("Dialog7", "FULL WIDTH", None))
        self.lNm2.setText(_translate("Dialog7", "param No.2", None))
        self.lDig2.setText(_translate("Dialog7", "TextLabel", None))
        self.chb2.setToolTip(_translate("Dialog7", "CHECKED FIXES THE PARAMETER\n"
"UNCHECKED MAKES THE PARAMETER FREE.", None))
        self.sld2.setToolTip(_translate("Dialog7", "FULL WIDTH", None))
        self.spb5.setToolTip(_translate("Dialog7", "Max Value", None))
        self.spb6.setToolTip(_translate("Dialog7", "Min Value", None))
        self.lNm3.setToolTip(_translate("Dialog7", "HEIGHT", None))
        self.lNm3.setText(_translate("Dialog7", "param No.3", None))
        self.lDig3.setText(_translate("Dialog7", "TextLabel", None))
        self.chb3.setToolTip(_translate("Dialog7", "CHECKED FIXES THE PARAMETER\n"
"UNCHECKED MAKES THE PARAMETER FREE.", None))
        self.sld3.setToolTip(_translate("Dialog7", "HEIGHT", None))
        self.spb11.setToolTip(_translate("Dialog7", "Max Value", None))
        self.spb12.setToolTip(_translate("Dialog7", "Min Value", None))
        self.lNm6.setToolTip(_translate("Dialog7", "QUADRADIC INNER", None))
        self.lNm6.setText(_translate("Dialog7", "param No.6", None))
        self.lDig6.setText(_translate("Dialog7", "TextLabel", None))
        self.chb6.setToolTip(_translate("Dialog7", "CHECKED FIXES THE PARAMETER\n"
"UNCHECKED MAKES THE PARAMETER FREE.", None))
        self.sld6.setToolTip(_translate("Dialog7", "QUADRADIC INNER", None))
        self.spb1.setToolTip(_translate("Dialog7", "Max Value", None))
        self.spb2.setToolTip(_translate("Dialog7", "Min Value", None))
        self.lNm1.setToolTip(_translate("Dialog7", "SYMMETRY POINT", None))
        self.lNm1.setText(_translate("Dialog7", "param No.1", None))
        self.lDig1.setText(_translate("Dialog7", "TextLabel", None))
        self.chb1.setToolTip(_translate("Dialog7", "CHECKED FIXES THE PARAMETER\n"
"UNCHECKED MAKES THE PARAMETER FREE.", None))
        self.sld1.setToolTip(_translate("Dialog7", "SYMMETRY POINT", None))
        self.spb13.setToolTip(_translate("Dialog7", "Max Value", None))
        self.spb14.setToolTip(_translate("Dialog7", "Min Value", None))
        self.lNm7.setToolTip(_translate("Dialog7", "SLOPE OUTER", None))
        self.lNm7.setText(_translate("Dialog7", "param No.6", None))
        self.lDig7.setText(_translate("Dialog7", "TextLabel", None))
        self.chb7.setToolTip(_translate("Dialog7", "CHECKED FIXES THE PARAMETER\n"
"UNCHECKED MAKES THE PARAMETER FREE.", None))
        self.sld7.setToolTip(_translate("Dialog7", "SLOPE OUTER", None))

