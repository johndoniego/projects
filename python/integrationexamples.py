from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
from math import cos, pi, e
import sympy as sp

x = sp.symbols('x', real=True)
f = sp.cos(x)
result = sp.integrate(f, x)
print(result)

half = pi/2

def integrand(x):
    return np.cos(x)

i, error = quad(integrand, 0, half)
print(i)
derivative = "The integral of cos(x) is " + str(result) + " and when x is " + str(round(half,2)) + " the value is " + str(round(i, 2))

x = np.linspace(0, pi, 100)
 
plt.plot(x,integrand(x), linestyle='-', color='blue', lw=2, label = derivative)
plt.axhline(0, color='black', lw=0.5)
plt.fill_between(x, integrand(x), where= [(x>=0) and (x<=half) for x in x], color='yellow', alpha=0.5)
plt.legend(loc='upper right')
plt.show()




