numeros = []
contador = 0

for i in range(8):
    num = float(input("Ingresa un numero: "))
    numeros.append(num)
    if num > 0:
        contador += 1

print("La cantidad de numeros positivos:", contador)
