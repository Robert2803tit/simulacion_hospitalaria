import asyncio
import threading
import multiprocessing
import time
import random

# ---------- ASÍNCRONO: REGISTRO Y ALTA ----------
async def registro_paciente(nombre):
    print(f" Registrando a {nombre}...")
    await asyncio.sleep(random.uniform(0.5, 1.5))
    print(f" {nombre} registrado.")

async def seguimiento_alta(nombre):
    await asyncio.sleep(random.uniform(1, 2))
    print(f" {nombre} fue dado de alta.")

# ---------- PARALELISMO: DIAGNÓSTICO ----------
def diagnostico(nombre):
    print(f" Diagnóstico para {nombre} en curso...")
    time.sleep(random.uniform(2, 4))  # procesamiento intensivo
    print(f" Diagnóstico de {nombre} finalizado.")

# ---------- CONCURRENCIA: ASIGNACIÓN DE RECURSOS ----------
camas_disponibles = threading.Semaphore(3)

def asignar_recursos(nombre):
    print(f" {nombre} esperando cama...")
    with camas_disponibles:
        print(f" {nombre} asignado a cama.")
        time.sleep(random.uniform(1, 2))
        print(f" {nombre} dejó la cama disponible.")

# ---------- FLUJO COMPLETO POR PACIENTE ----------
def flujo_paciente(nombre):
    asyncio.run(registro_paciente(nombre))
    
    p = multiprocessing.Process(target=diagnostico, args=(nombre,))
    p.start()

    asignar_recursos(nombre)
    p.join()

    asyncio.run(seguimiento_alta(nombre))

# ---------- INICIO DE SIMULACIÓN ----------
if __name__ == "__main__":
    pacientes = [f"Paciente-{i+1}" for i in range(5)]
    hilos = []

    for nombre in pacientes:
        hilo = threading.Thread(target=flujo_paciente, args=(nombre,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print(" Simulación hospitalaria finalizada.")
