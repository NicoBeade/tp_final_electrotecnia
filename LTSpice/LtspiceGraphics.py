import ltspice
import numpy as np
import matplotlib.pyplot as plt
import os

#------------Load the signals from the .raw file
ruta_actual = os.path.realpath(__file__)
ruta_carpeta = os.path.dirname(ruta_actual)
raw_file = ruta_carpeta + '\\Simulacion_con_valores_Fijos\\Simulacion_SPICE_Valores_Fijos.raw'
l = ltspice.Ltspice(raw_file) 
# Make sure that the .raw file is located in the correct path
l.parse()
#-----------------------------------------------

#Parameters for the circuit
Fs = 2.5
Ts = 1/Fs

