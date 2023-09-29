import numpy as np

def is_iterable(var):
    try:
        iter(var)
        return True
    except TypeError:
        return False
    
def Numpy_roots(self,a,b,c,d):#Metodo de calculo do Numpy
    coef = [a,b,c,d]
    raizes = np.roots(coef)
    raizes_reais = raizes[np.logical_and(raizes.real > 0, raizes.imag == 0)]
    return np.real(raizes_reais[0])
    pass

def Newton(self,a,b,c,d):#Metodo de calculo usando Newton Raphson
    x0=1
    i = 0
    MF = 1.0
    while (MF > 10**(-13)):
        F = a*x0**3 + b*x0**2 + c*x0 + d
        dF = 3*a*x0**2 + 2*b*x0 + c
        if dF == 0.0:
            x1 = x0 - F/(dF + 10**(-13))
        else:
            x1 = x0 - F/dF
        F = a*x1**3 + b*x1**2 + c*x1 + d
        MF = abs(F)
        i=i+1
        x0=x1
        if i > 100:
            #print ("Não convergiu")
            break
    # print(f"Convergiu em {i}")
    return x0
    pass

def arred(list,num):
    list = [round(item,num) for item in list]
    return list
    pass