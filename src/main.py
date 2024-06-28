# Autor: @fermeridamagni - https://fermeridamagni.me

# Este código permite controlar las luces de una casa mediante sensores de movimiento y un Raspberry Pi Pico.
# Los sensores de movimiento están conectados a los pines 2, 3 y 4 del Raspberry Pi Pico.
# Las luces de la cocina, sala y dormitorio están conectadas a los pines 5, 6 y 7 respectivamente.
# Cuando un sensor de movimiento detecta movimiento, se encienden las luces de la habitación correspondiente.
# Si no se detecta movimiento, las luces se apagan.

import machine  # Para interactuar con los pines del Raspberry Pi Pico
import time  # Para introducir pausas en el código

# Configuración de los pines
pin_sensor_movimiento_cocina = machine.Pin(
    2, machine.Pin.IN
)  # Pin 2 como entrada para el sensor de movimiento de la cocina
pin_sensor_movimiento_sala = machine.Pin(
    3, machine.Pin.IN
)  # Pin 3 como entrada para el sensor de movimiento de la sala
pin_sensor_movimiento_dormitorio = machine.Pin(
    4, machine.Pin.IN
)  # Pin 4 como entrada para el sensor de movimiento del dormitorio

pin_luces_cocina = machine.Pin(
    5, machine.Pin.OUT
)  # Pin 5 como salida para las luces de la cocina
pin_luces_sala = machine.Pin(
    6, machine.Pin.OUT
)  # Pin 6 como salida para las luces de la sala
pin_luces_dormitorio = machine.Pin(
    7, machine.Pin.OUT
)  # Pin 7 como salida para las luces del dormitorio


# Función para encender las luces de una habitación
def encender_luces(habitacion):
    if habitacion == "cocina":
        pin_luces_cocina.value(1)  # Enciende las luces de la cocina

    elif habitacion == "sala":
        pin_luces_sala.value(1)  # Enciende las luces de la sala

    elif habitacion == "dormitorio":
        pin_luces_dormitorio.value(1)  # Enciende las luces del dormitorio


# Función para apagar las luces de una habitación
def apagar_luces(habitacion):
    if habitacion == "cocina":
        pin_luces_cocina.value(0)  # Apaga las luces de la cocina

    elif habitacion == "sala":
        pin_luces_sala.value(0)  # Apaga las luces de la sala

    elif habitacion == "dormitorio":
        pin_luces_dormitorio.value(0)  # Apaga las luces del dormitorio


# Bucle principal
while True:
    if (
        pin_sensor_movimiento_cocina.value() == 1
    ):  # Si el sensor de la cocina detecta movimiento
        encender_luces("cocina")  # Encendemos las luces de la cocina
        print(
            "¡Movimiento detectado en la cocina! Luces encendidas."
        )  # Mostramos un mensaje en la consola

    else:
        apagar_luces("cocina")  # Apagamos las luces de la cocina
        print(
            "Sin movimiento en la cocina. Luces apagadas."
        )  # Mostramos un mensaje en la consola

    if (
        pin_sensor_movimiento_sala.value() == 1
    ):  # Si el sensor de la sala detecta movimiento
        encender_luces("sala")  # Encendemos las luces de la sala
        print(
            "¡Movimiento detectado en la sala! Luces encendidas."
        )  # Mostramos un mensaje en la consola

    else:
        apagar_luces("sala")  # Apagamos las luces de la sala
        print(
            "Sin movimiento en la sala. Luces apagadas."
        )  # Mostramos un mensaje en la consola

    if (
        pin_sensor_movimiento_dormitorio.value() == 1
    ):  # Si el sensor del dormitorio detecta movimiento
        encender_luces("dormitorio")  # Encendemos las luces del dormitorio
        print(
            "¡Movimiento detectado en el dormitorio! Luces encendidas."
        )  # Mostramos un mensaje en la consola

    else:
        apagar_luces("dormitorio")  # Apagamos las luces del dormitorio
        print(
            "Sin movimiento en el dormitorio. Luces apagadas."
        )  # Mostramos un mensaje en la consola

    time.sleep(
        1
    )  # Esperamos un segundo antes de volver a comprobar los sensores de movimiento
