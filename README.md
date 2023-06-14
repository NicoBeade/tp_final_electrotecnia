# TP FINAL ELECTROTECNIA
22.02 Electrotecnia - Trabajo Practico Final - Python, LTSpice IV y Altium - 2023

## Descripción

El presente trabajo consiste de tres trabajos que ponen en práctica los conocimientos adquiridos en la materia Electrotecnia (22.02):

* Diseño de una GUI en Python para un simulador de filtros
* Simulación de un circuito en LTSpice RLC de segundo orden
* Diseño y desarrollo de una PCB utilizando un OPAMP TL082

## 1. Implementación de interfaz gráfica en Python

Se desarrolló una GUI en Python para simular filtros RLC de distintos órdenes. Permite al usuario elegir la excitación correspondiente al circuito.

### Funcionamiento y Funcionalidades

* El usuario ingresa los parámetros correspondientes al sistema, tales como órden, frecuencia de corte, ganancia, entre otros
* Luego ingresa los parámetros correspondientes a la entrada como tipo de señal, amplitud, frecuencia
* A partir de esta información se simula la respuesta en frecuencia del circuito, así como la salida correspondiente a la entrada seleccionada
* Se muestran gráficos de Bode de respuesta en frecuencia de amplitud y fase, y un diagrama de polos y ceros del circuito
* Se pueden visualizar la entrada y la salida en simultáneo graficadas en función del tiempo

### Guía de usuario

* Para ejecutar el programa acceder al .exe correspondiente
* Seleccioanr el orden del filtro: 1er orden, 2do orden, orden superior
* Seleccionar el tipo de filtro
* Dependiendo del tipo de filtro elegido, especificar los parámetros correspondientes
* Diseñar la entrada a partir de las opciones disponibles
* Una vez diseñado el filtro y la entrada, actualizar mediante el botón correspondiente


## 2. Simulación en LTSpice

Se simuló en LTSpice un circuito RLC de segundo orden en el que se analizaron las etapas de carga y descarga. Se monitoreó la tensión sobre el inductor y la corriente sobre el capacitor debido a que estas magnitudes podrían tomar sufrir sobrepicos que dañen a los componentes.

### Desarrollo

* Se compararon gráficos teóricos con simulados
* Se desarrollaron diagramas de Montecarlo para el análisis del efecto de variar ciertos componentes en las distintas salidas
* Se evaluó el escenario en el que las resistencias tomen valor 0

![PCB desarrollado](https://github.com/NicoBeade/tp_final_electrotecnia/blob/main/LTSpice_image.jpg?raw=true)

## 3. Diseño de PCB en Altium

Se diseñó una PCB utilizando un OPAMP TL082 desde Altium. Este circuito fue luego desarrollado para realizar mediciones sobre el mismo.

### Desarrollo

* Diseño del PCB en Altium
* Justificación de las conexiones elegidas
* Simulación del circuito diseñado
* Mediciones sobre el circuito desarrollado y desarrollo del mismo

![PCB desarrollado](https://github.com/NicoBeade/tp_final_electrotecnia/blob/main/PCB_image.jpeg?raw=true)

## Authors

* Nicolás Agustín Beade - 63109
* Facundo Ezequiel di Toro - 63390
* Nicolás Ezequiel Professi - 63431
* Estanislao Lopresto Ripa - 63400

### Link al informe

* [Link al Overleaf donde se desarrolló el informe](https://www.overleaf.com/project/64709fe400f98ba26137f169)

## Referencias

* No hubo
