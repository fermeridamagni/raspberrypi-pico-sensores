# Autor: @fermeridamagni - https://fermeridamagni.me

# Este código permite controlar las luces de una casa mediante sensores de movimiento y un Raspberry Pi Pico.
# Los sensores de movimiento están conectados a los pines 2, 3 y 4 del Raspberry Pi Pico.
# Las luces de la cocina, sala y dormitorio están conectadas a los pines 5, 6 y 7 respectivamente.
# Cuando un sensor de movimiento detecta movimiento, se encienden las luces de la habitación correspondiente.
# Si no se detecta movimiento, las luces se apagan.

import time  # Para introducir pausas en el código

from controllers.lights import encender_luces, apagar_luces
from controllers.sensors import detectar_movimiento

# Bucle principal
while True:
    if (habitacion := detectar_movimiento()) is not None:
        encender_luces(habitacion)
        print(f"¡Movimiento detectado en la {habitacion}! Luces encendidas.")
    else:
        apagar_luces("cocina")
        apagar_luces("sala")
        apagar_luces("dormitorio")
        print("Sin movimiento en ninguna habitación. Luces apagadas.")

    time.sleep(
        1
    )  # Esperamos un segundo antes de volver a comprobar los sensores de movimiento
