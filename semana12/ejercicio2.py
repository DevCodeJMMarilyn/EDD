class Rutina:
    def __init__(self):
        self.actividades = []
        self.hora_inicio = 7 # 7:00 a.m.

    def agregar_actividad(self, actividad, tiempo):
        self.actividades.append((actividad, tiempo))
    
    def mostrar_rutina(self):
        hora_actual = self.hora_inicio
        for actividad, tiempo in self.actividades:
            print(f"{actividad}: {hora_actual}:00 - {hora_actual + tiempo}:00")
        hora_actual += tiempo
    
    def buscar_actividad(self, actividad):
        for act, tiempo in self.actividades:
            if act.lower() == actividad.lower():
                return f"{actividad} se realiza durante {tiempo} horas."
        return f"{actividad} no se encuentra en la rutina."
    
    def tiempo_total(self):
        total_horas = sum(tiempo for _, tiempo in self.actividades)
        return f"Tiempo total de actividades: {total_horas} horas."

rutina = Rutina()
rutina.agregar_actividad('Despertarse', 0.5)
rutina.agregar_actividad('Ducharse', 0.5)
rutina.agregar_actividad('Hacer aseo', 0.5)
rutina.agregar_actividad('Estudiar', 1)
rutina.agregar_actividad('Salir de casa', 0.5)
rutina.mostrar_rutina()
print(rutina.buscar_actividad('Despertarse'))
print(rutina.buscar_actividad('Ejercitarse'))
print(rutina.tiempo_total())