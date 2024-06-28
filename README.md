# Control de Luces con Raspberry Pi Pico y Sensores de Movimiento

Este proyecto permite controlar las luces de una casa mediante sensores de movimiento y un Raspberry Pi Pico. Los sensores de movimiento están conectados a los pines 2, 3 y 4 del Raspberry Pi Pico, mientras que las luces de la cocina, sala y dormitorio están conectadas a los pines 5, 6 y 7, respectivamente.

## Funcionamiento

- Cuando un sensor de movimiento detecta movimiento, se encienden las luces de la habitación correspondiente.
- Si no se detecta movimiento, las luces se apagan.

## Estructura

```

└── 📁raspberrypi-pico-sensores

    └── .gitignore

    └── 📁.vscode

    └── README.md

    └── 📁src

        └── config.py

        └── 📁controllers

            └── lights.py

            └── sensors.py

        └── main.py

```
