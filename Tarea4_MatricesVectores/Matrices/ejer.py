#Solicita al usuario llenar una matriz de 3x3 y calcula la suma de todos sus elementos.

matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        num = float(input(f"Ingrese el elemento [{i + 1}][{j + 1}]: "))
        fila.append(num)
    matriz.append(fila)

suma = sum(sum(fila) for fila in matriz)

print("La matriz ingresada es:")
for fila in matriz:
    print(fila)
print("La suma de todos los elementos es:", suma)