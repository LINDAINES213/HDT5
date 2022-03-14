################################################
# Universidad del Valle de Guatemala
# Linda Inés Jiménez Vides - 21169
# 11 de marzo de 2022
################################################

import simpy
import random

def simulacion(env, proceso_simulacion, RAM, CPU, duracion_simulacion, tiempo_simulacion): #Simulacion del Proceso

    
    yield env.timeout(tiempo_simulacion) # Ciclo de reloj del procesdor
    tiempo_inicial = env.now # Tiempo inicial del Proceso

    print('%s iniciando simulacion en %d' % (proceso_simulacion, env.now)) # Inicio de la simulacion de los procesos
    
    with CPU.request() as req: # Pide el procesador
        yield req

        print('%s empezando proceso en %s' % (proceso_simulacion, env.now)) # Inicio de los procesos
        yield env.timeout(duracion_simulacion)
        print('%s terminando proceso en %s' % (proceso_simulacion, env.now)) # Fin de los procesos 
        tiempo_final = env.now - tiempo_inicial # Tiempo final de cada proceso
        global total_simulacion     
        total_simulacion += tiempo_final #Tiempo total de la simulacion
        print('%s tardo %f' % (proceso_simulacion, env.now))

env = simpy.Environment() # Ambiente de simulacion
CPU = simpy.Resource(env, capacity = 1) # Creacion del procesador con cierta capacidad
RAM = simpy.Container(env, init = 100, capacity = 100) # Container de la RAM
intervalo = 10
cantidad_procesos = 25 # Cantidad de procesos a generad
total_simulacion = 0

for i in range(cantidad_procesos):
    env.process(simulacion(env, 'Proceso %d' % i, RAM, CPU, random.expovariate(1.0/intervalo), i))
    
env.run() # Corre la simulacion
print('Tiempo promedio %d' % (total_simulacion / cantidad_procesos))