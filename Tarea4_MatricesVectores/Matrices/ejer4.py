#Realiza la multiplicación de dos matrices de 2x2. Solicita los datos para ambas matrices y muestra el resultado.

matriz_a = []
matriz_b = []

print("Ingrese los elementos de la primera matriz (2x2):")
for i in range(2):
    fila = []
    for j in range(2):
        num = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
        fila.append(num)
    matriz_a.append(fila)

print("Ingrese los elementos de la segunda matriz (2x2):")
for i in range(2):
    fila = []
    for j in range(2):
        num = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
        fila.append(num)
    matriz_b.append(fila)

resultado = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        resultado[i][j] = matriz_a[i][0] * matriz_b[0][j] + matriz_a[i][1] * matriz_b[1][j]

print("El resultado de la multiplicación es:")
for fila in resultado:
    print(fila)
