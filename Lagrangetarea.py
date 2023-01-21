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
    
    # Ejemplo con la librería lagrange
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

# print(' ')
# print('Evaluación del polinomio')
# print(px(5.5)

# Función 
xi = np.array([20, 40, 60, 80, 100, 120, 140, 160, 180])
fi = np.array([170, 160, 150, 140, 130, 120, 110, 100, 90])
teta_s=lagrange_polinomio(xi,fi)
print(teta_s)