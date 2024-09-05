#Genera una matriz identidad de tamaño 4x4

matriz= [[1 if i == j else 0 for j in range(4)] for i in range(4)]

print("La matriz 4x4 es:")
for fila in matriz:
    print(fila)