numeros = []

for i in range(6):
    num = float(input("Ingresa un numero: "))
    numeros.append(num)

num_invertidos = numeros[::-1]
print("Los números ingresados son:", numeros)
print("Numeros en orden inverso:", num_invertidos)
