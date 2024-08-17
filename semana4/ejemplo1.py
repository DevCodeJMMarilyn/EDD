# #listas
# lista = []
# listaDos=[1,3,5]
# print("ejemplo 1")
# print(listaDos)

# print("Ejemplo 2")
# #usando append
# listaTres=[]
# listaTres.append(12)
# listaTres.append(1)
# listaTres.append(90)
# listaTres.append(listaDos)
# print(listaTres)

# #para imprimir listas anidadas 
# print(len(listaTres))

# print("Ejemplo 3)")
# #usando extend se une o forma parte pero no se anida
# lista1 = [2,3,4,4]
# lista2= [43,23,65]
# lista.extend(lista2)
# print(lista1)


# print("Ejemplo 4: insert")
# #insertando elementos
# listaI=[2,3,4,4,43,23,65]
# listaI.insert(2,234)
# print(listaI)

# print("Ejemplo 5: remove")
# listaH=[2,3,4,4,43,23,65]
# listaH.remove(3)
# print(listaH)


print("Borrar")
listaF=["Juan","Pablo","Ricardo","Josseline"]
#listaF.pop(1)
print(listaF.pop(1))
print(listaF)

print("Limpiar lista del espacio de memoria")
listaD=["Juan","Pablo","Ricardo","Josseline"]
del listaD[2]
#del listaD
print(listaD)

print("Limpiar la los objetos de la lista sin borrar la lista")
listaC=["Juan","Pablo","Ricardo","Josseline"]
listaC.clear()
print(listaC)

print("Ordenas una lista de menor a mayor")
num=[1,5,8,9,4,6,3,7,95,102,87]
#num.sort() #menor a mayor
num.sort(reverse=True) #mayor a menor
print(num)

print("Invertir el orden de una lista")
num1=[1,5,8,9,4,6,3,7,95,102,87]
num1.reverse()
print(num1)

#
print("Contador")
listaCount=[22,22,33,65,8]
print(listaCount.count(22))

#
print("Limpiar una lista index")
listaIndex=["Juan","Pablo","Ricardo","Josseline"]
print(listaIndex.index("Ricardo"))
print(listaIndex)