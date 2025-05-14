

from sympy import symbols, factor

# Definir las variables
a, x, m = symbols('a x m')

# Ejercicio 8
exp8 = 8 * a * x**2 - 2 * a
print("Ejercicio 8:", factor(exp8))

# Ejercicio 9
exp9 = a**5 + a**3 - 2 * a
print("Ejercicio 9:", factor(exp9))

# Ejercicio 10
exp10 = 64 - m**6
print("Ejercicio 10:", factor(exp10))
