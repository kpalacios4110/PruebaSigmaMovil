
import random


class Jugador:
    def __init__(self, nombre, dinero):
        self.nombre = nombre
        self.dinero = dinero

    def apostar(self, modo, cantidad):
        # Validar que la cantidad sea válida
        if cantidad < 0 or cantidad > self.dinero:
            print("Cantidad no válida")
            return

        # Validar que el modo sea válido
        if modo != "verde" and modo != "rojo" and modo != "negro":
            print("Modo no válido")
            return

        # Ajustar la cantidad según el límite
        if self.dinero <= 1000:
            cantidad = self.dinero

        # Realizar la apuesta
        if modo == "verde":
            if random.random() <= 0.02:
                self.dinero += cantidad * 15
            else:
                self.dinero -= cantidad
        elif modo == "rojo" or modo == "negro":
            if random.random() <= 0.49:
                self.dinero += cantidad * 2
            else:
                self.dinero -= cantidad

    def modificar_dinero(self, cantidad):
        self.dinero += cantidad

    def eliminar(self):
        # Eliminar el jugador de la lista
        jugadores.remove(self)

# Definir una lista para almacenar los jugadores
jugadores = []

# Agregar un jugador por defecto
jugadores.append(Jugador("Jugador 1", 10000))

# Iniciar el menú principal
while True:
    # Mostrar el menú principal
    print("Menú principal")
    print("1. Ingresar jugador")
    print("2. Modificar jugador")
    print("3. Eliminar jugador")
    print("4. Jugar")
    print("5. Mostrar Jugadores")
    print("6. Salir")

    # Solicitar una opción al usuario
    opcion = input("Ingrese una opción: ")

    # Procesar la opción seleccionada
    if opcion == "1":
        # Ingresar un nuevo jugador
        nombre = input("Ingrese el nombre del jugador: ")
        dinero = int(input("Ingrese la cantidad de dinero del jugador: "))
        jugadores.append(Jugador(nombre, dinero))
    elif opcion == "2":
        # Modificar un jugador existente
        nombre = input("Ingrese el nombre del jugador a modificar: ")
        for jugador in jugadores:
            if jugador.nombre == nombre:
                # Solicitar los datos a modificar
                cantidad = int(input("Ingrese la nueva cantidad de dinero: "))
                jugador.modificar_dinero(cantidad)
                break
    elif opcion == "3":
        # Eliminar un jugador existente
        nombre = input("Ingrese el nombre del jugador a eliminar: ")
        for jugador in jugadores:
            if jugador.nombre == nombre:
                jugador.eliminar()
                break
    elif opcion == "4":
        # Jugar una ronda
        # Seleccionar un jugador aleatorio
        jugador = jugadores[random.randint(0, len(jugadores) - 1)]

        # Solicitar el modo de apuesta
        modo = input("Ingrese el modo de apuesta (verde, rojo o negro): ")

        # Solicitar la cantidad a apostar
        cantidad = int(input("Ingrese la cantidad a apostar: "))

        # Realizar la apuesta
        jugador.apostar(modo, cantidad)

        # Mostrar el resultado de la apuesta
        if jugador.dinero > 0:
            print("El jugador ganó!")
        else:
            print("El jugador perdió!")
   
    elif opcion == "5":
        # Mostrar jugadores 
        for jugador in jugadores:
             print("Nombre:", jugador.nombre)
             print("Dinero:", jugador.dinero)
      
    elif opcion == "6":
        # Salir del programa
        break

    
    