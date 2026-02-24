# -*- coding: utf-8 -*-

# Declaracion de variables
import random as rd
HABITACION_SUCIA = 1
HABITACION_LIMPIA = 0

# Reglas codicion-accion
estado_habitaciones = (HABITACION_SUCIA, HABITACION_LIMPIA)

# Clases
class Habitacion():
    def __init__(self, estado, nombreHabitacion):
        # Atributos de las habitaciones

        # El estado de la habitacion, puede ser sucia o limpia, representado por 1 y 0 respectivamente.
        self.estado = estado
        # Nombre asignado a la habitacion.
        self.nombreHabitacion = nombreHabitacion
        # Contador que nos ayudara a decidir si la habitacion se ensucia o no. Representa 8 horas.
        self.horas = [1,2,3,4,5,6,7,8]
        # Determinara un numero aleatorio entre 1 y 8 para decidir si la habitacion se ensucia o no.
        self.ensucia = rd.choice(self.horas)
    
    # Metodos de las habitaciones (comportamientos)
    def ensuciarHabitacion(self):
        # Se elige una hora aleatoria, si coincide con la hora de ensuciar, la habitacion se ensucia, de lo contrario se elimina esa hora y se vuelve a intentar en la siguiente iteracion
        hora = rd.choice(self.horas)
        if hora == self.ensucia:
            self.estado = HABITACION_SUCIA
        else: 
            self.horas.remove(hora)
    # Al comprobase (en el objeto aspiradora) si esta sucia la habitacion antes de llamar a este metodo, solo se necesita cambiar el estado a limpia, sin necesidad de verificar denuevo.
    def limpieza(self):
        self.estado = HABITACION_LIMPIA

# Inicializacion de las habitaciones, se crean dos habitaciones con un estado aleatorio (sucia o limpia) y un nombre (A o B)
habitaciones = [Habitacion(rd.choice(estado_habitaciones), "A"), Habitacion(rd.choice(estado_habitaciones),"B")]

class Aspiradora():
    def __init__(self):
        # Atributos de la aspiradora

        # Iniciamos en una habitacion aleatoria
        self.posicion = rd.randint(0, len(habitaciones) - 1)
        # Llevamos la contabilizacion de las habitaciones aspiradadas
        self.limpiezasTotales = 0 
        # Se toma en cuenta la bateria, como metrica de desempeño, cada punto represnta 1 hora de funcionamiento.
        self.bateria = 4
        # La aspiradora cuenta con bateria?
        self.bateriaDisponible = True
        # Meta a culplir, si se limpian 2 habitaciones, la aspiradora debera detenerse.
        self.meta = 2

# Metodos de la aspiradora
    # Se comprueba la bateria, en caso de no tener se apaga la aspiradora y termina el programa. Accion basica = detener
    def comprobar_bateria(self):
        if self.bateria < 1:
            print("Bateria baja, apagando...")
            self.bateriaDisponible = False
    
    # Se mueve la posicion de la aspiradora a la siguiente habitacion. Accion basica = mover
    def mover_sig_habitacion(self):
        self.comprobar_bateria()
        # la posicion se mueve en 1, si se llega al limite, con el operador modulo regresamos al inicio
        self.posicion = (self.posicion + 1) % len(habitaciones)
        self.bateria = self.bateria - 1
        print("Aspiradora se mueve a habitacion ", habitaciones[self.posicion].nombreHabitacion)
    
    # Se aspira la habitacion actual. Accion basica = limpiar
    def aspirar(self):
        self.comprobar_bateria()
        self.limpiezasTotales = self.limpiezasTotales + 1
        self.bateria = self.bateria - 1
        habitaciones[self.posicion].limpieza()
        print("Aspiradora limpia habitacion ", habitaciones[self.posicion].nombreHabitacion)
    
    # Se decide sobre si limpiar o moverse de habitacion. Implementacion de IF SUCIO THEN {...} ELSE
    def decidir_accion(self):
        if habitaciones[self.posicion].estado == HABITACION_SUCIA:
            self.aspirar()
        else:
            print(f"Habitacion {habitaciones[self.posicion].nombreHabitacion} limpia, moviendo a siguiente habitacion...")
            self.mover_sig_habitacion()
    
    # Funcion principal de la aspiradora, donde se repiten el proceso de decidir accion, hasta que la bateria se agote y se apague la aspiradora. Implementacion de WHILE BATERIA DISPONIBLE THEN {...}
    # Implementacion de REPEAT n {...} . Donde n es la cantidad de bateria que posee la aspiradora, cada iteracion representa 1 hora de funcionamiento, y en cada iteracion se decide si limpiar o moverse, hasta que la bateria se agote.
    def repetir(self):
        while self.bateriaDisponible == True: 
            # La aspiradora verifica si la habitacion esta sucia, en caso contrario se mueve
            self.decidir_accion()
            
            # Se comprueba si se cumplio la meta. En caso de cumplirse, se detiene la aspiradora y termina el programa.
            if self.limpiezasTotales >= self.meta:
                print(f"Se limpiaron {self.limpiezasTotales} antes de apagarse. se cumplio la meta")
                return
            
            # Condiciones de la vida real actuan
            vidaReal()

        print(f"Se limpiaron {self.limpiezasTotales} antes de apagarse. No se cumplio la meta")

# Comportamiento de la vida real relacionado con las habitaciones y su limpieza
def vidaReal():
    for habitacion in habitaciones:
        habitacion.ensuciarHabitacion()

def casoPrueba1():
    global habitaciones
    # Se crean dos habitaciones, una sucia y otra limpia, para verificar que la aspiradora limpie la sucia y se mueva a la limpia.
    habitaciones[0].estado = HABITACION_SUCIA
    habitaciones[1].estado = HABITACION_LIMPIA
    aspiradora = Aspiradora()
    aspiradora.posicion = 0 # Iniciamos en la habitacion sucia
    aspiradora.decidir_accion() # Se espera que limpie la habitacion A
    aspiradora.decidir_accion() # Se espera que se mueva a la habitacion B

def casoPrueba2():
    global habitaciones
    # Se crean dos habitaciones limpias, para verificar que la aspiradora se mueva a ambas sin limpiar.
    habitaciones[0].estado = HABITACION_LIMPIA
    habitaciones[1].estado = HABITACION_LIMPIA
    aspiradora = Aspiradora()
    aspiradora.posicion = 0 # Iniciamos en la habitacion A
    aspiradora.decidir_accion() # Se espera que se mueva a la habitacion B
    aspiradora.decidir_accion() # Se espera que se mueva a la habitacion A
    
# Metodo principal, donde se crea una instancia de la aspiradora y se llama a su metodo repetir.     
def main():
    aspiradora = Aspiradora()
    aspiradora.repetir()
#main()
print("Ejecutando caso de prueba 1:")
casoPrueba1()
print("\nEjecutando caso de prueba 2:")
casoPrueba2()