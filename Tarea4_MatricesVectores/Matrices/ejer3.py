#Pide al usuario llenar una matriz de 2x3 y muestra su transpuesta.

matriz = []
for i in range(2):
    fila = []
    for j in range(3):
        num = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
        fila.append(num)
    matriz.append(fila)

transpuesta = [[matriz[j][i] for j in range(2)] for i in range(3)]

print("La matriz ingresada es:")
for fila in matriz:
    print(fila)

print("La transpuesta de la matriz es:")
for fila in transpuesta:
    print(fila)