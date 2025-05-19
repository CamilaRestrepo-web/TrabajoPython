from sympy import symbols, solve, pprint, Eq

# Definir la variable simbólica
x = symbols('x')

# Ecuaciones dadas
eq1 = Eq(x**3 + 6*x, 0)
eq2 = Eq(4*x**2 - 8*x, 0)
eq3 = Eq(5*x - x**2, 0)

# Resolver cada ecuación
raices1 = solve(eq1, x)
raices2 = solve(eq2, x)
raices3 = solve(eq3, x)

# Imprimir resultados
print("Raíces de x³ + 6x = 0:")
pprint(raices1)
print("\nRaíces de 4x² - 8x = 0:")
pprint(raices2)
print("\nRaíces de 5x - x² = 0:")
pprint(raices3)
