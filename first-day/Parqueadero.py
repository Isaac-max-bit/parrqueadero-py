from datetime import datetime

# Capacidad máxima del parqueadero
CAPACIDAD_MAXIMA = 10

# Lista para almacenar los vehículos estacionados
vehiculos_estacionados = []


# Función para registrar un vehículo
def registrar_vehiculo():
    if len(vehiculos_estacionados) >= CAPACIDAD_MAXIMA:
        print("PARQUEADERO LLENO")
        return

    placa = input("Ingrese la placa del vehículo: ")
    tipo = input("Ingrese el tipo de vehículo (Carro/Moto): ")
    hora_entrada = input("Ingrese la hora de entrada (HH:MM): ")

    for vehiculo in vehiculos_estacionados:
        if vehiculo['placa'] == placa:
            print("El vehículo ya está estacionado.")
            return

    vehiculo = {
        'placa': placa,
        'tipo': tipo,
        'hora_entrada': hora_entrada,
        'hora_salida': None
    }
    vehiculos_estacionados.append(vehiculo)
    print(f"Vehículo {placa} registrado exitosamente.")


# Función para registrar la salida de un vehículo
def registrar_salida():
    placa = input("Ingrese la placa del vehículo que sale: ")
    hora_salida = input("Ingrese la hora de salida (HH:MM): ")

    for vehiculo in vehiculos_estacionados:
        if vehiculo['placa'] == placa:
            vehiculo['hora_salida'] = hora_salida
            tiempo_estacionado = calcular_tiempo(vehiculo['hora_entrada'], hora_salida)
            print(f"Vehículo {placa} ha salido. Tiempo estacionado: {tiempo_estacionado:.2f} horas.")
            vehiculos_estacionados.remove(vehiculo)
            return

    print("El vehículo no está estacionado.")


# Función para calcular el tiempo de estancia
def calcular_tiempo(hora_entrada, hora_salida):
    entrada = datetime.strptime(hora_entrada, "%H:%M")
    salida = datetime.strptime(hora_salida, "%H:%M")
    tiempo = (salida - entrada).seconds / 3600  # Convertir a horas
    return tiempo


# Función para visualizar vehículos estacionados
def visualizar_vehiculos():
    if not vehiculos_estacionados:
        print("No hay vehículos estacionados.")
        return

    for vehiculo in vehiculos_estacionados:
        print(
            f"Placa: {vehiculo['placa']}, Tipo: {vehiculo['tipo']}, Hora de entrada: {vehiculo['hora_entrada']}, Hora de salida: {vehiculo['hora_salida'] if vehiculo['hora_salida'] else 'Aún estacionado'}")


# Menú principal
def menu():
    while True:
        print("\n--- Sistema de Administración de Parqueadero ---")
        print("1. Registrar vehículo")
        print("2. Registrar salida")
        print("3. Visualizar vehículos estacionados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_vehiculo()
        elif opcion == '2':
            registrar_salida()
        elif opcion == '3':
            visualizar_vehiculos()
        elif opcion == '4':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el menú
menu()