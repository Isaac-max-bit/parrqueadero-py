import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Capacidad máxima del parqueadero
CAPACIDAD_MAXIMA = 10
vehiculos_estacionados = []


# Función para registrar un vehículo
def registrar_vehiculo():
    if len(vehiculos_estacionados) >= CAPACIDAD_MAXIMA:
        messagebox.showerror("Error", "PARQUEADERO LLENO")
        return

    placa = entrada_placa.get().upper()
    tipo = entrada_tipo.get()
    hora_entrada = entrada_hora_entrada.get()

    if not placa or not tipo or not hora_entrada:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    for vehiculo in vehiculos_estacionados:
        if vehiculo['placa'] == placa:
            messagebox.showerror("Error", "El vehículo ya está estacionado")
            return

    vehiculo = {
        'placa': placa,
        'tipo': tipo,
        'hora_entrada': hora_entrada,
        'hora_salida': None
    }
    vehiculos_estacionados.append(vehiculo)
    messagebox.showinfo("Éxito", f"Vehículo {placa} registrado correctamente")
    limpiar_campos()


# Función para registrar la salida de un vehículo
def registrar_salida():
    placa = entrada_placa.get().upper()
    hora_salida = entrada_hora_salida.get()

    if not placa or not hora_salida:
        messagebox.showwarning("Advertencia", "Ingrese la placa y la hora de salida")
        return

    for vehiculo in vehiculos_estacionados:
        if vehiculo['placa'] == placa:
            vehiculo['hora_salida'] = hora_salida
            tiempo_estacionado = calcular_tiempo(vehiculo['hora_entrada'], hora_salida)
            messagebox.showinfo("Salida registrada",
                                f"Vehículo {placa} ha salido.\nTiempo estacionado: {tiempo_estacionado:.2f} horas.")
            vehiculos_estacionados.remove(vehiculo)
            limpiar_campos()
            return

    messagebox.showerror("Error", "El vehículo no está estacionado")


# Función para calcular el tiempo de estancia
def calcular_tiempo(hora_entrada, hora_salida):
    entrada = datetime.strptime(hora_entrada, "%H:%M")
    salida = datetime.strptime(hora_salida, "%H:%M")
    tiempo = (salida - entrada).seconds / 3600  # Convertir a horas
    return tiempo


# Función para visualizar vehículos estacionados
def visualizar_vehiculos():
    if not vehiculos_estacionados:
        messagebox.showinfo("Vehículos", "No hay vehículos estacionados.")
        return

    mensaje = "Vehículos estacionados:\n"
    for vehiculo in vehiculos_estacionados:
        mensaje += f"Placa: {vehiculo['placa']} | Tipo: {vehiculo['tipo']} | Entrada: {vehiculo['hora_entrada']}\n"

    messagebox.showinfo("Vehículos Estacionados", mensaje)


# Función para limpiar los campos de entrada
def limpiar_campos():
    entrada_placa.delete(0, tk.END)
    entrada_tipo.delete(0, tk.END)
    entrada_hora_entrada.delete(0, tk.END)
    entrada_hora_salida.delete(0, tk.END)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Parqueadero")
ventana.geometry("400x400")

# Etiquetas y entradas
tk.Label(ventana, text="Placa del vehículo:").pack()
entrada_placa = tk.Entry(ventana)
entrada_placa.pack()

tk.Label(ventana, text="Tipo de vehículo (Carro/Moto):").pack()
entrada_tipo = tk.Entry(ventana)
entrada_tipo.pack()

tk.Label(ventana, text="Hora de entrada (HH:MM):").pack()
entrada_hora_entrada = tk.Entry(ventana)
entrada_hora_entrada.pack()

tk.Label(ventana, text="Hora de salida (HH:MM):").pack()
entrada_hora_salida = tk.Entry(ventana)
entrada_hora_salida.pack()

# Botones
tk.Button(ventana, text="Registrar Vehículo", command=registrar_vehiculo).pack(pady=5)
tk.Button(ventana, text="Registrar Salida", command=registrar_salida).pack(pady=5)
tk.Button(ventana, text="Ver Vehículos Estacionados", command=visualizar_vehiculos).pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
