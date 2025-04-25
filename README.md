# Simulación de Sistema Hospitalario Automatizado

Este proyecto es una simulación realista de un sistema hospitalario que emplea **programación paralela, concurrente y asíncrona** para modelar el flujo de pacientes en distintas etapas: **registro**, **diagnóstico**, **asignación de recursos** y **alta médica**.

---

##  Objetivo

Demostrar la aplicación y diferencias entre los paradigmas de programación:
- **Concurrente**: múltiples pacientes en hilos compartiendo recursos.
- **Paralelo**: procesamiento intensivo simulado con procesos separados.
- **Asíncrono**: operaciones simuladas de entrada/salida no bloqueantes.

---

##  Etapas del Sistema

1. **Registro** (asíncrono con `asyncio`)
2. **Diagnóstico automatizado** (paralelo con `multiprocessing`)
3. **Asignación de recursos limitados** (concurrente con `threading.Semaphore`)
4. **Seguimiento y alta médica** (asíncrono)

---

##  Tecnologías y Librerías

- Python 3.10+
- `asyncio`
- `threading`
- `multiprocessing`
- `random`, `time`
- `colorama` (interfaz en consola)
- `logging` (registro en archivo)

---

##  Ejecución del Proyecto

1. Clona el repositorio:
    ```bash
        git clone https://github.com/Robert2803tit/simulacion_hospitalaria.git

2. Activa el entorno virtual
   ```b́ash
         source venv/bin/activate  # o .\venv\Scripts\activate en Windows
   
3. Instala dependencias:
   ```bash
           pip install colorama

4. Ejecuta la simulación:
     ```b̀ash 
           python3 hospital_sim.py

## Resultados

La simulación maneja múltiples pacientes simultáneamente, con tiempos de procesamiento variables, mostrando cómo se sincronizan recursos y se aprovechan los distintos paradigmas.

## Informe 

en el archivo **Reporte.pdf** se explica mas a detalle la practica       
       
