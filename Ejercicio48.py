from sympy import symbols, simplify

# Definimos las variables
m, n, b, y, p = symbols('m n b y p')

# Ejercicio 8
expr8 = m**2 - n**2 + 4 + 4*m - 1 - 2*n
simplified_expr8 = simplify(expr8)

# Ejercicio 9
expr9 = 2*b*y - y**2 + 1 - b**2
simplified_expr9 = simplify(expr9)

# Ejercicio 10
expr10 = 25*p**2 - 2*m - m**2 - 1
simplified_expr10 = simplify(expr10)

# Mostramos los resultados
print("Ejercicio 8 simplificado:", simplified_expr8)
print("Ejercicio 9 simplificado:", simplified_expr9)
print("Ejercicio 10 simplificado:", simplified_expr10)
