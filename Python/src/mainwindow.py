# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow , QVBoxLayout, QWidget
from PyQt5.Qt import pyqtSlot
# Project modules
from src.ui.mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker

from numpy import *
from time import *
from random import *
from scipy import signal


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.ErrorLabel.hide()
        #System input
        self.SystemOrder.currentIndexChanged.connect(self.changeSystemFrame)
        self.FirstOrderWidget.show()
        self.SecondOrderWidget.hide()
        self.SupOrderWidget.hide()
        self.FirstOrderFilters.show()
        self.SecondOrderFilters.hide()
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
        self.PZAxes.spines['left'].set_position('zero')
        self.PZAxes.spines['bottom'].set_position('zero')
        self.PZAxes.spines['right'].set_visible(False)
        self.PZAxes.spines['top'].set_visible(False)
        self.PZLayout.addWidget(self.PZCanvas)

        self.UpdateBotton.clicked.connect(self.plotGraphics)


    def plotGraphics(self):

        InputTypeIndex = self.InputType.currentIndex()          #0: senoide, 1: Escalon, 2: Pulso periodico, 3: Triangular
        SystemOrderIndex = self.SystemOrder.currentIndex()      #0: order 1, 1: Orden Dos, 3: orden superior

        self.GainAxes.clear()
        self.PhaseAxes.clear()
        self.PZAxes.clear()
        self.PhaseAxes.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}°'))

        if SystemOrderIndex == 0:
            self.firstOrder()
        elif SystemOrderIndex == 1:
            self.secondOrder()
        elif SystemOrderIndex == 2:
            self.supOrder()

    def firstOrder(self):

        filterType = self.FirstOrderFilters.currentIndex()      #0: pasa bajos, 1: pasa altos, 2: pasa todo
        gain = self.GainInput.text()
        frecuency = self.FrecuencyInput.text()

        if gain and frecuency:
            self.ErrorLabel.hide()

            gain = float(self.GainInput.text())
            frecuency = float(self.FrecuencyInput.text())
            #pasa bajos
            if filterType == 0:
                num = [gain]
                den = [(1/frecuency), 1]
            #pasa altos
            if filterType == 1:
                num = [gain, 0]
                den = [(1/frecuency), 1]
            #pasa todo
            if filterType == 2:
                num = [gain/frecuency, -gain]
                den = [(1/frecuency), 1]
        
            system = signal.TransferFunction(num, den)
            w, mag, phase = signal.bode(system)
            self.GainAxes.semilogx(w, mag, color = 'blue')
            self.PhaseAxes.semilogx(w, phase, color = 'red')
            self.GainCanvas.draw()
            self.PhaseCanvas.draw()

            if system.zeros:
                self.PZAxes.scatter(system.zeros[0], 0, color='blue', marker='o', s=100)
            if system.poles:
                self.PZAxes.scatter(system.poles[0], 0, color='red', marker='x', s=100)
            
            self.PZCanvas.draw()
        
        else:

            self.ErrorLabel.show()

    def secondOrder(self):

        filterType = self.SecondOrderFilters.currentIndex()      #0: pasa bajos, 1: pasa altos, 2: pasa todo, 3: pasa banda, 4: notch
        gain = self.GainInput.text()
        omega = self.OmegaInput.text()
        xsi = self.XsiInput.text()
        
        if gain and omega and xsi:
            self.ErrorLabel.hide()

            gain = float(self.GainInput.text())
            omega = float(self.OmegaInput.text())
            xsi = float(self.XsiInput.text())
            #pasa bajos
            if filterType == 0:
                num = [gain]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
            #pasa altos
            if filterType == 1:
                num = [gain, 0, 0]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
            #pasa todo
            if filterType == 2:
                num = [(gain/pow(omega, 2)), -gain*2*xsi/omega, gain]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
            #pasa banda
            if filterType == 1:
                num = [gain, 0]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
            #Notch
            if filterType == 2:
                num = [(gain/pow(omega, 2)), 0, gain]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
        
            system = signal.TransferFunction(num, den)
            w, mag, phase = signal.bode(system)
            self.GainAxes.semilogx(w, mag)
            self.PhaseAxes.semilogx(w, phase)
            self.GainCanvas.draw()
            self.PhaseCanvas.draw()
        
        else:
            self.ErrorLabel.show()

    def supOrder(self):

        gain = self.GainInput.text()
        numerador = self.NumeratorInput.text()
        denominador = self.DenominatorInput.text()
        
        if gain and numerador and denominador:
            self.ErrorLabel.hide()

            gain = float(self.GainInput.text())
            num = numerador.split()
            num = [float(numero) * gain for numero in num]
            den = denominador.split()
            den = [float(numero) for numero in den]
        
            system = signal.TransferFunction(num, den)
            w, mag, phase = signal.bode(system)
            self.GainAxes.semilogx(w, mag)
            self.PhaseAxes.semilogx(w, phase)
            self.GainCanvas.draw()
            self.PhaseCanvas.draw()
        
        else:
            self.ErrorLabel.show()

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
        
            

