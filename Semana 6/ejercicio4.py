#solicitar el numero de filas y columnas
filas = int(input("Ingresa el numero de filas: "))
columnas= int(input("Ingresa el numero de columnas: "))

#inicializar la matriz
matriz = [["A" for _ in range(columnas)] for _ in range(filas)]

#mostrar la matriz resultante
print("\nLa matriz resultante es:")
for fila in matriz:
    print(fila)
