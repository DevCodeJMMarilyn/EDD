numeros = []

for i in range(7):
    num = float(input(f"Ingrese el numero {i + 1}: "))
    numeros.append(num)

mayor = max(numeros)
print("Los numeros ingresados son:", numeros)
print("El mayor numero es:", mayor)
