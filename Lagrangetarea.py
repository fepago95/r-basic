# importamos la interpolación de Langrange del módulo de interpolación de Scipy
from scipy.interpolate import lagrange
# importamos la librería Numpy con un alias, para hacer los cálculos
import numpy as np
# importamos la librería Sympy, para desarrollar la forma algebraica del polinomio
import sympy as sym
# importamos la librería Matplotlib con un alias, para graficas
import matplotlib.pyplot as plt

# Procedimiento
def lagrange_polinomio(xi,fi):# Conocer cuantos elementos tiene xi 
    
    #Uso de función de la librería lagrange
    p = lagrange(xi,fi)
    # print('polinomio con lagrange')
    # print(p)
    res=round(p(55),2)

    # Vectores para graficas
    muestras = 100 # Numero cualquiera
    a = np.min(xi)
    #print(a)
    b = np.max(xi)
    #print(b)
    p_xi = np.linspace(a,b,muestras)
    pfi = p(p_xi)

    # Grafica
    plt.plot(xi,fi, 'o')
    plt.plot(p_xi,pfi)
    plt.show()

    return res


# Interpolación para hayar teta_s
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([170, 160, 150, 140, 130, 120, 110, 100, 90])
teta_s=lagrange_polinomio(xi,fi)
print("teta_s:",teta_s)

#Interpolación para hayar % de ciclo:
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([5.6, 11.1, 16.7, 22.2, 27.8, 33.3, 38.9, 44.4, 50])
per_cycle=lagrange_polinomio(xi,fi)
print("porcentaje de ciclo:",per_cycle)

#Interpolación para hayar Minimo delta Cy:
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.00001, 0.00004, 0.00027, 0.001, 0.004, 0.010, 0.023, 0.047, 0.096])
Min_Cy=lagrange_polinomio(xi,fi)
print("porcentaje Minimo delta Cy:",Min_Cy)

#Interpolacion para hayar Porcentaje delta V:
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.38, 1.53, 3.48, 6.27, 9.90, 14.68, 20.48, 27.17, 35.31])
delta_V=lagrange_polinomio(xi,fi)
print("Porcentaje delta V:",delta_V)

#Interpolacion para hayar Vx/(L2_w2)
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([1.436, 1.504, 1.565, 1.611, 1.646, 1.679, 1.702, 1.717, 1.725])
Vx_L2_w2=lagrange_polinomio(xi,fi)
print("Vx/(L2_W2:",Vx_L2_w2)

#Interpolacion para hayar L1/L2:
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([2.975, 2.950, 2.900, 2.825, 2.725, 2.625, 2.500, 2.350, 2.200])
L1_L2=lagrange_polinomio(xi,fi)
print("L1/L2:",L1_L2)

#Interpolacion para L3/L2:
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([3.963, 3.925, 3.850, 3.738, 3.588, 3.438, 3.250, 3.025, 2.800])
L3_L2=lagrange_polinomio(xi,fi)
print("L3/L2:",L3_L2)

#Interpolacion para deltaX/L2
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.601, 1.193, 1.763, 2.299, 2.790, 3.238, 3.623, 3.933, 4.181])
deltaX_L2=lagrange_polinomio(xi,fi)
print("deltaX_L2:",deltaX_L2)

#Interpolacion porcentaje Minimo para Vx:
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.006, 0.038, 0.106, 0.340, 0.910, 1.885, 3.327, 5.878, 9.299])
Min_Vx=lagrange_polinomio(xi,fi)
print("Porcentaje Minimo Vx:",Min_Vx)

#Interpolacion delta Cy:
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([0.137, 0.274, 0.387, 0.503, 0.640, 0.752, 0.888, 1.067, 1.446])
delta_Cy=lagrange_polinomio(xi,fi)
print("Delta_Cy",delta_Cy)