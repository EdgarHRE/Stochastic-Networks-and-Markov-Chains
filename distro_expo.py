
# Librerias

from math import exp
from lib_random.variable_aleatorias import *
from lib_random.distributions import *
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as static
import numpy as np 


#"""

# Ingresa el numero de variables aleatorias.
elements = int(input('Ingrese el valor de n elementos en la lista: '))

# Ingresa el valor de lambda que se usara en la distribucion exponencial.
lmbd = float(input('Ingrese el valor de lambda: ')) 

#Variable list_nums crea n numeros pseudo aleatorios -> 100000 
list_nums = Random_Var.Method_1(elements) #parametros -> (int)

#Variable expo_nega crea una lista con n valores de la funcion Expo_Negative()
expo_nega = Distributions.Expo_Negative(lmbd, list_nums) # parametros -> (float,list)
    

# Lee la lista expo_nega.txt para sumar todos los valores obtenidos en la variable expo_nega

with open('expo_nega.txt', 'w') as salida:
    
    for linea in expo_nega:
        salida.write(str(linea))
        salida.write('\n')
    
    media = static.mean(expo_nega) # Calcula la media de todos los valores obtenidos
    var = static.variance(expo_nega) # Calcula la varianza todos los valores obtenidos
    cov = (math.sqrt(var))/media # Calcula el coficiente de variacion de los valores obtenidos

    print(f'La media es: {media}, La varianza es: {var}, La covarianza es: {cov}')


# Obtencion de un Histograma y grafica de la pdf.

intervalos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # Bins del histograma

fig, ax1 = plt.subplots() 

# Desarrollo del histograma
ax1.hist(expo_nega, bins = intervalos, color = 'blue', ec = 'black') 

# Labels del eje x & y del Histograma
ax1.set_xlabel('fx(x)')
ax1.set_ylabel('Número total de valores', color='blue')


# Crear un segundo eje y (para la gráfica de puntos)
ax2 = ax1.twinx()

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [0.65, 0.33, 0.17, 0.09, 0.04, 0.02, 0.01, 0.007, 0.003]

# Dibujar la gráfica de puntos en el segundo eje y
ax2.scatter(x, y, label='pdf', color='red', marker='o')
ax2.plot(x, y, color='red')
ax2.set_ylim(0, 1)
ax2.set_ylabel('y', color='black')


# Añadir una leyenda
ax2.legend(loc='upper right')

plt.show()
