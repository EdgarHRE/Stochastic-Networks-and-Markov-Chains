
#Libraries
import numpy as np
import math 
from lib_random.variable_aleatorias import * 


#Distribution class
class Distributions: 
    
    def __init__(self,lmbda):

        self.lmda = lmbda #Parameter lambda


    def Expo_Negative(lmbda,lista):

        expo_nega = [] #Empty list

        for expo in lista:  
            distri_expo = (-1/lmbda)*(np.log(1-expo))
            expo_nega.append(distri_expo)
        
        return expo_nega #Return a list with
    
    
    def K_expo(lista):

        k_values = []

        for i in range(0, len(lista),4):

            k = sum(lista[i:i+4])
            k_values.append(k)
        
        return k_values
    
    def Hiper(list_nums, lmbd1, lmbd2, p, elements):

        hiper_expo = []

        for i in range(1,elements+1):
            
            p_aleatory = Random_Var.One_var()


            if p_aleatory <= p:

                hyper1 = (-1 / lmbd1) * np.log(1-list_nums[i-1])
                
                hiper_expo.append(hyper1)
            
            else:

                hyper2 = (-1 / lmbd2) * np.log(1- list_nums[i-1])

                hiper_expo.append(hyper2)
        
        return hiper_expo

    
