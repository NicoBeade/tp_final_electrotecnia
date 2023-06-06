# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow , QVBoxLayout, QWidget
from PyQt5.Qt import pyqtSlot
# Project modules
from src.ui.mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from numpy import *
from time import *
from random import *


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #System input
        self.SystemOrder.currentIndexChanged.connect(self.changeSystemFrame)
        self.FirstOrderWidget.show()
        self.SecondOrderWidget.hide()
        self.SupOrderWidget.hide()
        #Entry input
        self.InputType.currentIndexChanged.connect(self.changeInputFrame)
        self.PhaseLabel.show()
        self.DutyCicleLabel.hide()
        #Graphics

        #Grafico de ganancia
        self.GainBode = Figure()
        self.GainCanvas = FigureCanvas(self.GainBode)
        self.GainAxes = self.GainBode.add_subplot()
        self.BodeLayout.addWidget(self.GainCanvas)
        #Grafico de fase
        self.PhaseBode = Figure()
        self.PhaseCanvas = FigureCanvas(self.PhaseBode)
        self.PhaseAxes = self.PhaseBode.add_subplot()
        self.BodeLayout.addWidget(self.PhaseCanvas)
        #Grafico de Entrada
        self.InputFigure = Figure()
        self.InputCanvas = FigureCanvas(self.InputFigure)
        self.InputAxes = self.InputFigure.add_subplot()
        self.IOLayout.addWidget(self.InputCanvas)
        #Grafico de Salida
        self.OutputFigure = Figure()
        self.OutputCanvas = FigureCanvas(self.OutputFigure)
        self.OutputAxes = self.OutputFigure.add_subplot()
        self.IOLayout.addWidget(self.OutputCanvas)
        #Grafico de Polos y Ceros
        self.PZFigure = Figure()
        self.PZCanvas = FigureCanvas(self.PZFigure)
        self.PZAxes = self.PZFigure.add_subplot()
        self.PZLayout.addWidget(self.PZCanvas)

        self.UpdateBotton.clicked.connect(self.plotGraphics)


    def plotGraphics(self):

        InputTypeIndex = self.InputType.currentIndex()          #0: senoide, 1: Escalon, 2: Pulso periodico, 3: Triangular
        SystemOrderIndex = self.SystemOrder.currentIndex()      #0: order 1, 1: Orden Dos, 3: orden superior
        
        print(SystemOrderIndex)
        print(InputTypeIndex)
        x_axis = linspace(0, 2 * pi, num=1000)
        y_axis = sin(x_axis * randint(1, 5))
        self.GainAxes.plot(x_axis, y_axis, label="Señal")
        self.PhaseAxes.plot(x_axis, y_axis, label="Señal2")
        self.GainCanvas.draw()
        self.PhaseCanvas.draw()

    def changeSystemFrame(self):
        order = self.SystemOrder.currentIndex()
        self.FirstOrderWidget.hide()
        self.FirstOrderFilters.hide()
        self.SecondOrderWidget.hide()
        self.SecondOrderFilters.hide()
        self.SupOrderWidget.hide()
        if( order == 0):
            self.FirstOrderWidget.show()
            self.FirstOrderFilters.show()
        elif( order == 1 ):
            self.SecondOrderWidget.show()
            self.SecondOrderFilters.show()
        elif( order == 2 ):
            self.SupOrderWidget.show()

    def changeInputFrame(self):
        order = self.InputType.currentIndex()
        if( order == 0):
            self.EntryFrecInput.show()
            self.EntryFrecLabel.show()
            self.Phase_DutyCicleInput.show()
            self.PhaseLabel.show()
            self.DutyCicleLabel.hide()
        if( order == 1):
            self.EntryFrecLabel.hide()
            self.EntryFrecInput.hide()
            self.Phase_DutyCicleInput.hide()
            self.PhaseLabel.hide()
            self.DutyCicleLabel.hide()
        if( order == 2 or order == 3):
            self.EntryFrecLabel.show()
            self.EntryFrecInput.show()
            self.Phase_DutyCicleInput.show()
            self.PhaseLabel.hide()
            self.DutyCicleLabel.show()
        
            

