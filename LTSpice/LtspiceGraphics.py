import ltspice
import numpy as np
import matplotlib.pyplot as plt
import os

#------------Load the signals from the .raw file
ruta_actual = os.path.realpath(__file__)
ruta_carpeta = os.path.dirname(ruta_actual)
raw_file = ruta_carpeta + '\\Montecarlo_Completo\\Simulacion_SPICE_Montecarlo_Completo.raw'
l = ltspice.Ltspice(raw_file) 
# Make sure that the .raw file is located in the correct path
l.parse()
#-----------------------------------------------

#Parameters for the circuit
Fs = 2.5
Ts = 1/Fs

time = l.get_time() * 1E+3
Vl = l.get_data('V(vl+)') - l.get_data('V(vl-)')
V_l_max = []
V_l_min = []

for i in range(l.case_count): # Iteration in simulation cases 
    time = l.get_time(i) * 1E+3 
    # Case number starts from zero
    # Each case has different time point numbers
    V_l = l.get_data('V(vl+)',i) - l.get_data('V(vl-)', i) 
    V_l_max.append(max(V_l))
    V_l_min.append(min(V_l))
    #plt.plot(time, V_l)

#Histograma

mu = 3.8
sigma = 0.1
var = sigma**2
t = np.linspace(3.3, 4.3, 1000)
dist_normal = 60*sigma*np.exp(-(t-mu)**2/(2*sigma**2))

bins = 20
plt.plot(t, dist_normal)
plt.hist(V_l_max, bins, density=True)  

plt.show()


