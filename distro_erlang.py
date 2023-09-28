
#Librerias 

from math import exp 
from lib_random.variable_aleatorias import *
from lib_random.distributions import *
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as static
import numpy as np


# Ingresa el numero de variables aleatorias
elements = int(input('Ingresa el numero de n elementos en la lista: '))

# Ingresa el valor de lambda que se usara en la distribucion exponencial.
lmbd = float(input('Ingresa el valor de lambda: '))

# Variable list_nums crea n numeros pseudo aleatorios -> 100000 
list_nums = Random_Var.Method_1(elements) # parametros -> (int)

# Variable expo_nega crea una lista con n valores de la funcion Expo_Negative()
expo_nega = Distributions.Expo_Negative(lmbd, list_nums) # parametros -> (float,list)

# Variable erlang crea una lista con n valores de distribución erlang
erlang = Distributions.K_expo(expo_nega) # parametros -> (float,list)

# Lee la lista erlang.txt para sumar todos los valores obtenidos en la variable expo_nega

with open('erlang.txt', 'w') as salida:
    
    for linea in erlang:
        
        salida.write(str(linea))
        salida.write('\n')
       
    
    media = static.mean(erlang) # Calcula la media de todos los valores obtenidos
    var = static.variance(erlang) # Calcula la varianza todos los valores obtenidos
    cov = (math.sqrt(var)) / media # Calcula el coficiente de variacion de los valores obtenidos

    print(f'La media es: {media}, La varianza es: {var}, La covarianza es: {cov}')


# Obtencion de un Histograma y grafica de la pdf.

intervalos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # Bins del histograma

fig, ax1 = plt.subplots() 

# Desarrollo del histograma
ax1.hist(erlang, bins = intervalos, color = '#FFC1CC', ec = 'black') 

# Labels del eje x & y del Histograma
ax1.set_xlabel('fx(x)')
ax1.set_ylabel('Número total de valores', color='blue')


# Crear un segundo eje y (para la gráfica de puntos)
ax2 = ax1.twinx()

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [0, 0.3678, 0.2706, 0.1493, 0.0732, 0.0036, 0.0148, 0.0063, 0.0026,]

# Dibujar la gráfica de puntos en el segundo eje y
ax2.scatter(x, y, label='pdf', color='#21ABCD', marker='o')
ax2.plot(x, y, color='#00CC99')
ax2.set_ylim(0, 1)
ax2.set_ylabel('y', color='black')


# Añadir una leyenda
ax2.legend(loc='upper right')

plt.show()