# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow , QVBoxLayout, QWidget
from PyQt5.Qt import pyqtSlot
# Project modules
from src.ui.mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker

import numpy as np
from time import *
from random import *
from scipy import signal
import matplotlib.image as mpimg


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

        self.UpdateBotton.clicked.connect(self.plotGraphics)
                 
    def plotGraphics(self):

        SystemOrderIndex = self.SystemOrder.currentIndex()      #0: order 1, 1: Orden Dos, 3: orden superior

        self.GainAxes.clear()
        self.PhaseAxes.clear()
        self.PZAxes.clear()
        self.InputAxes.clear()
        self.OutputAxes.clear()
        
        self.PZAxes.spines['left'].set_position('zero')
        self.PZAxes.spines['bottom'].set_position('zero')
        self.PZAxes.spines['left'].set_visible(False)
        self.PZAxes.spines['bottom'].set_visible(False)
        self.PZAxes.spines['right'].set_visible(False)
        self.PZAxes.spines['top'].set_visible(False)
        self.PZLayout.addWidget(self.PZCanvas)
        
        self.PhaseAxes.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.0f}°'))

        self.systemParameters = []
        if SystemOrderIndex == 0:
            self.firstOrder(self.systemParameters)
        elif SystemOrderIndex == 1:
            self.secondOrder(self.systemParameters)
        elif SystemOrderIndex == 2:
            self.supOrder(self.systemParameters)

        if len(self.systemParameters):
            system = signal.TransferFunction(self.systemParameters[0], self.systemParameters[1])
            
        #-----------------Bode----------------------------
            w, mag, phase = signal.bode(system)
            phase = np.round(phase, decimals=6)
            self.GainAxes.semilogx(w, mag, color = 'blue')
            self.PhaseAxes.semilogx(w, phase, color = 'red')
            self.GainAxes.grid()
            self.PhaseAxes.grid()
            self.GainCanvas.draw()
            self.PhaseCanvas.draw()
        #-------------------------------------------------

        #-----------------Polos y Ceros-------------------
            poles_real = system.poles.real
            poles_imag = system.poles.imag
            zeros_real = system.zeros.real
            zeros_imag = system.zeros.imag
            polesRealMod = [np.abs(pole) for pole in poles_real]
            zerosRealMod = [np.abs(zero) for zero in zeros_real]
            polesImagMod = [np.abs(pole) for pole in poles_imag]
            zerosimagMod = [np.abs(zero) for zero in zeros_imag]
            xLimMax = 0
            yLimMax = 0

        #SUS_PNG = mpimg.imread('resources\\SUS.png')
        
            if len(system.zeros):
                for i in range(len(zeros_real)):
                    self.PZAxes.scatter(zeros_real[i], zeros_imag[i], color='blue', marker='o', s=100)
                xLimMax = max(polesRealMod)*1.5 + 10 if max(polesRealMod) >= max(zerosRealMod) else max(zerosRealMod)*1.5 + 10
                yLimMax = max(polesImagMod)*1.5 + 10 if max(polesImagMod) >= max(zerosimagMod) else max(zerosimagMod)*1.5 + 10
            else:
                xLimMax = max(polesRealMod)*1.5 + 10
                yLimMax = max(polesImagMod)*1.5 + 10

            for i in range(len(poles_real)):
                self.PZAxes.scatter(poles_real[i], poles_imag[i], color='red', marker='x', s=100)

            self.PZAxes.annotate("", xy=(-xLimMax, 0), xytext=(xLimMax, 0), arrowprops=dict(arrowstyle='<-')) # Eje x
            self.PZAxes.annotate(r"$\sigma$", xy=(xLimMax,0), xytext=(1, 5),textcoords='offset points', ha='center', fontsize = 13)
            self.PZAxes.annotate("", xy=(0, -yLimMax), xytext=(0, yLimMax), arrowprops=dict(arrowstyle='<-')) # Eje y
            self.PZAxes.annotate(r"$j \omega$", xy=(0,yLimMax), xytext=(8, 1),textcoords='offset points', ha='center', fontsize = 13)
            
            self.PZAxes.set_xlim(-xLimMax, xLimMax)
            self.PZAxes.set_ylim(-yLimMax, yLimMax)
            self.PZAxes.grid()
            
            # Saca el 0 del grafico
            yticks = self.PZAxes.get_yticks()
            xticks = self.PZAxes.get_xticks()
            # Número que deseas eliminar
            numero_a_borrar = 0
            # Filtrar las marcas del eje para eliminar el número específico
            nuevas_yticks = [tick for tick in yticks if tick != numero_a_borrar]
            nuevas_xticks = [tick for tick in yticks if tick != numero_a_borrar]
            # Establecer las nuevas marcas del eje
            self.PZAxes.set_yticks(nuevas_yticks)
            self.PZAxes.set_xticks(nuevas_xticks)
            
            self.PZCanvas.draw()
        #--------------------------------------------------

        #-------------Entrada y Salida---------------------

            inputType = self.InputType.currentIndex()

            self.tin = []
            self.yin = []
            if( inputType == 0):
                
                self.senoidEntry()
        
            if( inputType == 1):
                
                self.pulseEntry()

            if( inputType == 2):
                
                self.pwmEntry()
                
            if( inputType == 3):
                
                self.triangularEntry()

            if len(self.tin) and len(self.yin):
                tout, yout, xout = signal.lsim(system, U=self.yin, T=self.tin)

                self.InputAxes.plot(self.tin, self.yin, color='red')
                self.InputAxes.grid()
                self.InputCanvas.draw()

                self.OutputAxes.plot(tout, yout, color='blue')
                self.OutputAxes.grid()
                self.OutputCanvas.draw()

        #--------------------------------------------------

    def senoidEntry(self):

        # Senoidal
        ampli = self.AmpInput.text()
        frecuency = self.EntryFrecInput.text()
        phase_duty = self.Phase_DutyCicleInput.text()

        # Senoidal
        # Señal senoidal
        if ampli and frecuency and phase_duty:
            self.ErrorLabel.hide()
            ampli = float(ampli)
            frecuency = float(frecuency)
            phase_duty = float(phase_duty)
            T = 1.0 / frecuency  # Período de la señal senoidal
            num_periods = 6  # Número de períodos que deseas generar
            num_samples_per_period = 200  # Número de muestras por período

            num_samples = num_periods * num_samples_per_period
            self.tin = np.linspace(0, num_periods * T, num_samples, endpoint=False)
            self.yin = ampli * np.sin(2 * np.pi * frecuency * self.tin + phase_duty*np.pi/180)
        
        else:
            self.ErrorLabel.show()
            self.ErrorLabel.setText("Faltan Datos!")

    def pulseEntry(self):

        ampli = self.AmpInput.text()

        if ampli:
            self.ErrorLabel.hide()
            ampli = float(ampli)
            # Escalón
            T = 1  # Duración del escalón
            num_samples = 1000  # Número de muestras

            self.tin = np.linspace(0, T, num_samples, endpoint=False)
            self.yin = np.repeat(ampli, num_samples)
            self.yin[0] = 0
        
        else:
            
            self.ErrorLabel.show()
            self.ErrorLabel.setText("Faltan Datos!")

    def pwmEntry(self):

        ampli = self.AmpInput.text()
        frecuency = self.EntryFrecInput.text()
        duty_cycle = self.Phase_DutyCicleInput.text()

        if ampli and frecuency and duty_cycle:
            self.ErrorLabel.hide()
            ampli = float(ampli)
            frecuency = float(frecuency)
            duty_cycle = float(duty_cycle)
            if duty_cycle >= 1:
                self.ErrorLabel.show()
                self.ErrorLabel.setText("Ingrese un Duty Cycle menor a 1")
            else:
                self.ErrorLabel.hide()
                # Señal cuadrada PWM
                T = 1 / frecuency  # Período de la señal cuadrada PWM
                num_periods = 6  # Número de períodos que deseas generar
                num_samples_per_period = 200  # Número de muestras por período

                num_samples = num_periods * num_samples_per_period
                self.tin = np.linspace(0, num_periods * T, num_samples, endpoint=False)

                self.yin = ampli * signal.square(2 * np.pi * frecuency * self.tin, duty=duty_cycle)  
        
        else:
            
            self.ErrorLabel.show()
            self.ErrorLabel.setText("Faltan Datos!")

    def triangularEntry(self):

        ampli = self.AmpInput.text()
        frecuency = self.EntryFrecInput.text()
        duty_cycle = self.Phase_DutyCicleInput.text()

        if ampli and frecuency and duty_cycle:
            self.ErrorLabel.hide()
            #Triangular
            ampli = float(self.AmpInput.text())
            frecuency = float(self.EntryFrecInput.text())
            duty_cycle = float(duty_cycle)
            if duty_cycle >= 1:
                self.ErrorLabel.show()
                self.ErrorLabel.setText("Ingrese un Duty Cycle menor a 1")
            else:
                self.ErrorLabel.hide()
                # Señal triangular
                T = 1.0 / frecuency  # Período de la señal triangular
                num_periods = 6  # Número de períodos que deseas generar
                num_samples_per_period = 200  # Número de muestras por período

                num_samples = num_periods * num_samples_per_period
                self.tin = np.linspace(0, num_periods * T, num_samples, endpoint=False)

                self.yin = ampli * signal.sawtooth(2 * np.pi * frecuency * self.tin, width=duty_cycle)
        
        else:
            
            self.ErrorLabel.show()
            self.ErrorLabel.setText("Faltan Datos!")

    def firstOrder(self, systemParameters):

        filterType = self.FirstOrderFilters.currentIndex()      #0: pasa bajos, 1: pasa altos, 2: pasa todo
        gain = self.GainInput.text()
        frecuency = self.FrecuencyInput.text()

        if gain and frecuency:
            self.ErrorLabel.hide()

            gain = float(self.GainInput.text())
            frecuency = float(self.FrecuencyInput.text())
            k = pow(10, gain/20)
            #pasa bajos
            if filterType == 0:
                num = [k]
                den = [(1/frecuency), 1]
            #pasa altos
            if filterType == 1:
                num = [k / frecuency, 0]
                den = [(1/frecuency), 1]
            #pasa todo
            if filterType == 2:
                num = [k/frecuency, -k]
                den = [(1/frecuency), 1]

            systemParameters.append(num)
            systemParameters.append(den)
                    
        else:

            self.ErrorLabel.show()
            self.ErrorLabel.setText("Faltan Datos!")

    def secondOrder(self, systemParameters):

        filterType = self.SecondOrderFilters.currentIndex()      #0: pasa bajos, 1: pasa altos, 2: pasa todo, 3: pasa banda, 4: notch
        gain = self.GainInput.text()
        omega = self.OmegaInput.text()
        xsi = self.XsiInput.text()
        
        if gain and omega and xsi:
            self.ErrorLabel.hide()

            gain = float(self.GainInput.text())
            omega = float(self.OmegaInput.text())
            xsi = float(self.XsiInput.text())
            k = pow(10, gain/20)
            #pasa bajos
            if filterType == 0:
                num = [k]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
            #pasa altos
            if filterType == 1:
                num = [k / pow(omega, 2), 0, 0]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
            #pasa todo
            if filterType == 2:
                num = [(k/pow(omega, 2)), -k*2*xsi/omega, k]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
            #pasa banda
            if filterType == 3:
                num = [k * 2*xsi / omega, 0]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
            #Notch
            if filterType == 4:
                num = [(k/pow(omega, 2)), 0, k]
                den = [(1/pow(omega, 2)), 2*xsi/omega, 1]
        
            systemParameters.append(num)
            systemParameters.append(den)
        
        else:
            self.ErrorLabel.show()
            self.ErrorLabel.setText("Faltan Datos!")

    def supOrder(self, systemParameters):

        gain = self.GainInput.text()
        numerador = self.NumeratorInput.text()
        denominador = self.DenominatorInput.text()
        
        if gain and numerador and denominador:
            self.ErrorLabel.hide()
            
            gain = float(self.GainInput.text())
            k = pow(10, gain/20)
            num = numerador.split()
            num = [float(numero) * k for numero in num]
            den = denominador.split()
            den = [float(numero) for numero in den]
            if len(den) == 1:
                self.ErrorLabel.show()
                self.ErrorLabel.setText("Denominador incorrecto")
            elif len(num) > len(den):
                self.ErrorLabel.show()
                self.ErrorLabel.setText("Sistema inestable")
            else:
                systemParameters.append(num)
                systemParameters.append(den)
        
        else:
            self.ErrorLabel.show()
            self.ErrorLabel.setText("Faltan Datos!")

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
        
            

