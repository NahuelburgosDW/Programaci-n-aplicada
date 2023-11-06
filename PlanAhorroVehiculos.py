import os


# Definición de la clase Persona
class Persona:

  def __init__(self, dni, nombre, apellido, domicilio):
    self.dni = dni
    self.nombre = nombre
    self.apellido = apellido
    self.domicilio = domicilio

  def agregar_persona(self, lista_personas):
    lista_personas.append(self)

    def modificar_persona(self, atributo, nuevo_valor):
      if atributo == 'dni':
        self.dni = nuevo_valor
      elif atributo == 'nombre':
        self.nombre = nuevo_valor
      elif atributo == 'apellido':
        self.apellido = nuevo_valor
      elif atributo == 'domicilio':
        self.domicilio = nuevo_valor
      else:
        print(
            "Atributo no válido. Los atributos válidos son: dni, nombre, apellido, domicilio"
        )

    def eliminar_persona(self, lista_personas):
      input("Ingrese el DNI de la persona que desea eliminar: ")

    # Buscar la persona por su DNI en la lista
    persona_encontrada = None
    for persona in lista_personas:
      if persona.dni == dni_eliminar:
        persona_encontrada = persona
        break

    if persona_encontrada:
      confirmacion = input(
          f"¿Está seguro de eliminar a {persona_encontrada.nombre} {persona_encontrada.apellido}? (s/n): "
      )
      if confirmacion.lower() == 's':
        lista_personas.remove(persona_encontrada)
        print(
            f"La persona {persona_encontrada.nombre} {persona_encontrada.apellido} ha sido eliminada."
        )
      else:
        print("Operación cancelada.")
    else:
      print(f"No se encontró ninguna persona con DNI {dni_eliminar}.")

# Definición de la clase Cliente que hereda de Persona
# Definición de la clase Cliente que hereda de Persona

    class Cliente(Persona):

      def __init__(self, dni, nombre, apellido, domicilio, nro_cliente):
        super().__init__(dni, nombre, apellido, domicilio)
        self.nro_cliente = nro_cliente
        self.cuotas_pagadas = 0  # Nuevo atributo para llevar registro de cuotas pagadas

      def agregar_grupo(self, grupo):
        if grupo.cantidad_clientes < 5:  # Verificar si el grupo tiene menos de 5 clientes
          grupo.agregar_cliente(self)
          grupo.cantidad_clientes += 1  # Incrementar contador de clientes en el grupo
        else:
          print(
              "No se puede agregar más clientes a este grupo. Límite alcanzado."
          )

      def registrar_pago_cuota(self):
        if self.cuotas_pagadas < 8:  # Verificar que el cliente no haya pagado todas las cuotas
          self.cuotas_pagadas += 1
          print(f"Se registró el pago de la cuota {self.cuotas_pagadas}.")
          if self.cuotas_pagadas == 8:  # Si se completan las 8 cuotas, gestionar adjudicación
            self.gestionar_adjudicacion()

      def gestionar_adjudicacion(self):
        print("¡Felicidades! Usted ha completado el pago de todas las cuotas.")
        print("Seleccione el método de adjudicación:")
        print("1. Sorteo mensual")
        print("2. Pago completo de cuotas")
        print("3. Licitación")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
          if self.sorteo_mensual():
            print("¡Felicidades! Usted ha sido adjudicado por sorteo.")
            self.registrar_pago_cuota()  # Registrar el pago de una cuota
          else:
            print("Lo sentimos, no fue seleccionado en el sorteo.")
        elif opcion == '2':
          self.pago_completo_cuotas()
        elif opcion == '3':
          self.licitacion()
        else:
          print("Opción no válida. Por favor, seleccione una opción válida.")


# Definición de la clase Grupo
class Grupo:

  def __init__(self, nro_grupo, fecha_inicio, fecha_cierre):
    self.nro_grupo = nro_grupo
    self.fecha_inicio = fecha_inicio
    self.fecha_cierre = fecha_cierre
    self.cantidad_clientes = 0
    self.clientes = []
    self.vehiculos = []

  def agregar_cliente(self, cliente):
    self.clientes.append(cliente)
    self.cantidad_clientes += 1

  def agregar_vehiculo(self, vehiculo):
    self.vehiculos.append(vehiculo)

  def modificar_grupo(self):
    # Implementar la lógica para modificar un grupo
    pass

  def cerrar_grupo(self):
    # Implementar la lógica para cerrar un grupo
    pass


# Definición de la clase Plan
class Plan:

  def __init__(self, nombre_plan, fecha_apertura, fecha_cierre):
    self.nombre_plan = nombre_plan
    self.fecha_apertura = fecha_apertura
    self.fecha_cierre = fecha_cierre
    self.grupos = []

  def agregar_grupo(self, grupo):
    self.grupos.append(grupo)


# Definición de la clase Vehiculo
class Vehiculo:

  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas,
               cant_pasajeros):
    self.marca = marca
    self.modelo = modelo
    self.color = color
    self.cantidad_puertas = cantidad_puertas
    self.ruedas = ruedas
    self.cant_pasajeros = cant_pasajeros
    self.precio = precio
    self.matricula = None  # Atributo para almacenar la matrícula del vehículo

  def cargar(self):
    self.marca = input("Ingrese la marca del vehículo: ")
    self.modelo = input("Ingrese el modelo del vehículo: ")
    self.color = input("Ingrese el color del vehículo: ")
    self.cantidad_puertas = int(
        input("Ingrese la cantidad de puertas del vehículo: "))
    self.ruedas = int(input("Ingrese la cantidad de ruedas del vehículo: "))
    self.cant_pasajeros = int(
        input("Ingrese la cantidad de pasajeros del vehículo: "))
    self.precio = int(input("Ingrese el precio del vehículo: "))
    self.matricula = input("Ingrese la matrícula del vehículo: ")


class Camioneta(Vehiculo):

  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas,
               cant_pasajeros, carga, tolva):
    super().__init__(marca, modelo, color, cantidad_puertas, ruedas,
                     cant_pasajeros)
    self.carga = carga
    self.tolva = tolva

  def cargar(self, carga):
    # Implementar la lógica para cargar la camioneta
    pass


class Auto(Vehiculo):

  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas,
               cant_pasajeros, tipo):
    super().__init__(marca, modelo, color, cantidad_puertas, ruedas,
                     cant_pasajeros)
    self.tipo = tipo


def mostrar_menu():
  print("¡Bienvenido al Plan de Ahorro de Autos!")
  print("Por favor, seleccione una opción:")
  print("a. Gestionar Clientes")
  print("b. Gestionar Grupos de Clientes")
  print("c. Agregar pago de cuotas de los clientes")
  print("d. Registrar una adjudicación")
  print("e. Gestionar vehículos")
  print("q. Salir")


def limpiar_pantalla():
  os.system('clear' if os.name == 'posix' else 'cls')


def gestionar_clientes(lista_personas):
  print("Gestionando Clientes...")
  dni = input("Ingrese DNI del cliente: ")
  nombre = input("Ingrese nombre del cliente: ")
  apellido = input("Ingrese apellido del cliente: ")
  domicilio = input("Ingrese domicilio del cliente: ")
  nro_cliente = input("Ingrese número de cliente: ")

  cliente = Cliente(dni, nombre, apellido, domicilio, nro_cliente)
  cliente.agregar_persona(lista_personas)

  print("Cliente agregado con éxito.")


def gestionar_grupos():
  print("Gestionando Grupos de Clientes...")
  # Implementar lógica para gestionar grupos
  pass


def agregar_pago_cuotas():
  print("Agregando pago de cuotas de los clientes...")
  # Implementar lógica para agregar pagos de cuotas
  pass


def registrar_adjudicacion():
  print("Registrando una adjudicación...")
  # Implementar lógica para registrar una adjudicación
  pass


def gestionar_vehiculos():
  print("Gestionando vehículos...")
  # Implementar lógica para gestionar vehículos
  pass


lista_personas = []  # Lista para almacenar personas

while True:
  limpiar_pantalla()
  mostrar_menu()
  opcion = input("Seleccione una opción: ").lower()

  if opcion == 'a':
    gestionar_clientes(lista_personas)
  elif opcion == 'b':
    gestionar_grupos()
  elif opcion == 'c':
    agregar_pago_cuotas()
  elif opcion == 'd':
    registrar_adjudicacion()
  elif opcion == 'e':
    gestionar_vehiculos()
  elif opcion == 'q':
    print("¡Hasta luego!")
    break
  else:
    print("Opción no válida. Por favor, seleccione una opción válida.")


# Definición de la clase Cliente que hereda de Persona
class Cliente(Persona):
  # Constructor de la clase Cliente, que recibe los atributos de Persona y nro_cliente adicional
  def __init__(self, dni, nombre, apellido, domicilio, nro_cliente):
    # Llamada al constructor de la clase madre (Persona)
    super().__init__(dni, nombre, apellido, domicilio)
    # Atributo específico de Cliente
    self.nro_cliente = nro_cliente

  # Método para agregar un cliente a un grupo
  def agregar_grupo(self, grupo):
    # Invocación de un método de Grupo
    grupo.agregar_cliente(self)

  # Método para agregar un pago de cuota
  def agregar_pago_cuota(self, monto):
    # Implementar la lógica para agregar un pago de cuota
    pass

  # Método para registrar una adjudicación
  def registrar_adjudicacion(self, auto):
    # Implementar la lógica para registrar una adjudicación
    pass

  # Método para gestionar vehículos (debería implementarse)
  def gestionar_vehiculos(self):
    pass


# Definición de la clase Grupo
class Grupo:
  # Constructor de la clase Grupo
  def __init__(self, nro_grupo, fecha_inicio, fecha_cierre):
    self.nro_grupo = nro_grupo
    self.fecha_inicio = fecha_inicio
    self.fecha_cierre = fecha_cierre
    self.cantidad_clientes = 0
    self.clientes = []  # Lista de clientes asociados al grupo
    self.vehiculos = []  # Lista de vehículos asociados al grupo

  # Método para agregar un cliente al grupo
  def agregar_cliente(self, cliente):
    self.clientes.append(cliente)
    self.cantidad_clientes += 1

  # Método para agregar un vehículo al grupo
  def agregar_vehiculo(self, vehiculo):
    self.vehiculos.append(vehiculo)

  # Método para modificar un grupo (debería implementarse)
  def modificar_grupo(self):
    # Implementar la lógica para modificar un grupo
    pass

  # Método para cerrar un grupo (debería implementarse)
  def cerrar_grupo(self):
    # Implementar la lógica para cerrar un grupo
    pass


# Definición de la clase Plan
class Plan:
  # Constructor de la clase Plan
  def __init__(self, nombre_plan, fecha_apertura, fecha_cierre):
    self.nombre_plan = nombre_plan
    self.fecha_apertura = fecha_apertura
    self.fecha_cierre = fecha_cierre
    self.grupos = []  # Lista de grupos asociados al plan

  # Método para agregar un grupo al plan
  def agregar_grupo(self, grupo):
    self.grupos.append(grupo)


# Definición de la clase Vehiculo
class Vehiculo:
  # Constructor de la clase Vehiculo
  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas,
               cant_pasajeros):
    self.marca = marca
    self.modelo = modelo
    self.color = color
    self.cantidad_puertas = cantidad_puertas
    self.ruedas = ruedas
    self.cant_pasajeros = cant_pasajeros


# Definición de la clase Camioneta que hereda de Vehiculo
class Camioneta(Vehiculo):
  # Constructor de la clase Camioneta, que recibe los atributos de Vehiculo y carga, tolva adicionales
  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas,
               cant_pasajeros, carga, tolva):
    # Llamada al constructor de la clase madre (Vehiculo)
    super().__init__(marca, modelo, color, cantidad_puertas, ruedas,
                     cant_pasajeros)
    # Atributos específicos de Camioneta
    self.carga = carga
    self.tolva = tolva

  # Método para cargar la camioneta (debería implementarse)
  def cargar(self, carga):
    # Implementar la lógica para cargar la camioneta
    pass

  # Método para crear la camioneta (debería implementarse)
  def crear(self):
    # Implementar la lógica para crear la camioneta
    pass


# Definición de la clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
  # Constructor de la clase Auto, que recibe los atributos de Vehiculo y tipo adicional
  def __init__(self, marca, modelo, color, cantidad_puertas, ruedas,
               cant_pasajeros, tipo):
    # Llamada al constructor de la clase madre (Vehiculo)
    super().__init__(marca, modelo, color, cantidad_puertas, ruedas,
                     cant_pasajeros)
    # Atributo específico de Auto
    self.tipo = tipo


# Función para mostrar el menú principal
def mostrar_menu():
  print("¡Bienvenido al Plan de Ahorro de Autos!")
  print("Por favor, seleccione una opción:")
  print("a. Gestionar Clientes")
  print("b. Gestionar Grupos de Clientes")
  print("c. Agregar pago de cuotas de los clientes")
  print("d. Registrar una adjudicación")
  print("e. Gestionar vehículos")
  print("q. Salir")


# Función para limpiar la pantalla (dependiendo del sistema operativo)
def limpiar_pantalla():
  os.system('clear' if os.name == 'posix' else 'cls')


# Función para gestionar clientes (debería implementarse)
def gestionar_clientes():
  print("Gestionando Clientes...")
  dni = input("Ingrese DNI del cliente: ")
  nombre = input("Ingrese nombre del cliente: ")
  apellido = input("Ingrese apellido del cliente: ")
  domicilio = input("Ingrese domicilio del cliente: ")
  nro_cliente = input("Ingrese número de cliente: ")

  cliente = Cliente(dni, nombre, apellido, domicilio, nro_cliente)
  cliente.agregar_persona(lista_personas)

  # Aquí podríamos agregar el cliente a un grupo o realizar otras operaciones

  print("Cliente agregado con éxito.")


# Función para gestionar grupos (debería implementarse)
def gestionar_grupos():
  print("Gestionando Grupos de Clientes...")
  # Implementar lógica para gestionar grupos
  pass


# Función para agregar pagos de cuotas (debería implementarse)
def agregar_pago_cuotas():
  print("Agregando pago de cuotas de los clientes...")
  # Implementar lógica para agregar pagos de cuotas
  pass


# Función para registrar adjudicaciones (debería implementarse)
def registrar_adjudicacion():
  print("Registrando una adjudicación...")
  # Implementar lógica para registrar una adjudicación
  pass


# Función para gestionar vehículos (debería implementarse)
def gestionar_vehiculos():
  print("Gestionando vehículos...")
  # Implementar lógica para gestionar vehículos
  pass


# Bucle principal
while True:
  limpiar_pantalla()
  mostrar_menu()
  opcion = input("Seleccione una opción: ").lower()

  if opcion == 'a':
    gestionar_clientes()
  elif opcion == 'b':
    gestionar_grupos()
  elif opcion == 'c':
    agregar_pago_cuotas()
  elif opcion == 'd':
    registrar_adjudicacion()
  elif opcion == 'e':
    gestionar_vehiculos()
  elif opcion == 'q':
    print("¡Hasta luego!")
    break
  else:
    print("Opción no válida. Por favor, seleccione una opción válida.")
