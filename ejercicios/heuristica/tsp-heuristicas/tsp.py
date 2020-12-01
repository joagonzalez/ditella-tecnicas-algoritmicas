from mapa import Mapa
import datetime
import random
random.seed(1)  # Fijo una semilla para obtener los mismos resultados entre
                # una ejecución y la siguiente.

#######################################################################

# TSP con algoritmo de búsqueda exhaustivo (exponencial).
# El recorrido debe empezar y terminar en la ciudad indicada.
def tsp_exhaustivo(mapa, ciudad):
  cs = mapa.obtener_ciudades()
  cs.remove(ciudad) # ciudades que resta visitar
  return tsp_exhaustivo_aux(mapa, cs, [ciudad])

# Función auxiliar de TSP exhaustivo por backtracking.
# ciudades_faltantes es un conjunto de ciudades que aún no se visitaron.
# recorrido_actual es la lista de ciudades visitadas hasta ahora.
# Obs: El recorrido debe terminar en recorrido_actual[0] (la primera
# ciudad).
def tsp_exhaustivo_aux(mapa, ciudades_faltantes, recorrido_actual):
  mejor_recorrido = None
  menor_distancia = float('inf')  # infinito
  
  if len(ciudades_faltantes)==0:
    # Caso base: terminamos de visitar las ciudades.
    # Devolvemos el recorrido actual (luego de agregarle la vuelta a la
    # ciudad de origen) como el mejor recorrido encontrado en esta rama
    # de la búsqueda.
    mejor_recorrido = recorrido_actual.copy()
    mejor_recorrido.append(recorrido_actual[0])
  else:
    # Todavía quedan ciudades por visitar, hacemos BT una por una.
    for c in ciudades_faltantes.copy():  
                      # Obs: Hacemos .copy() porque vamos a modificar
                      #      ciudades_faltantes en el cuerpo del ciclo.
                      #      Sin .copy(), Python daría error.
      # Paso para adelante.
      recorrido_actual.append(c)
      ciudades_faltantes.remove(c)
      
      # 're' es el mejor recorrido encontrado recursivamente si seguimos
      # el recorrido actual por la ciudad c.
      re = tsp_exhaustivo_aux(mapa, ciudades_faltantes, recorrido_actual)
      di = mapa.distancia_de_recorrido(re)

      # Si el recorrido 're' es el de menor distancia (hasta ahora), 
      # lo recordamos.
      if di < menor_distancia:
        mejor_recorrido = re
        menor_distancia = di

      # Paso para atrás.
      ciudades_faltantes.add(c)
      recorrido_actual.pop()

  return mejor_recorrido

#######################################################################

# TSP con algoritmo greedy.
def tsp_greedy(mapa, ciudad):
  ciudades_faltantes = list(mapa.obtener_ciudades())
  ciudades_faltantes.remove(ciudad)
  # Empiezo el recorrido por la ciudad indicada.
  recorrido_actual = [ciudad]
  while len(ciudades_faltantes) > 0:
    # Busco la ciudad mas cercana a la última del recorrido.
    ciudad_mas_cercana = ciudades_faltantes[0]
    for c in ciudades_faltantes[1:]:
      ultima_ciudad = recorrido_actual[-1]
      if mapa.obtener_distancia(ultima_ciudad, c) < \
         mapa.obtener_distancia(ultima_ciudad, ciudad_mas_cercana):
        ciudad_mas_cercana = c
    # Agrego la ciudad mas cercana al recorrido y la saco de las
    # ciudades que falta recorrer.
    recorrido_actual.append(ciudad_mas_cercana)
    ciudades_faltantes.remove(ciudad_mas_cercana)
  # Termino el recorrido por la ciudad indicada.
  recorrido_actual.append(ciudad)
  return recorrido_actual

#######################################################################

# TSP con algoritmo de búsqueda local, empezando desde una solución random
# si inicial=='random', o desde una solución greedy si inicial=="greedy".
def tsp_busqueda_local(mapa, ciudad, inicial):
  if inicial=="random":
    rec_actual = tsp_aleatorio(mapa, ciudad)
  else:
    rec_actual = tsp_greedy(mapa, ciudad)
  distancia_rec_actual = mapa.distancia_de_recorrido(rec_actual)
  pudimos_mejorar = True
  while pudimos_mejorar:
    # Busco al mejor recorrido 'vecino' del recorrido actual.
    # Los vecinos son todas las formas posibles de invertir pares de
    # posiciones en el recorrido (excluyendo la primera y ultima ciudad).
    distancia_mejor_vecino = float('inf')
    mejor_vecino = None
    for i in range(1, len(rec_actual)-2):
      for j in range(i+1, len(rec_actual)-1):
        vecino = rec_actual.copy()
        vecino[i],vecino[j] = vecino[j],vecino[i] # swap de ciudades
        distancia = mapa.distancia_de_recorrido(vecino)
        if distancia < distancia_mejor_vecino:
          distancia_mejor_vecino = distancia
          mejor_vecino = vecino
    
    # Si el mejor vecino encontrado es mejor que la solución actual,
    # lo guardamos y seguimos buscando. Si no, terminamos.
    if distancia_mejor_vecino < distancia_rec_actual:
      pudimos_mejorar = True
      rec_actual = mejor_vecino
      distancia_rec_actual = distancia_mejor_vecino
    else:
      pudimos_mejorar = False
  return rec_actual

#######################################################################

# TSP con una algoritmo puramente aleatorio.
def tsp_aleatorio(mapa, ciudad):
  ciudades = list(mapa.obtener_ciudades())  # obtengo todas las ciudades
  ciudades.remove(ciudad)             # saco la ciudad de origen/destino
  random.shuffle(ciudades)            # desordeno al resto al azar
  recorrido = [ciudad] + ciudades + [ciudad]  # agrego origen y destino
  return recorrido

#######################################################################

# TSP con algoritmo de búsqueda local iterativa, (empezando desde una
# solución aleatoria en cada iteración).
def tsp_busqueda_local_iterativa(mapa, ciudad):
  mejor_recorrido = None
  mejor_distancia = float('inf')  # infinito

  MAX_ITERACIONES = 1000 # criterio de corte

  for _ in range(MAX_ITERACIONES):
    rec_actual = tsp_busqueda_local(mapa, ciudad, 'random')
    
    # Si es la mejor solucion encontrada hasta ahora, recordarla:
    distancia_rec_actual = mapa.distancia_de_recorrido(rec_actual)
    if distancia_rec_actual < mejor_distancia:
      mejor_recorrido = rec_actual
      mejor_distancia = distancia_rec_actual

  return mejor_recorrido

#######################################################################

# Devuelve un recorrido que empieza y termina en la ciudad dada,
# pasando exactamente una vez por cada ciudad del mapa.
# Usa el algoritmo de búsqueda indicado: 'exhaustivo', 'greedy', 
# 'búsqueda local'.
def tsp(mapa, ciudad, algoritmo='exhaustivo'):
  if algoritmo=='exhaustivo':
    res = tsp_exhaustivo(mapa,ciudad)
  elif algoritmo=='aleatorio': 
    res = tsp_aleatorio(mapa, ciudad)
  elif algoritmo=='greedy': 
    res = tsp_greedy(mapa, ciudad)
  elif algoritmo=='búsqueda local':
    res = tsp_busqueda_local(mapa, ciudad, 'greedy')
  elif algoritmo=='búsqueda local iterativa':
    res = tsp_busqueda_local_iterativa(mapa, ciudad)
  else:
    res = None
  return res    

#######################################################################

# Dada una lista de ciudades, arma un mapa con distancias aleatorias 
# entre cada par de ciudades.
def mapa_aleatorio(ciudades):
  m = Mapa()
  for x in ciudades:
    m.agregar_ciudad(x)
  for x in ciudades:
    for y in ciudades:
      if x<y:
        m.agregar_camino(x, y, random.randint(1, 100))
  return m

#######################################################################

if __name__=="__main__":
  mapa1 = Mapa()
  mapa1.agregar_ciudad('a')
  mapa1.agregar_ciudad('b')
  mapa1.agregar_ciudad('c')
  mapa1.agregar_ciudad('d')
  mapa1.agregar_ciudad('e')
  mapa1.agregar_camino('a', 'b', 2)
  mapa1.agregar_camino('a', 'c', 5)
  mapa1.agregar_camino('a', 'd', 1)
  mapa1.agregar_camino('a', 'e', 3)
  mapa1.agregar_camino('b', 'c', 1)
  mapa1.agregar_camino('b', 'd', 3)
  mapa1.agregar_camino('b', 'e', 9)
  mapa1.agregar_camino('c', 'd', 1)
  mapa1.agregar_camino('c', 'e', 4)
  mapa1.agregar_camino('d', 'e', 2)

  mapa2 = mapa_aleatorio(list('abcdefghi'))

  mapa3 = mapa_aleatorio(list('abcdefghijk'))

  for m in (mapa1, mapa2, mapa3):
    for alg in ['exhaustivo', 'aleatorio', 'greedy', 'búsqueda local', 'búsqueda local iterativa']:
      comienzo = datetime.datetime.now()
      recorrido = tsp(m, 'a', algoritmo=alg)
      tiempo = datetime.datetime.now() - comienzo
      print(alg.ljust(25), str(m.distancia_de_recorrido(recorrido)).rjust(8), tiempo, recorrido)
    print()
