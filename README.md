# Mini-Proyecto: Aspiradora Inteligente

## Descripción
Este proyecto es una simulación de un agente inteligente de reflejo simple en Python. El agente (una aspiradora) opera en un entorno de dos habitaciones ("A" y "B"), evaluando su entorno en tiempo real para decidir si debe limpiar o moverse a la siguiente habitación, gestionando una batería limitada (4 horas de uso) y deteniéndose al cumplir una meta de limpieza.

## Implementación de Nuevas Instrucciones

Como parte de la actualización del agente, se integraron dos nuevas estructuras de control principales:

### 1. Instrucción: `IF SUCIO THEN {...} ELSE {...}`
Esta instrucción permite que el agente tome decisiones en tiempo real basándose en la percepción de su entorno inmediato.
* **Ubicación en el código:** Método `decidir_accion()` en la clase `Aspiradora`.
* **Funcionamiento:** El robot evalúa el estado de la habitación actual mediante el atributo `estado`. Si la lectura devuelve `HABITACION_SUCIA`, invoca el método `aspirar()`. Si la habitación ya está limpia, entra en el bloque `ELSE` e invoca el método `mover_sig_habitacion()`, optimizando así el uso de su batería.

### 2. Instrucción: `REPEAT n {...}`
Esta instrucción define el ciclo de vida y operación continua del agente, limitando sus acciones a un número finito `n`.
* **Ubicación en el código:** Método `repetir()` en la clase `Aspiradora`.
* **Funcionamiento:** Representa la cantidad de iteraciones operativas permitidas antes de la detención. En la simulación, `n` está ligado a la autonomía del agente (su batería). Durante cada iteración, el agente ejecuta la evaluación de su entorno, verifica si la meta de limpieza se ha cumplido y aplica las condiciones dinámicas del entorno (posibilidad de que las habitaciones se ensucien aleatoriamente) antes de concluir su ciclo.

## Ejecución y Casos de Prueba
Para correr la simulación, ejecuta el archivo principal en la terminal:
`python proyecto_aspiradora.py`

![Caso de prueba 1](image-3.png)

![Caso de prueba 2](image-4.png)