#Solicita una matriz cuadrada de tamaño 3x3 y muestra los elementos de su diagonal principal

matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        num = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
        fila.append(num)
    matriz.append(fila)

diagonal = [matriz[i][i] for i in range(3)]

print("La matriz ingresada es:")
for fila in matriz:
    print(fila)

print("Los elementos de la diagonal principal son:", diagonal)
