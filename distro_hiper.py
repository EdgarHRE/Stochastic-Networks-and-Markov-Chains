
# Liberias 

from math import exp
from lib_random.distributions import *
from lib_random.variable_aleatorias import *
import matplotlib.pyplot as plt
import seaborn as sn
import statistics as static
import numpy as np

# Ingresa el número de variables aleatorias.
elements = int(input('Ingrese de n elementos en la lista: '))

# Ingresa el valor de lambda 1 que se usara en las distribuciones hiper-exponenciales.
lmbd1 = float(input('Ingresa el valor de lambda 1: '))

# Ingresa el valor de lambda 2 que usara en las distribuciones hiper-exponenciales.
lmbd2 = float(input('Ingrese el valor de lambda 2: '))

# Ingresa el valor de p.
p = float(input('Ingresa el valor de p: '))

# Variable list_nums crea n variables pseudo-aleatorias.
list_nums = Random_Var.Method_1(elements)

# Variable expo_nega crea una lista de n variables exponenciales.
#expo_nega = Distributions.Expo_Negative(lmbd, list_nums) # parametros -> (float, list)

# Variable hiper crea una lista de n variables de hiper exponenciales.
hiper = Distributions.Hiper(list_nums, lmbd1, lmbd2, p, elements)

# Lee la lista hiper.txt para sumar todos los valores obtenidos en la variable expo_nega

with open('hiper.txt', 'w') as salida:
    
    for linea in hiper:
        
        salida.write(str(linea))
        salida.write('\n')
       
    
    media = static.mean(hiper) # Calcula la media de todos los valores obtenidos
    var = static.variance(hiper) # Calcula la varianza todos los valores obtenidos
    cov = (math.sqrt(var)) / media # Calcula el coficiente de variacion de los valores obtenidos

    print(f'La media es: {media}, La varianza es: {var}, La covarianza es: {cov}')


# Obtencion de un Histograma y grafica de la pdf.

intervalos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # Bins del histograma

fig, ax1 = plt.subplots() 

# Desarrollo del histograma
ax1.hist(hiper, bins = intervalos, color = '#FF8C00', ec = 'black') 

# Labels del eje x & y del Histograma
ax1.set_xlabel('fx(x)')
ax1.set_ylabel('Número total de valores', color='blue')


# Crear un segundo eje y (para la gráfica de puntos)
ax2 = ax1.twinx()

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [1.4286, 0.2315, 0.0956, 0.05019, 0.03928, 0.02629, 0.01726, 0.0118, 0.0070]

# Dibujar la gráfica de puntos en el segundo eje y
ax2.scatter(x, y, label='pdf', color='black', marker='o')
ax2.plot(x, y, color='black')
ax2.set_ylim(0, 1.5)
ax2.set_ylabel('y', color='black')


# Añadir una leyenda
ax2.legend(loc='upper right')

plt.show()