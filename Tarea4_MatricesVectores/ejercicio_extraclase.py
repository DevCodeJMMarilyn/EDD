# Datos básicos del estudiante
Datos_Basicos = {
    "Inicio de ciclo": "15 Julio",
    "Fin de ciclo": "15 Diciembre",
    "Ciclo actual": "Ciclo IV",
    "Carnet estudiante": "U20231085",
    "Carrera": "Ingeniería En Desarrollo de Software",
    "Fechas de pago": ["17 jul", "17 agos", "17 sep"],
    "Materias que cursa": ["Programación Orientada a Eventos", "Metodos numericos", "Estructura de Datos"]
}

def mostrar_menu():
    print("\n---** Bienvenido a la aplicación WUNIVO **---")
    print("1. Ver inicio de ciclo")
    print("2. Ver fin de ciclo")
    print("3. Ver ciclo actual")
    print("4. Ver carnet del estudiante")
    print("5. Ver carrera")
    print("6. Ver fechas de pago")
    print("7. Ver materias que cursa")
    print("8. Salir :D")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Inicio de ciclo:", Datos_Basicos["Inicio de ciclo"])
        elif opcion == "2":
            print("Fin de ciclo:", Datos_Basicos["Fin de ciclo"])
        elif opcion == "3":
            print("Ciclo actual:", Datos_Basicos["Ciclo actual"])
        elif opcion == "4":
            print("Carnet del estudiante:", Datos_Basicos["Carnet estudiante"])
        elif opcion == "5":
            print("Carrera:", Datos_Basicos["Carrera"])
        elif opcion == "6":
            print("Fechas de pago:", ", ".join(Datos_Basicos["Fechas de pago"]))
        elif opcion == "7":
            print("Materias que cursa:", ", ".join(Datos_Basicos["Materias que cursa"]))
        elif opcion == "8":
            print("Hasta la proxima...")
            break
        else:
            print("Opción no invalida. Selecciona un numero del 1 al 8")

# main para que quede en bucle el programa
main()
