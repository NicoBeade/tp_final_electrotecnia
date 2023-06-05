# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow

# Project modules
from src.ui.mainwindow import Ui_MainWindow


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
        if( order == 2 or order == 4):
            self.EntryFrecLabel.show()
            self.EntryFrecInput.show()
            self.Phase_DutyCicleInput.show()
            self.PhaseLabel.hide()
            self.DutyCicleLabel.show()
        
            

