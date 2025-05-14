U = list(range(0, 19))  # U = {0, 1, ..., 18}

A = [x for x in U if x % 2 == 0 and x < 10]  # Pares menores que 10
B = [x for x in U if x != 0 and 12 % x == 0]  # Divisores de 12 diferentes de 0
conjuntoC = [x for x in U if x < 6]  # Números menores que 6
conjuntoD = [x for x in U if x % 2 == 0 and x <= 6]  # Pares y menores o igual a 6
conjuntoE = [x for x in U if x < 10]  # Números menores que 10
F = [x for x in U if x > 13]  # Números mayores que 13
G = [x for x in U if x % 2 == 0 and x > 10]  # Pares y mayores que 10


#Ejercicio 2
ejercicio_2 = sorted(set(B).union(conjuntoC))
print("Ejercicio 2:", ejercicio_2)

#Ejercicio 18
complemento_B = sorted(set(U).difference(B))  # B'
print("Complemento de B:", complemento_B)
ejercicio_18 = sorted(set(A).union(complemento_B))
print("Ejercicio 18:", ejercicio_18)

#Ejercicio 20
complemento_A = sorted(set(U).difference(A))  # A'
print("Complemento de A:", complemento_A)
ejercicio_20 = sorted(set(complemento_A).difference(G))
print("Ejercicio 20:", ejercicio_20)
