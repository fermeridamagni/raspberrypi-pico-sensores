# Control de Luces con Raspberry Pi Pico y Sensores de Movimiento

Este proyecto permite controlar las luces de una casa mediante sensores de movimiento y un Raspberry Pi Pico. Los sensores de movimiento están conectados a los pines 2, 3 y 4 del Raspberry Pi Pico, mientras que las luces de la cocina, sala y dormitorio están conectadas a los pines 5, 6 y 7, respectivamente.

## Funcionamiento

- Cuando un sensor de movimiento detecta movimiento, se encienden las luces de la habitación correspondiente.
- Si no se detecta movimiento, las luces se apagan.

## Código

```python
import machine
import time

# Configuración de los pines
pin_sensor_movimiento_cocina = machine.Pin(2, machine.Pin.IN)
pin_sensor_movimiento_sala = machine.Pin(3, machine.Pin.IN)
pin_sensor_movimiento_dormitorio = machine.Pin(4, machine.Pin.IN)

pin_luces_cocina = machine.Pin(5, machine.Pin.OUT)
pin_luces_sala = machine.Pin(6, machine.Pin.OUT)
pin_luces_dormitorio = machine.Pin(7, machine.Pin.OUT)

# Función para encender las luces de una habitación
def encender_luces(habitacion):
    if habitacion == "Cocina":
        pin_luces_cocina.value(1)
    elif habitacion == "Sala":
        pin_luces_sala.value(1)
    elif habitacion == "Dormitorio":
        pin_luces_dormitorio.value(1)

# Función para apagar las luces de una habitación
def apagar_luces(habitacion):
    if habitacion == "Cocina":
        pin_luces_cocina.value(0)
    elif habitacion == "Sala":
        pin_luces_sala.value(0)
    elif habitacion == "Dormitorio":
        pin_luces_dormitorio.value(0)

# Bucle principal
while True:
    if pin_sensor_movimiento_cocina.value() == 1:
        encender_luces("Cocina")
        print("¡Movimiento detectado en la cocina! Luces encendidas.")
    else:
        apagar_luces("Cocina")
        print("Sin movimiento en la cocina. Luces apagadas.")

    if pin_sensor_movimiento_sala.value() == 1:
        encender_luces("Sala")
        print("¡Movimiento detectado en la sala! Luces encendidas.")
    else:
        apagar_luces("Sala")
        print("Sin movimiento en la sala. Luces apagadas.")

    if pin_sensor_movimiento_dormitorio.value() == 1:
        encender_luces("Dormitorio")
        print("¡Movimiento detectado en el dormitorio! Luces encendidas.")
    else:
        apagar_luces("Dormitorio")
        print("Sin movimiento en el dormitorio. Luces apagadas.")

    time.sleep(1)
```
