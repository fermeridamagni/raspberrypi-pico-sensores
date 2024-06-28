import machine  # Para interactuar con los pines del Raspberry Pi Pico

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
