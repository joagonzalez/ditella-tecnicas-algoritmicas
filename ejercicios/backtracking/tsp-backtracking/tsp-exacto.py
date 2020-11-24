from mapa import Mapa

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

  import random
  random.seed(1)
  mapa2 = Mapa()
  ciudades = list('abcdefghij')
  for x in ciudades:
    mapa2.agregar_ciudad(x)
  for x in ciudades:
    for y in ciudades:
      if x<y:
        mapa2.agregar_camino(x, y, random.randint(1, 100))

  recorrido = tsp_exhaustivo(mapa1, 'a')
  print(recorrido, mapa1.distancia_de_recorrido(recorrido))
    
  recorrido = tsp_exhaustivo(mapa2, 'a')
  print(recorrido, mapa2.distancia_de_recorrido(recorrido))

