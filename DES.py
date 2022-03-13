################################################
# Universidad del Valle de Guatemala
# Linda Inés Jiménez Vides - 21169
# 11 de marzo de 2022
################################################

import simpy
import random

def simulacion(env, proceso_simulacion, RAM, CPU, duracion_simulacion, tiempo_simulacion):
    
    yield env.timeout(tiempo_simulacion)
    tiempo_inicial = env.now

    print('%s iniciando simulacion en %d' % (proceso_simulacion, env.now))
    
    with CPU.request() as req:
        yield req

        print('%s empezando proceso en %s' % (proceso_simulacion, env.now))
        yield env.timeout(duracion_simulacion)
        print('%s terminando proceso en %s' % (proceso_simulacion, env.now))
        tiempo_final = env.now - tiempo_inicial
        global total_simulacion     
        total_simulacion += tiempo_final
        print('%s tardo %f' % (proceso_simulacion, env.now))

env = simpy.Environment()
CPU = simpy.Resource(env, capacity = 1)
RAM = simpy.Container(env, init = 200, capacity = 200)
intervalo = 1
cantidad_procesos = 200
total_simulacion = 0

for i in range(cantidad_procesos):
    env.process(simulacion(env, 'Proceso %d' % i, RAM, CPU, random.expovariate(1.0/intervalo), i))
    
env.run()
print('Tiempo promedio %d' % (total_simulacion / cantidad_procesos))