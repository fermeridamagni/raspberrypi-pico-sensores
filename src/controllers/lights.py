# Descripción: Controlador para el manejo de las luces de una habitación
from config import (
    pin_luces_cocina,
    pin_luces_dormitorio,
    pin_luces_sala,
)


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
