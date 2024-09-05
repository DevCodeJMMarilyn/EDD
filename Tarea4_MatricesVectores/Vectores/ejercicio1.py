#Crea un programa que pida al usuario ingresar 5 números en un vector y luego calcule la suma de todos los elementos.

numeros = []
suma = 0

for i in range(5):
    num = float(input("Ingresa un numero: "))
    numeros.append(num)
    suma += num

print("La suma de los elementos es:", suma)
