# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectefitte.ui'
#
# Created: Wed Apr 20 03:35:20 2016
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SelectEfitTe(object):
    def setupUi(self, SelectEfitTe):
        SelectEfitTe.setObjectName(_fromUtf8("SelectEfitTe"))
        SelectEfitTe.resize(465, 551)
        self.verticalLayout = QtGui.QVBoxLayout(SelectEfitTe)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(SelectEfitTe)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_7 = QtGui.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.rbMdsPlus = QtGui.QRadioButton(self.frame)
        self.rbMdsPlus.setObjectName(_fromUtf8("rbMdsPlus"))
        self.gridLayout_7.addWidget(self.rbMdsPlus, 0, 2, 1, 1)
        self.rbFile = QtGui.QRadioButton(self.frame)
        self.rbFile.setChecked(True)
        self.rbFile.setObjectName(_fromUtf8("rbFile"))
        self.gridLayout_7.addWidget(self.rbFile, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(SelectEfitTe)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.rbRZMap = QtGui.QRadioButton(self.frame_2)
        self.rbRZMap.setChecked(True)
        self.rbRZMap.setObjectName(_fromUtf8("rbRZMap"))
        self.verticalLayout_2.addWidget(self.rbRZMap)
        self.rbRhoMap = QtGui.QRadioButton(self.frame_2)
        self.rbRhoMap.setObjectName(_fromUtf8("rbRhoMap"))
        self.verticalLayout_2.addWidget(self.rbRhoMap)
        self.rbPsiMap = QtGui.QRadioButton(self.frame_2)
        self.rbPsiMap.setObjectName(_fromUtf8("rbPsiMap"))
        self.verticalLayout_2.addWidget(self.rbPsiMap)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 2, 1)
        self.line = QtGui.QFrame(self.frame_2)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 0, 1, 2, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lGFileDir = QtGui.QLabel(self.frame_2)
        self.lGFileDir.setObjectName(_fromUtf8("lGFileDir"))
        self.horizontalLayout_2.addWidget(self.lGFileDir)
        self.leGFileDir = QtGui.QLineEdit(self.frame_2)
        self.leGFileDir.setDragEnabled(True)
        self.leGFileDir.setObjectName(_fromUtf8("leGFileDir"))
        self.horizontalLayout_2.addWidget(self.leGFileDir)
        self.tbGFileDir = QtGui.QToolButton(self.frame_2)
        self.tbGFileDir.setObjectName(_fromUtf8("tbGFileDir"))
        self.horizontalLayout_2.addWidget(self.tbGFileDir)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 2, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lDataDir = QtGui.QLabel(self.frame_2)
        self.lDataDir.setObjectName(_fromUtf8("lDataDir"))
        self.horizontalLayout_3.addWidget(self.lDataDir)
        self.leDataDir = QtGui.QLineEdit(self.frame_2)
        self.leDataDir.setDragEnabled(True)
        self.leDataDir.setObjectName(_fromUtf8("leDataDir"))
        self.horizontalLayout_3.addWidget(self.leDataDir)
        self.tbData = QtGui.QToolButton(self.frame_2)
        self.tbData.setObjectName(_fromUtf8("tbData"))
        self.horizontalLayout_3.addWidget(self.tbData)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtGui.QFrame(SelectEfitTe)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.frame_4)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.spbShot = SpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spbShot.sizePolicy().hasHeightForWidth())
        self.spbShot.setSizePolicy(sizePolicy)
        self.spbShot.setMaximum(100000)
        self.spbShot.setObjectName(_fromUtf8("spbShot"))
        self.gridLayout.addWidget(self.spbShot, 0, 0, 1, 1)
        self.bUpdate = QtGui.QPushButton(self.groupBox)
        self.bUpdate.setObjectName(_fromUtf8("bUpdate"))
        self.gridLayout.addWidget(self.bUpdate, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.treeLayout = QtGui.QVBoxLayout()
        self.treeLayout.setSpacing(0)
        self.treeLayout.setObjectName(_fromUtf8("treeLayout"))
        self.lTree = QtGui.QLabel(self.frame_4)
        self.lTree.setFrameShape(QtGui.QFrame.Panel)
        self.lTree.setFrameShadow(QtGui.QFrame.Raised)
        self.lTree.setAlignment(QtCore.Qt.AlignCenter)
        self.lTree.setObjectName(_fromUtf8("lTree"))
        self.treeLayout.addWidget(self.lTree)
        self.listTree = QtGui.QListWidget(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listTree.sizePolicy().hasHeightForWidth())
        self.listTree.setSizePolicy(sizePolicy)
        self.listTree.setMaximumSize(QtCore.QSize(120, 16777215))
        self.listTree.setFrameShape(QtGui.QFrame.Panel)
        self.listTree.setObjectName(_fromUtf8("listTree"))
        self.treeLayout.addWidget(self.listTree)
        self.horizontalLayout.addLayout(self.treeLayout)
        self.timeLayout = QtGui.QVBoxLayout()
        self.timeLayout.setSpacing(0)
        self.timeLayout.setObjectName(_fromUtf8("timeLayout"))
        self.lTime = QtGui.QLabel(self.frame_4)
        self.lTime.setFrameShape(QtGui.QFrame.Panel)
        self.lTime.setFrameShadow(QtGui.QFrame.Raised)
        self.lTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lTime.setObjectName(_fromUtf8("lTime"))
        self.timeLayout.addWidget(self.lTime)
        self.listTime = QtGui.QListWidget(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listTime.sizePolicy().hasHeightForWidth())
        self.listTime.setSizePolicy(sizePolicy)
        self.listTime.setMaximumSize(QtCore.QSize(120, 16777215))
        self.listTime.setFrameShape(QtGui.QFrame.Panel)
        self.listTime.setObjectName(_fromUtf8("listTime"))
        self.timeLayout.addWidget(self.listTime)
        self.horizontalLayout.addLayout(self.timeLayout)
        spacerItem = QtGui.QSpacerItem(34, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtGui.QFrame(SelectEfitTe)
        self.frame_3.setEnabled(True)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.diagnostics1 = QtGui.QCheckBox(self.frame_3)
        self.diagnostics1.setEnabled(False)
        self.diagnostics1.setObjectName(_fromUtf8("diagnostics1"))
        self.gridLayout_3.addWidget(self.diagnostics1, 0, 0, 1, 1)
        self.diagnostics3 = QtGui.QCheckBox(self.frame_3)
        self.diagnostics3.setEnabled(False)
        self.diagnostics3.setObjectName(_fromUtf8("diagnostics3"))
        self.gridLayout_3.addWidget(self.diagnostics3, 2, 0, 1, 1)
        self.diagnostics4 = QtGui.QCheckBox(self.frame_3)
        self.diagnostics4.setEnabled(False)
        self.diagnostics4.setObjectName(_fromUtf8("diagnostics4"))
        self.gridLayout_3.addWidget(self.diagnostics4, 3, 0, 1, 1)
        self.diagnostics5 = QtGui.QCheckBox(self.frame_3)
        self.diagnostics5.setEnabled(False)
        self.diagnostics5.setObjectName(_fromUtf8("diagnostics5"))
        self.gridLayout_3.addWidget(self.diagnostics5, 4, 0, 1, 1)
        self.diagnostics2 = QtGui.QCheckBox(self.frame_3)
        self.diagnostics2.setEnabled(False)
        self.diagnostics2.setObjectName(_fromUtf8("diagnostics2"))
        self.gridLayout_3.addWidget(self.diagnostics2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        spacerItem1 = QtGui.QSpacerItem(20, 87, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(SelectEfitTe)
        QtCore.QObject.connect(self.rbFile, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame_2.show)
        QtCore.QObject.connect(self.rbFile, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame_3.hide)
        QtCore.QObject.connect(self.rbMdsPlus, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame_2.hide)
        QtCore.QObject.connect(self.rbMdsPlus, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame_3.show)
        QtCore.QObject.connect(self.rbFile, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame_4.hide)
        QtCore.QObject.connect(self.rbMdsPlus, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame_4.show)
        QtCore.QObject.connect(self.rbRhoMap, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.leGFileDir.setDisabled)
        QtCore.QObject.connect(self.rbRhoMap, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.tbGFileDir.setDisabled)
        QtCore.QObject.connect(self.rbPsiMap, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.leGFileDir.setDisabled)
        QtCore.QObject.connect(self.rbPsiMap, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.tbGFileDir.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(SelectEfitTe)

    def retranslateUi(self, SelectEfitTe):
        self.rbMdsPlus.setText(QtGui.QApplication.translate("SelectEfitTe", "MDS+ Server", None, QtGui.QApplication.UnicodeUTF8))
        self.rbFile.setText(QtGui.QApplication.translate("SelectEfitTe", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SelectEfitTe", "Select Efit From:", None, QtGui.QApplication.UnicodeUTF8))
        self.rbRZMap.setText(QtGui.QApplication.translate("SelectEfitTe", "RZ Map", None, QtGui.QApplication.UnicodeUTF8))
        self.rbRhoMap.setText(QtGui.QApplication.translate("SelectEfitTe", "Rho Map", None, QtGui.QApplication.UnicodeUTF8))
        self.rbPsiMap.setText(QtGui.QApplication.translate("SelectEfitTe", "Psi Map", None, QtGui.QApplication.UnicodeUTF8))
        self.lGFileDir.setText(QtGui.QApplication.translate("SelectEfitTe", "GFile Dir:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbGFileDir.setText(QtGui.QApplication.translate("SelectEfitTe", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.lDataDir.setText(QtGui.QApplication.translate("SelectEfitTe", "Data Dir:", None, QtGui.QApplication.UnicodeUTF8))
        self.tbData.setText(QtGui.QApplication.translate("SelectEfitTe", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SelectEfitTe", "Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.bUpdate.setText(QtGui.QApplication.translate("SelectEfitTe", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.lTree.setText(QtGui.QApplication.translate("SelectEfitTe", "Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.lTime.setText(QtGui.QApplication.translate("SelectEfitTe", "Time", None, QtGui.QApplication.UnicodeUTF8))
        self.diagnostics1.setText(QtGui.QApplication.translate("SelectEfitTe", "Thomson (Core)", None, QtGui.QApplication.UnicodeUTF8))
        self.diagnostics3.setText(QtGui.QApplication.translate("SelectEfitTe", "ECE", None, QtGui.QApplication.UnicodeUTF8))
        self.diagnostics4.setText(QtGui.QApplication.translate("SelectEfitTe", "Michelson", None, QtGui.QApplication.UnicodeUTF8))
        self.diagnostics5.setText(QtGui.QApplication.translate("SelectEfitTe", "TXCS", None, QtGui.QApplication.UnicodeUTF8))
        self.diagnostics2.setText(QtGui.QApplication.translate("SelectEfitTe", "Thomson (Edge)", None, QtGui.QApplication.UnicodeUTF8))

from spinbox import SpinBox

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SelectEfitTe = QtGui.QWidget()
    ui = Ui_SelectEfitTe()
    ui.setupUi(SelectEfitTe)
    SelectEfitTe.show()
    sys.exit(app.exec_())

