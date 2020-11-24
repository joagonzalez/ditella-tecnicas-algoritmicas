import sys
from tablero import Casillero,Tablero

#####

def Reinas(tablero, sols):
  if tablero.cantidadDeReinas() < tablero.tamaño():
    caSinAm = tablero.casillerosSinAmenazas()

    # Optimización: alcanza con considerar los casilleros de una columna.
    caSinAm = [c for c in caSinAm if c.col==tablero.cantidadDeReinas()]

    for c in caSinAm:
      tablero.ponerReina(c)     # avanzar un paso
      Reinas(tablero, sols)     # seguir buscando recursivamente
      tablero.sacarReina(c)     # retroceder un paso
  else:
    # Caso base: logramos colocar todas las reinas.
    # Agregamos una copia del tablero en el conjunto de soluciones.
    sols.add(tablero.copy())

#####

# Leemos el tamaño del tablero como argumento del programa.
tamaño = int(sys.argv[1])  # ej: 8 para un tablero de 8x8

soluciones = set()
Reinas(Tablero(tamaño), soluciones)
for tablero_solucion in soluciones:
  print('solucion: ' + str(tablero_solucion.listarReinas()))

