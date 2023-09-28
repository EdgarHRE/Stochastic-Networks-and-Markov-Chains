"""
Este programa es una libreria para crear variables pseudo aleatorias uniformes.

"""

from random import randint #Libreria random
import random

#Se creo una clase Random_Var, para mayor facilidad al crear funciones diferentes y poder llamarlas de manera eficaz

class Random_Var: #Clase Random_Var

    def __init__(self, num_var): #Constructor __init__ que incluye los atributos de la clase ->(num_var)
        self.num_var = num_var #Atributos de la clase -> num_var = numero de variable aleatorias que se crearan
    
    #Funcion para crear variables pseudo aleatorias entre [0,1]... Metodo del Profesor
    def Method_1(num_var): #Funcion Mathod_1 -> recibe el atributo  num_var 
        
        random_nums = [] #Lista vacia

        for i in range(1,num_var+1 ): #Iteracion for que va de 0 a num_var
            v_aleatory = randint(1,1000000) #Se selecciona 1 numero aleatorio entre 1 y 1000000 
            number = v_aleatory / 1000000 #El valor aleatorio selecionado se divide entre 1000000
            random_nums.append(number) #A la lista vacia se le agrega el valor de a y lo guarda

        return random_nums #regresa la lista que contiene todos los valores aleatorios asigandos previeamente
    
    
    #Funcion para crear variables pseudo aleatorias entre [0,1]... Metodo Libreria de Python.
    def Method_2(num_var):

        random_nums_2 = [] #Lista vacia

        for j in range(0,100000): #Iteracion for que va de 0 a num_var
            b = random.uniform(0,1) #Se selecciona 1 numero aleatorio entre 0 y 1.000000001
            random_nums_2.append(b) #A la lista vacia se le agrega el valor de la variable b y lo guarda
        
        print(len(random_nums_2)) # Imprime el tamaño de lista esto para saber si se realizo los n valores aleatorios.

        return random_nums_2 #regresa la lista que contiene todos los valores aleatorios asigandos previeamente
    
    
    def  One_var():

        v_aleatory = randint(1, 1000000)
        number = v_aleatory / 1000000

        return number

