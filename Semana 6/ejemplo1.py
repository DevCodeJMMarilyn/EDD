#una matriz tiene filas y columnas

#Tipos de diccionarios
Datos_Basicos = {
    "Nombres": "Juan Carlos",
    "Apellidos":"Perez Garcia",
    "Dui":"0978456-8",
    "Fecha_Nacimiento":"19/09/99",
    "Lugar_Nacimiento":"Soya City",
    "Nacionalidad":"Salvadoreña",
    "Estado_Civil": "Complicado"
}

print("\nDetalle del dicionario")
print("\n***********************")

print("\nClaves del diccionario: ", Datos_Basicos.keys())
print("\nValores del diccionario: ", Datos_Basicos.values())
print("\nElementos del diccionario: ", Datos_Basicos.items())

#Ejemplo practico
print("\nInscripción del curso")
print("\n***********************")

print("\nDatos del participante")
print("\n***********************")

print("Dui: ", Datos_Basicos["Dui"])
print("Nombre completo: ",Datos_Basicos["Nombres"]+"", Datos_Basicos["Apellidos"])

print("\n***********************")








