# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore

import param
from Ui_dialog6 import Ui_Dialog6


class Dialog6(QtGui.QDialog, Ui_Dialog6):
    """
    c includes three parts, sliders' value, spin boxes' value, check buttons' value
    shift = c[0][-1]
    """
    c = dict(
        Params=[[0, 0, 0, 0, 0, 0, 0], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [0, 0, 0, 0, 0, 0]])
    temp = param.GlobalVar6.value['Params']  # 临时存储

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        for btn in self.buttonBox.buttons():
            if self.buttonBox.buttonRole(btn) == QtGui.QDialogButtonBox.ResetRole:
                # QtCore.QObject.connect(btn, QtCore.SIGNAL(u"clicked()"), self.reset)
                btn.clicked.connect(self.reset)
        # for i in range(1, 6 + 1):
        #     setattr(self.__class__, "chb%d" % i, i).setChecked(True)
        self._initial()

    def reset(self):
        """
        reset values
        """
        self.spb1.setValue(0)
        self.spb2.setValue(1000)
        self.spb3.setValue(0)
        self.spb4.setValue(1000)
        self.spb5.setValue(0)
        self.spb6.setValue(3000)
        self.spb7.setValue(0)
        self.spb8.setValue(1000)
        self.spb9.setValue(0)
        self.spb10.setValue(1000)
        self.spb11.setValue(0)
        self.spb12.setValue(1000)
        self.spb13.setValue(-100)
        self.spb14.setValue(100)
        self.chb1.setCheckState(0)
        self.chb2.setCheckState(0)
        self.chb3.setCheckState(0)
        self.chb4.setCheckState(2)
        self.chb5.setCheckState(2)
        self.chb6.setCheckState(2)
        self.sld1.setMinimum(0)
        self.sld2.setMinimum(0)
        self.sld3.setMinimum(0)
        self.sld4.setMinimum(0)
        self.sld5.setMinimum(0)
        self.sld6.setMinimum(0)
        self.sld7.setMinimum(-100)
        self.sld1.setMaximum(1000)
        self.sld2.setMaximum(1000)
        self.sld3.setMaximum(3000)
        self.sld4.setMaximum(1000)
        self.sld5.setMaximum(1000)
        self.sld6.setMaximum(1000)
        self.sld7.setMaximum(100)
        self.sld1.setValue(950)
        self.sld2.setValue(100)
        self.sld3.setValue(2300)
        self.sld4.setValue(-100)
        self.sld5.setValue(0)
        self.sld6.setValue(0)
        self.sld7.setValue(0)
        self.lDig1.setNum(self.sld1.value())
        self.lDig2.setNum(self.sld2.value())
        self.lDig3.setNum(self.sld3.value())
        self.lDig4.setNum(self.sld4.value())
        self.lDig5.setNum(self.sld5.value())
        self.lDig6.setNum(self.sld6.value())
        self.lDig7.setNum(self.sld7.value())
        self.save()

    @QtCore.pyqtSignature("")
    def on_buttonBox_rejected(self):
        self.save()
        self.reject()

    @QtCore.pyqtSignature("")
    def on_buttonBox_accepted(self):
        self.save()
        self.accept()

    def _initial(self):
        # for x in xrange(15, 19 + 1):
        #     setattr(self.__class__, "spd%d" % x, staticmethod(self.QSpinBox.setMaximum(10)))
        #     print getattr(self.spd15, 'Minimum', 'no')
        self.sld1.setPageStep(1)
        self.sld2.setPageStep(1)
        self.sld3.setPageStep(1)
        self.sld4.setPageStep(1)
        self.sld5.setPageStep(1)
        self.sld6.setPageStep(1)
        self.sld7.setPageStep(1)
        self.spb1.setMinimum(-10000)
        self.spb2.setMinimum(-10000)
        self.spb3.setMinimum(-10000)
        self.spb4.setMinimum(-10000)
        self.spb5.setMinimum(-10000)
        self.spb6.setMinimum(-10000)
        self.spb7.setMinimum(-10000)
        self.spb8.setMinimum(-10000)
        self.spb9.setMinimum(-10000)
        self.spb10.setMinimum(-10000)
        self.spb11.setMinimum(-10000)
        self.spb12.setMinimum(-10000)
        self.spb13.setMinimum(-1000)
        self.spb14.setMinimum(-1000)
        self.spb1.setMaximum(10000)
        self.spb2.setMaximum(10000)
        self.spb3.setMaximum(10000)
        self.spb4.setMaximum(10000)
        self.spb5.setMaximum(10000)
        self.spb6.setMaximum(10000)
        self.spb7.setMaximum(10000)
        self.spb8.setMaximum(10000)
        self.spb9.setMaximum(10000)
        self.spb10.setMaximum(10000)
        self.spb11.setMaximum(10000)
        self.spb12.setMaximum(10000)
        self.spb13.setMaximum(1000)
        self.spb14.setMaximum(1000)
        if len(param.GlobalVar6.value['Params']) == 0:
            self.reset()
        else:
            self.chb1.setCheckState(param.GlobalVar6.value['Params'][2][0])
            self.chb2.setCheckState(param.GlobalVar6.value['Params'][2][1])
            self.chb3.setCheckState(param.GlobalVar6.value['Params'][2][2])
            self.chb4.setCheckState(param.GlobalVar6.value['Params'][2][3])
            self.chb5.setCheckState(param.GlobalVar6.value['Params'][2][4])
            self.chb6.setCheckState(param.GlobalVar6.value['Params'][2][5])
            self.spb1.setValue(param.GlobalVar6.value['Params'][1][0][0])
            self.spb2.setValue(param.GlobalVar6.value['Params'][1][0][1])
            self.spb3.setValue(param.GlobalVar6.value['Params'][1][1][0])
            self.spb4.setValue(param.GlobalVar6.value['Params'][1][1][1])
            self.spb5.setValue(param.GlobalVar6.value['Params'][1][2][0])
            self.spb6.setValue(param.GlobalVar6.value['Params'][1][2][1])
            self.spb7.setValue(param.GlobalVar6.value['Params'][1][3][0])
            self.spb8.setValue(param.GlobalVar6.value['Params'][1][3][1])
            self.spb9.setValue(param.GlobalVar6.value['Params'][1][4][0])
            self.spb10.setValue(param.GlobalVar6.value['Params'][1][4][1])
            self.spb11.setValue(param.GlobalVar6.value['Params'][1][5][0])
            self.spb12.setValue(param.GlobalVar6.value['Params'][1][5][1])
            self.spb13.setValue(param.GlobalVar6.value['Params'][1][6][0])
            self.spb14.setValue(param.GlobalVar6.value['Params'][1][6][1])
            self.spb2.setMinimum(self.spb1.value())
            self.spb1.setMaximum(self.spb2.value())
            self.spb4.setMinimum(self.spb3.value())
            self.spb3.setMaximum(self.spb4.value())
            self.spb6.setMinimum(self.spb5.value())
            self.spb5.setMaximum(self.spb6.value())
            self.spb8.setMinimum(self.spb7.value())
            self.spb7.setMaximum(self.spb8.value())
            self.spb10.setMinimum(self.spb9.value())
            self.spb9.setMaximum(self.spb10.value())
            self.spb12.setMinimum(self.spb11.value())
            self.spb11.setMaximum(self.spb12.value())
            self.spb14.setMinimum(self.spb13.value())
            self.spb13.setMaximum(self.spb14.value())
            self.sld1.setMinimum(self.spb1.value())
            self.sld1.setMaximum(self.spb2.value())
            self.sld2.setMinimum(self.spb3.value())
            self.sld2.setMaximum(self.spb4.value())
            self.sld3.setMinimum(self.spb5.value())
            self.sld3.setMaximum(self.spb6.value())
            self.sld4.setMinimum(self.spb7.value())
            self.sld4.setMaximum(self.spb8.value())
            self.sld5.setMinimum(self.spb9.value())
            self.sld5.setMaximum(self.spb10.value())
            self.sld6.setMinimum(self.spb11.value())
            self.sld6.setMaximum(self.spb12.value())
            self.sld7.setMinimum(self.spb13.value())
            self.sld7.setMaximum(self.spb14.value())
            self.sld1.setValue(param.GlobalVar6.value['Params'][0][0])
            self.sld2.setValue(param.GlobalVar6.value['Params'][0][1])
            self.sld3.setValue(param.GlobalVar6.value['Params'][0][2])
            self.sld4.setValue(param.GlobalVar6.value['Params'][0][3])
            self.sld5.setValue(param.GlobalVar6.value['Params'][0][4])
            self.sld6.setValue(param.GlobalVar6.value['Params'][0][5])
            self.sld7.setValue(param.GlobalVar6.value['Params'][0][6])
            self.lDig1.setNum(self.sld1.value())
            self.lDig2.setNum(self.sld2.value())
            self.lDig3.setNum(self.sld3.value())
            self.lDig4.setNum(self.sld4.value())
            self.lDig5.setNum(self.sld5.value())
            self.lDig6.setNum(self.sld6.value())
            self.lDig7.setNum(self.sld7.value())
        self.save()

    def save(self):
        self.c['Params'][0][0] = self.sld1.value()
        self.c['Params'][0][1] = self.sld2.value()
        self.c['Params'][0][2] = self.sld3.value()
        self.c['Params'][0][3] = self.sld4.value()
        self.c['Params'][0][4] = self.sld5.value()
        self.c['Params'][0][5] = self.sld6.value()
        self.c['Params'][0][6] = self.sld7.value()
        self.c['Params'][1][0][0] = self.spb1.value()
        self.c['Params'][1][0][1] = self.spb2.value()
        self.c['Params'][1][1][0] = self.spb3.value()
        self.c['Params'][1][1][1] = self.spb4.value()
        self.c['Params'][1][2][0] = self.spb5.value()
        self.c['Params'][1][2][1] = self.spb6.value()
        self.c['Params'][1][3][0] = self.spb7.value()
        self.c['Params'][1][3][1] = self.spb8.value()
        self.c['Params'][1][4][0] = self.spb9.value()
        self.c['Params'][1][4][1] = self.spb10.value()
        self.c['Params'][1][5][0] = self.spb11.value()
        self.c['Params'][1][5][1] = self.spb12.value()
        self.c['Params'][1][6][0] = self.spb13.value()
        self.c['Params'][1][6][1] = self.spb14.value()
        self.c['Params'][2][0] = self.chb1.checkState()
        self.c['Params'][2][1] = self.chb2.checkState()
        self.c['Params'][2][2] = self.chb3.checkState()
        self.c['Params'][2][3] = self.chb4.checkState()
        self.c['Params'][2][4] = self.chb5.checkState()
        self.c['Params'][2][5] = self.chb6.checkState()
        param.GlobalVar6(self.c)

    @QtCore.pyqtSignature("int")
    def on_spb1_valueChanged(self):
        self.sld1.setMinimum(self.spb1.value())
        self.spb2.setMinimum(self.spb1.value())

    @QtCore.pyqtSignature("int")
    def on_spb2_valueChanged(self):
        self.sld1.setMaximum(self.spb2.value())
        self.spb1.setMaximum(self.spb2.value())

    @QtCore.pyqtSignature("int")
    def on_spb3_valueChanged(self):
        self.sld2.setMinimum(self.spb3.value())
        self.spb4.setMinimum(self.spb3.value())

    @QtCore.pyqtSignature("int")
    def on_spb4_valueChanged(self):
        self.sld2.setMaximum(self.spb4.value())
        self.spb3.setMaximum(self.spb4.value())

    @QtCore.pyqtSignature("int")
    def on_spb5_valueChanged(self):
        self.sld3.setMinimum(self.spb5.value())
        self.spb6.setMinimum(self.spb5.value())

    @QtCore.pyqtSignature("int")
    def on_spb6_valueChanged(self):
        self.sld3.setMaximum(self.spb6.value())
        self.spb5.setMaximum(self.spb6.value())

    @QtCore.pyqtSignature("int")
    def on_spb7_valueChanged(self):
        self.sld4.setMinimum(self.spb7.value())
        self.spb8.setMinimum(self.spb7.value())

    @QtCore.pyqtSignature("int")
    def on_spb8_valueChanged(self):
        self.sld4.setMaximum(self.spb8.value())
        self.spb7.setMaximum(self.spb8.value())

    @QtCore.pyqtSignature("int")
    def on_spb9_valueChanged(self):
        self.sld5.setMinimum(self.spb9.value())
        self.spb10.setMinimum(self.spb9.value())

    @QtCore.pyqtSignature("int")
    def on_spb10_valueChanged(self):
        self.sld5.setMaximum(self.spb10.value())
        self.spb9.setMaximum(self.spb10.value())

    @QtCore.pyqtSignature("int")
    def on_spb11_valueChanged(self):
        self.sld6.setMinimum(self.spb11.value())
        self.spb12.setMinimum(self.spb11.value())

    @QtCore.pyqtSignature("int")
    def on_spb12_valueChanged(self):
        self.sld6.setMaximum(self.spb12.value())
        self.spb11.setMaximum(self.spb12.value())

    @QtCore.pyqtSignature("int")
    def on_spb13_valueChanged(self):
        self.sld7.setMinimum(self.spb13.value())
        self.spb14.setMinimum(self.spb13.value())

    @QtCore.pyqtSignature("int")
    def on_spb14_valueChanged(self):
        self.sld7.setMaximum(self.spb14.value())
        self.spb13.setMaximum(self.spb14.value())


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = Dialog6()
    dialog.show()
    sys.exit(app.exec_())