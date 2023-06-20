# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1114, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1114, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.SystemFrame = QtWidgets.QFrame(self.centralwidget)
        self.SystemFrame.setGeometry(QtCore.QRect(20, 10, 521, 220))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SystemFrame.sizePolicy().hasHeightForWidth())
        self.SystemFrame.setSizePolicy(sizePolicy)
        self.SystemFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.SystemFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SystemFrame.setLineWidth(3)
        self.SystemFrame.setObjectName("SystemFrame")
        self.label = QtWidgets.QLabel(self.SystemFrame)
        self.label.setGeometry(QtCore.QRect(0, 0, 520, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.SystemOrder = QtWidgets.QComboBox(self.SystemFrame)
        self.SystemOrder.setEnabled(True)
        self.SystemOrder.setGeometry(QtCore.QRect(30, 70, 175, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SystemOrder.setFont(font)
        self.SystemOrder.setObjectName("SystemOrder")
        self.SystemOrder.addItem("")
        self.SystemOrder.addItem("")
        self.SystemOrder.addItem("")
        self.FirstOrderFilters = QtWidgets.QComboBox(self.SystemFrame)
        self.FirstOrderFilters.setGeometry(QtCore.QRect(30, 120, 175, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FirstOrderFilters.setFont(font)
        self.FirstOrderFilters.setObjectName("FirstOrderFilters")
        self.FirstOrderFilters.addItem("")
        self.FirstOrderFilters.addItem("")
        self.FirstOrderFilters.addItem("")
        self.SecondOrderFilters = QtWidgets.QComboBox(self.SystemFrame)
        self.SecondOrderFilters.setGeometry(QtCore.QRect(30, 120, 175, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.SecondOrderFilters.setFont(font)
        self.SecondOrderFilters.setObjectName("SecondOrderFilters")
        self.SecondOrderFilters.addItem("")
        self.SecondOrderFilters.addItem("")
        self.SecondOrderFilters.addItem("")
        self.SecondOrderFilters.addItem("")
        self.SecondOrderFilters.addItem("")
        self.FirstOrderWidget = QtWidgets.QWidget(self.SystemFrame)
        self.FirstOrderWidget.setGeometry(QtCore.QRect(210, 100, 291, 111))
        self.FirstOrderWidget.setAutoFillBackground(False)
        self.FirstOrderWidget.setObjectName("FirstOrderWidget")
        self.FrecuencyLabel = QtWidgets.QLabel(self.FirstOrderWidget)
        self.FrecuencyLabel.setGeometry(QtCore.QRect(20, 20, 108, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.FrecuencyLabel.setFont(font)
        self.FrecuencyLabel.setTextFormat(QtCore.Qt.AutoText)
        self.FrecuencyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FrecuencyLabel.setObjectName("FrecuencyLabel")
        self.FrecuencyInput = QtWidgets.QLineEdit(self.FirstOrderWidget)
        self.FrecuencyInput.setGeometry(QtCore.QRect(140, 20, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.FrecuencyInput.setFont(font)
        self.FrecuencyInput.setObjectName("FrecuencyInput")
        self.SecondOrderWidget = QtWidgets.QWidget(self.SystemFrame)
        self.SecondOrderWidget.setGeometry(QtCore.QRect(210, 100, 291, 111))
        self.SecondOrderWidget.setAutoFillBackground(False)
        self.SecondOrderWidget.setObjectName("SecondOrderWidget")
        self.OmegaLabel = QtWidgets.QLabel(self.SecondOrderWidget)
        self.OmegaLabel.setGeometry(QtCore.QRect(20, 11, 108, 32))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(12)
        self.OmegaLabel.setFont(font)
        self.OmegaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OmegaLabel.setObjectName("OmegaLabel")
        self.OmegaInput = QtWidgets.QLineEdit(self.SecondOrderWidget)
        self.OmegaInput.setGeometry(QtCore.QRect(140, 20, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.OmegaInput.setFont(font)
        self.OmegaInput.setObjectName("OmegaInput")
        self.XsiLabel = QtWidgets.QLabel(self.SecondOrderWidget)
        self.XsiLabel.setGeometry(QtCore.QRect(20, 65, 108, 32))
        font = QtGui.QFont()
        font.setFamily("Symbol")
        font.setPointSize(12)
        self.XsiLabel.setFont(font)
        self.XsiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.XsiLabel.setObjectName("XsiLabel")
        self.XsiInput = QtWidgets.QLineEdit(self.SecondOrderWidget)
        self.XsiInput.setGeometry(QtCore.QRect(140, 65, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.XsiInput.setFont(font)
        self.XsiInput.setObjectName("XsiInput")
        self.SupOrderWidget = QtWidgets.QWidget(self.SystemFrame)
        self.SupOrderWidget.setGeometry(QtCore.QRect(210, 100, 291, 111))
        self.SupOrderWidget.setAutoFillBackground(False)
        self.SupOrderWidget.setObjectName("SupOrderWidget")
        self.NumeratorLabel = QtWidgets.QLabel(self.SupOrderWidget)
        self.NumeratorLabel.setGeometry(QtCore.QRect(20, 20, 108, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NumeratorLabel.setFont(font)
        self.NumeratorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NumeratorLabel.setObjectName("NumeratorLabel")
        self.NumeratorInput = QtWidgets.QLineEdit(self.SupOrderWidget)
        self.NumeratorInput.setGeometry(QtCore.QRect(140, 20, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NumeratorInput.setFont(font)
        self.NumeratorInput.setObjectName("NumeratorInput")
        self.DenominatorLabel = QtWidgets.QLabel(self.SupOrderWidget)
        self.DenominatorLabel.setGeometry(QtCore.QRect(3, 62, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DenominatorLabel.setFont(font)
        self.DenominatorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DenominatorLabel.setObjectName("DenominatorLabel")
        self.DenominatorInput = QtWidgets.QLineEdit(self.SupOrderWidget)
        self.DenominatorInput.setGeometry(QtCore.QRect(140, 65, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DenominatorInput.setFont(font)
        self.DenominatorInput.setObjectName("DenominatorInput")
        self.GainLabel = QtWidgets.QLabel(self.SystemFrame)
        self.GainLabel.setGeometry(QtCore.QRect(220, 70, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GainLabel.setFont(font)
        self.GainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GainLabel.setObjectName("GainLabel")
        self.GainInput = QtWidgets.QLineEdit(self.SystemFrame)
        self.GainInput.setGeometry(QtCore.QRect(350, 70, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GainInput.setFont(font)
        self.GainInput.setObjectName("GainInput")
        self.SecondOrderFilters.raise_()
        self.label.raise_()
        self.SystemOrder.raise_()
        self.FirstOrderWidget.raise_()
        self.SecondOrderWidget.raise_()
        self.SupOrderWidget.raise_()
        self.GainLabel.raise_()
        self.GainInput.raise_()
        self.FirstOrderFilters.raise_()
        self.InputFrame = QtWidgets.QFrame(self.centralwidget)
        self.InputFrame.setGeometry(QtCore.QRect(570, 10, 521, 220))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputFrame.sizePolicy().hasHeightForWidth())
        self.InputFrame.setSizePolicy(sizePolicy)
        self.InputFrame.setBaseSize(QtCore.QSize(520, 220))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.InputFrame.setFont(font)
        self.InputFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.InputFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InputFrame.setLineWidth(3)
        self.InputFrame.setObjectName("InputFrame")
        self.label_2 = QtWidgets.QLabel(self.InputFrame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 520, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.InputType = QtWidgets.QComboBox(self.InputFrame)
        self.InputType.setGeometry(QtCore.QRect(30, 70, 175, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputType.sizePolicy().hasHeightForWidth())
        self.InputType.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InputType.setFont(font)
        self.InputType.setObjectName("InputType")
        self.InputType.addItem("")
        self.InputType.addItem("")
        self.InputType.addItem("")
        self.InputType.addItem("")
        self.AmpLabel = QtWidgets.QLabel(self.InputFrame)
        self.AmpLabel.setGeometry(QtCore.QRect(220, 70, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AmpLabel.setFont(font)
        self.AmpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AmpLabel.setObjectName("AmpLabel")
        self.AmpInput = QtWidgets.QLineEdit(self.InputFrame)
        self.AmpInput.setGeometry(QtCore.QRect(350, 70, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AmpInput.setFont(font)
        self.AmpInput.setObjectName("AmpInput")
        self.EntryFrecInput = QtWidgets.QLineEdit(self.InputFrame)
        self.EntryFrecInput.setGeometry(QtCore.QRect(350, 120, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.EntryFrecInput.setFont(font)
        self.EntryFrecInput.setObjectName("EntryFrecInput")
        self.EntryFrecLabel = QtWidgets.QLabel(self.InputFrame)
        self.EntryFrecLabel.setGeometry(QtCore.QRect(230, 120, 108, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EntryFrecLabel.setFont(font)
        self.EntryFrecLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EntryFrecLabel.setObjectName("EntryFrecLabel")
        self.PhaseLabel = QtWidgets.QLabel(self.InputFrame)
        self.PhaseLabel.setGeometry(QtCore.QRect(210, 170, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PhaseLabel.setFont(font)
        self.PhaseLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PhaseLabel.setObjectName("PhaseLabel")
        self.Phase_DutyCycleInput = QtWidgets.QLineEdit(self.InputFrame)
        self.Phase_DutyCycleInput.setGeometry(QtCore.QRect(350, 170, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Phase_DutyCycleInput.setFont(font)
        self.Phase_DutyCycleInput.setObjectName("Phase_DutyCycleInput")
        self.DutyCycleLabel = QtWidgets.QLabel(self.InputFrame)
        self.DutyCycleLabel.setGeometry(QtCore.QRect(215, 170, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DutyCycleLabel.setFont(font)
        self.DutyCycleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DutyCycleLabel.setObjectName("DutyCycleLabel")
        self.GraphicsFrame = QtWidgets.QFrame(self.centralwidget)
        self.GraphicsFrame.setGeometry(QtCore.QRect(20, 250, 1071, 581))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GraphicsFrame.sizePolicy().hasHeightForWidth())
        self.GraphicsFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GraphicsFrame.setFont(font)
        self.GraphicsFrame.setMouseTracking(False)
        self.GraphicsFrame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.GraphicsFrame.setToolTipDuration(-1)
        self.GraphicsFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.GraphicsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.GraphicsFrame.setLineWidth(3)
        self.GraphicsFrame.setObjectName("GraphicsFrame")
        self.tabWidget = QtWidgets.QTabWidget(self.GraphicsFrame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1051, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.BodeTab = QtWidgets.QWidget()
        self.BodeTab.setObjectName("BodeTab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.BodeTab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1041, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.BodeLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.BodeLayout.setContentsMargins(0, 0, 0, 0)
        self.BodeLayout.setSpacing(0)
        self.BodeLayout.setObjectName("BodeLayout")
        self.tabWidget.addTab(self.BodeTab, "")
        self.IOTab = QtWidgets.QWidget()
        self.IOTab.setObjectName("IOTab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.IOTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1041, 441))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.IOLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.IOLayout.setContentsMargins(0, 0, 0, 0)
        self.IOLayout.setSpacing(0)
        self.IOLayout.setObjectName("IOLayout")
        self.tabWidget.addTab(self.IOTab, "")
        self.PZTab = QtWidgets.QWidget()
        self.PZTab.setObjectName("PZTab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.PZTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1041, 441))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.PZLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.PZLayout.setContentsMargins(0, 0, 0, 0)
        self.PZLayout.setObjectName("PZLayout")
        self.tabWidget.addTab(self.PZTab, "")
        self.UpdateBotton = QtWidgets.QPushButton(self.GraphicsFrame)
        self.UpdateBotton.setGeometry(QtCore.QRect(860, 520, 181, 41))
        self.UpdateBotton.setToolTipDuration(1)
        self.UpdateBotton.setObjectName("UpdateBotton")
        self.ErrorLabel = QtWidgets.QLabel(self.GraphicsFrame)
        self.ErrorLabel.setGeometry(QtCore.QRect(10, 520, 841, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ErrorLabel.setFont(font)
        self.ErrorLabel.setObjectName("ErrorLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Configuración del Sistema"))
        self.SystemOrder.setItemText(0, _translate("MainWindow", "Primer Orden"))
        self.SystemOrder.setItemText(1, _translate("MainWindow", "Segundo Orden"))
        self.SystemOrder.setItemText(2, _translate("MainWindow", "Orden Superior"))
        self.FirstOrderFilters.setItemText(0, _translate("MainWindow", "Paso Bajo"))
        self.FirstOrderFilters.setItemText(1, _translate("MainWindow", "Paso Alto"))
        self.FirstOrderFilters.setItemText(2, _translate("MainWindow", "Pasa Todo"))
        self.SecondOrderFilters.setItemText(0, _translate("MainWindow", "Pasa Bajo"))
        self.SecondOrderFilters.setItemText(1, _translate("MainWindow", "Pasa Alto"))
        self.SecondOrderFilters.setItemText(2, _translate("MainWindow", "Pasa Todo"))
        self.SecondOrderFilters.setItemText(3, _translate("MainWindow", "Pasa Banda"))
        self.SecondOrderFilters.setItemText(4, _translate("MainWindow", "Notch"))
        self.FrecuencyLabel.setText(_translate("MainWindow", "Frecuencia"))
        self.OmegaLabel.setText(_translate("MainWindow", "w"))
        self.XsiLabel.setText(_translate("MainWindow", "x"))
        self.NumeratorLabel.setText(_translate("MainWindow", "Numerador"))
        self.DenominatorLabel.setText(_translate("MainWindow", "Denominador"))
        self.GainLabel.setText(_translate("MainWindow", "Ganancia"))
        self.label_2.setText(_translate("MainWindow", "Configuración de la Entrada"))
        self.InputType.setItemText(0, _translate("MainWindow", "Senoide"))
        self.InputType.setItemText(1, _translate("MainWindow", "Escalón"))
        self.InputType.setItemText(2, _translate("MainWindow", "Pulso periódico"))
        self.InputType.setItemText(3, _translate("MainWindow", "Triangular"))
        self.AmpLabel.setText(_translate("MainWindow", "Amplitud"))
        self.EntryFrecLabel.setText(_translate("MainWindow", "Frecuencia"))
        self.PhaseLabel.setText(_translate("MainWindow", "Fase"))
        self.DutyCycleLabel.setText(_translate("MainWindow", "Duty Cycle"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BodeTab), _translate("MainWindow", "Bode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IOTab), _translate("MainWindow", "Entrada y Respuesta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PZTab), _translate("MainWindow", "Polos y ceros"))
        self.UpdateBotton.setText(_translate("MainWindow", "Actualizar"))
        self.ErrorLabel.setText(_translate("MainWindow", "Faltan Datos!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
