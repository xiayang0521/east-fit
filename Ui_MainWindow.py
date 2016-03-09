# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1158, 668)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(515, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.bManFit = QtGui.QPushButton(self.tab_3)
        self.bManFit.setGeometry(QtCore.QRect(170, 180, 81, 31))
        self.bManFit.setObjectName(_fromUtf8("bManFit"))
        self.sKnotsNum = QtGui.QSlider(self.tab_3)
        self.sKnotsNum.setGeometry(QtCore.QRect(119, 140, 131, 20))
        self.sKnotsNum.setMinimum(5)
        self.sKnotsNum.setMaximum(9)
        self.sKnotsNum.setPageStep(1)
        self.sKnotsNum.setProperty("value", 5)
        self.sKnotsNum.setOrientation(QtCore.Qt.Horizontal)
        self.sKnotsNum.setObjectName(_fromUtf8("sKnotsNum"))
        self.lKnotsNum = QtGui.QLabel(self.tab_3)
        self.lKnotsNum.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.lKnotsNum.setObjectName(_fromUtf8("lKnotsNum"))
        self.lShowKnotsNum = QtGui.QLabel(self.tab_3)
        self.lShowKnotsNum.setGeometry(QtCore.QRect(180, 120, 68, 17))
        self.lShowKnotsNum.setScaledContents(True)
        self.lShowKnotsNum.setObjectName(_fromUtf8("lShowKnotsNum"))
        self.cbFunctionSelect = QtGui.QComboBox(self.tab_3)
        self.cbFunctionSelect.setGeometry(QtCore.QRect(50, 180, 91, 21))
        self.cbFunctionSelect.setObjectName(_fromUtf8("cbFunctionSelect"))
        self.cbFunctionSelect.addItem(_fromUtf8(""))
        self.cbFunctionSelect.addItem(_fromUtf8(""))
        self.cbFunctionSelect.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(634, 0))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mplCanvas = MplCanvasWrapper(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCanvas.sizePolicy().hasHeightForWidth())
        self.mplCanvas.setSizePolicy(sizePolicy)
        self.mplCanvas.setObjectName(_fromUtf8("mplCanvas"))
        self.gridLayout.addWidget(self.mplCanvas, 0, 0, 1, 9)
        self.lDataDescription = QtGui.QLabel(self.frame)
        self.lDataDescription.setObjectName(_fromUtf8("lDataDescription"))
        self.gridLayout.addWidget(self.lDataDescription, 1, 0, 1, 3)
        self.cRhoPsi = QtGui.QComboBox(self.frame)
        self.cRhoPsi.setObjectName(_fromUtf8("cRhoPsi"))
        self.cRhoPsi.addItem(_fromUtf8(""))
        self.cRhoPsi.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cRhoPsi, 1, 8, 1, 1)
        self.lEfit = QtGui.QLabel(self.frame)
        self.lEfit.setObjectName(_fromUtf8("lEfit"))
        self.gridLayout.addWidget(self.lEfit, 2, 0, 1, 1)
        self.lShot2 = QtGui.QLabel(self.frame)
        self.lShot2.setObjectName(_fromUtf8("lShot2"))
        self.gridLayout.addWidget(self.lShot2, 2, 1, 1, 1)
        self.lShowShot = QtGui.QLabel(self.frame)
        self.lShowShot.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lShowShot.setFrameShape(QtGui.QFrame.Panel)
        self.lShowShot.setFrameShadow(QtGui.QFrame.Sunken)
        self.lShowShot.setObjectName(_fromUtf8("lShowShot"))
        self.gridLayout.addWidget(self.lShowShot, 2, 2, 1, 2)
        self.lTime2 = QtGui.QLabel(self.frame)
        self.lTime2.setObjectName(_fromUtf8("lTime2"))
        self.gridLayout.addWidget(self.lTime2, 2, 4, 1, 1)
        self.lShowTime = QtGui.QLabel(self.frame)
        self.lShowTime.setMinimumSize(QtCore.QSize(46, 0))
        self.lShowTime.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lShowTime.setFrameShape(QtGui.QFrame.Panel)
        self.lShowTime.setFrameShadow(QtGui.QFrame.Sunken)
        self.lShowTime.setObjectName(_fromUtf8("lShowTime"))
        self.gridLayout.addWidget(self.lShowTime, 2, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(324, 14, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 6, 1, 3)
        self.lShot1 = QtGui.QLabel(self.frame)
        self.lShot1.setObjectName(_fromUtf8("lShot1"))
        self.gridLayout.addWidget(self.lShot1, 3, 0, 1, 1)
        self.sShot = QtGui.QSpinBox(self.frame)
        self.sShot.setMaximum(100000)
        self.sShot.setProperty("value", 100000)
        self.sShot.setObjectName(_fromUtf8("sShot"))
        self.gridLayout.addWidget(self.sShot, 3, 1, 1, 2)
        self.lTime1 = QtGui.QLabel(self.frame)
        self.lTime1.setObjectName(_fromUtf8("lTime1"))
        self.gridLayout.addWidget(self.lTime1, 3, 3, 1, 1)
        self.sTime = QtGui.QSpinBox(self.frame)
        self.sTime.setMaximum(100000)
        self.sTime.setProperty("value", 3000)
        self.sTime.setObjectName(_fromUtf8("sTime"))
        self.gridLayout.addWidget(self.sTime, 3, 4, 1, 1)
        self.bPlot = QtGui.QPushButton(self.frame)
        self.bPlot.setObjectName(_fromUtf8("bPlot"))
        self.gridLayout.addWidget(self.bPlot, 3, 5, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(65, 22, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 7, 1, 1)
        self.bSave = QtGui.QPushButton(self.frame)
        self.bSave.setObjectName(_fromUtf8("bSave"))
        self.gridLayout.addWidget(self.bSave, 3, 8, 1, 1)
        self.mplCanvas.raise_()
        self.lDataDescription.raise_()
        self.cRhoPsi.raise_()
        self.bSave.raise_()
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.lShot1.setBuddy(self.sShot)
        self.lTime1.setBuddy(self.sTime)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.sKnotsNum, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lShowKnotsNum.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Whatever Name", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "data control", None))
        self.bManFit.setText(_translate("MainWindow", "Manual Fit", None))
        self.lKnotsNum.setText(_translate("MainWindow", "Number of knots:", None))
        self.lShowKnotsNum.setText(_translate("MainWindow", "5", None))
        self.cbFunctionSelect.setItemText(0, _translate("MainWindow", "tanh_multi", None))
        self.cbFunctionSelect.setItemText(1, _translate("MainWindow", "tanh_0out", None))
        self.cbFunctionSelect.setItemText(2, _translate("MainWindow", "tsplfun", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "fit control", None))
        self.lDataDescription.setText(_translate("MainWindow", "Data Description:", None))
        self.cRhoPsi.setItemText(0, _translate("MainWindow", "rho", None))
        self.cRhoPsi.setItemText(1, _translate("MainWindow", "psi", None))
        self.lEfit.setText(_translate("MainWindow", "Efit:", None))
        self.lShot2.setText(_translate("MainWindow", "Shot:", None))
        self.lShowShot.setText(_translate("MainWindow", "100000", None))
        self.lTime2.setText(_translate("MainWindow", "Time(msec):", None))
        self.lShowTime.setText(_translate("MainWindow", "3000", None))
        self.lShot1.setText(_translate("MainWindow", "Shot:", None))
        self.lTime1.setText(_translate("MainWindow", "Time:", None))
        self.bPlot.setText(_translate("MainWindow", "Plot", None))
        self.bSave.setText(_translate("MainWindow", "Save", None))

from mplCanvasWrapper import MplCanvasWrapper
