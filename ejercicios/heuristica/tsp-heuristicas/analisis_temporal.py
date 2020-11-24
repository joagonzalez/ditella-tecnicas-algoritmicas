from mapa import Mapa
from tsp import *
import datetime
from matplotlib import pyplot

import random
random.seed(1)

letras = 'abcdefghijklmnopqrstuvwxyz'

tamaños = [5, 6, 7, 8, 9, 10]
tiempos = []

for n in tamaños:
  # Creamos un mapa aleatorio con n ciudades
  ciudades = letras[:n]
  mapa = mapa_aleatorio(ciudades)
  print(ciudades)

  # Corremos TSP exacto, tomando nota del tiempo de ejecución.
  comienzo = datetime.datetime.now()
  recorrido = tsp_exhaustivo(mapa, 'a')
  tiempos.append((datetime.datetime.now() - comienzo).total_seconds())

# Mostramos tabla de resultados 
print()
print('n tiempo')
for (n,t) in zip(tamaños, tiempos):
  print(n, t)

# Graficamos los tiempos de ejecución en función del tamaño del mapa.
pyplot.xlabel('cantidad de ciudades')
pyplot.ylabel('tiempo de ejecución')
pyplot.plot(tamaños, tiempos, 'x-')
pyplot.show()

# Ahora con escala logarítmica
pyplot.xlabel('cantidad de ciudades')
pyplot.ylabel('log(tiempo de ejecución)')
pyplot.yscale("log")
pyplot.plot(tamaños, tiempos, 'x-')
pyplot.show()

