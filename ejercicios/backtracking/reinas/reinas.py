import sys
from tablero import Casillero,Tablero

#####

def Reinas(tablero):
  if tablero.cantidadDeReinas() < tablero.tamaño():
    caSinAm = tablero.casillerosSinAmenazas()

    # Optimización: alcanza con considerar los casilleros de una columna.
    caSinAm = [c for c in caSinAm if c.col==tablero.cantidadDeReinas()]

    for c in caSinAm:
      tablero.ponerReina(c)     # avanzar un paso
      Reinas(tablero)           # seguir buscando recursivamente
      tablero.sacarReina(c)     # retroceder un paso
  else:
    # Caso base: logramos colocar todas las reinas.
    # Agregamos una copia del tablero en el conjunto de soluciones.
    soluciones.add(tablero.copy())

#####

# Leemos el tamaño del tablero como argumento del programa.
tamaño = int(sys.argv[1])  # Ej: 8 para un tablero de 8x8

soluciones = set()  # ATENCIÓN (*)
Reinas(Tablero(tamaño))
for tablero_solucion in soluciones:
  print(tablero_solucion.listarReinas())

#####

# (*) Este programa usa una variable global 'soluciones', en donde
# se van copiando las soluciones encontradas. El uso de variables
# globales es una práctica fuertemente desaconsejada, porque atenta
# contra la claridad del código y hace más difícil seguir la ejecución.
# Hacemos esta excepción para ayudar a entender el algoritmo backtracking
# de Reinas. Una vez entendido, ver en la versión reinas2.py cómo puede
# evitarse el uso de variables globales con inmersión de parámetros.

