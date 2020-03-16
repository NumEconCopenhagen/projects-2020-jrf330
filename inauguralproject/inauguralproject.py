import numpy as np 

def u_func(l, c, v, epsilon):
    
     return np.log(c) - v * (l**(1+1/epsilon)/(1+1/epsilon))
    

