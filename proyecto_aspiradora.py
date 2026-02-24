# -*- coding: utf-8 -*-

# Declaracion de variables
import random as rd
HABITACION_SUCIA = 1
HABITACION_LIMPIA = 0
PROGRAMA = 1

# Reglas codicion-accion
estado_habitaciones = (HABITACION_SUCIA, HABITACION_LIMPIA)

# Clases
class Habitacion():
    def __init__(self, estado, nombreHabitacion):
        self.estado = estado
        self.nombreHabitacion = nombreHabitacion
# Metodos de las habitaciones (comportamientos)
    def ensuciarHabitacion(self):
        self.estado = rd.choice(estado_habitaciones)

    def limpieza(self):
        self.estado = HABITACION_LIMPIA

habitaciones = [Habitacion(rd.choice(estado_habitaciones), "A"), Habitacion(rd.choice(estado_habitaciones),"B")]

# Comportamiento de la vida real relacionado con las habitaciones y su limpieza
def vidaReal():
    for habitacion in habitaciones:
        habitacion.ensuciarHabitacion()

class Aspiradora():

    def __init__(self):
        # Atributos de la aspiradora

        # Iniciamos en una habitacion aleatoria
        self.posicion = rd.randint(0, len(habitaciones) - 1)
        # Llevamos la contabilizacion de las habitaciones aspiradadas
        self.limpiezasTotales = 0 
        # Se toma en cuenta la bateria, como metrica de desempeño
        self.bateria = 20

# Metodos de la aspiradora
    # Se comprueba la bateria, en caso de no tener se apaga la aspiradora y termina el programa
    def comprobar_bateria(self):
        global PROGRAMA
        if self.bateria < 1:
            print("Bateria baja, apagando...")
            PROGRAMA = 0
    # Se mueve la posicion de la aspiradora a la siguiente habitacion 
    def mover_sig_habitacion(self):
        self.comprobar_bateria()
        # la posicion se mueve en 1, si se llega al limite, con el operador modulo regresamos al inicio
        self.posicion = (self.posicion + 1) % len(habitaciones)
        self.bateria = self.bateria - 1
        print("Aspiradora se mueve a habitacion ", habitaciones[self.posicion].nombreHabitacion)
    # Se aspira la habitacion actual 
    def aspirar(self):
        self.comprobar_bateria()
        self.limpiezasTotales = self.limpiezasTotales + 1
        self.bateria = self.bateria - 2
        habitaciones[self.posicion].limpieza()
    # Se decide sobre si limpiar o moverse de habitacion
    def decidir_accion(self):
        if habitaciones[self.posicion].estado == HABITACION_SUCIA:
            self.aspirar()
        else:
            print("Habitacion limpia, moviendo a siguiente habitacion...")
            self.mover_sig_habitacion()

def main():
    aspiradora = Aspiradora()
    while PROGRAMA == 1:
        # La aspiradora verifica si la habitacion esta sucia, en caso contrario se mueve
        aspiradora.decidir_accion()

        # Condiciones de la vida real actuan
        vidaReal()
    print(f"Se limpiaron {aspiradora.limpiezasTotales} antes de apagarse.")

main()

"""
def repetir_acciones(veces):
    for i in range(veces):
        print("Repeticion", i + 1)
        siguiente_habitacion = (posicion_robot + 1) % len(estado_habitaciones)
        decidir_accion(siguiente_habitacion)

def caso_prueba_if():
    global posicion_robot
    print("\n--- CASO IF SUCIO ---")

    posicion_robot = 0
    decidir_accion(1)
    decidir_accion(2)

caso_prueba_if()

def caso_prueba_repeat():
    global posicion_robot
    print("\n--- CASO REPEAT ---")

    posicion_robot = 0
    repetir_acciones(5)

caso_prueba_repeat()

if total_limpiezas >= meta_limpiezas:
    detener_robot()
else:
    print("Meta aun no alcanzada")
"""