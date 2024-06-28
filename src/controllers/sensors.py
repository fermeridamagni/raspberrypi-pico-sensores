# Description: Controlador para los sensores de movimiento de las habitaciones
from config import (
    pin_sensor_movimiento_sala,
    pin_sensor_movimiento_cocina,
    pin_sensor_movimiento_dormitorio,
)


def detectar_movimiento():  # Función para detectar movimiento en las habitaciones
    if (
        pin_sensor_movimiento_cocina.value() == 1
    ):  # Si el sensor de movimiento de la cocina detecta movimiento
        return "cocina"
    elif (
        pin_sensor_movimiento_sala.value() == 1
    ):  # Si el sensor de movimiento de la sala detecta movimiento
        return "sala"
    elif (
        pin_sensor_movimiento_dormitorio.value() == 1
    ):  # Si el sensor de movimiento del dormitorio detecta movimiento
        return "dormitorio"
    else:
        return None  # Si no se detecta movimiento en ninguna habitación
