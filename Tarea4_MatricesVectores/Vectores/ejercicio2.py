numeros = []
suma = 0

for i in range(10):
    num = float(input("Ingresa un numero: "))
    numeros.append(num)
    suma += num

promedio = suma / 10
print("El promedio es:", promedio)