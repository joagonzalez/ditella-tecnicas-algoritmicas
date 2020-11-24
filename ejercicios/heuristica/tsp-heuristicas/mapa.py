class Mapa:
  # Crea un nuevo mapa.
  def __init__(self):   
    self.ciudades = set()
    self.caminos = {}

  # Representación como string de un Mapa.
  def __repr__(self):
    res = "ciudades:" + str(self.ciudades) + "\n"
    res += "caminos:" + str(self.caminos)
    return res

  # Dice si una ciudad está definida en el mapa.
  def existe_ciudad(self, c):
    return c in self.ciudades

  # Agrega una ciudad al mapa.
  # Pre: not self.existe_ciudad(ciudad)
  def agregar_ciudad(self, c):
    self.ciudades.add(c)

  # Agrega al mapa un camino entre dos ciudades c1 y c2, con una
  # distancia asociada.
  # Los caminos no tienen sentido (van de c1 a c2 y viceversa).
  # Pre: self.existe_ciudad(c1) and self.existe_ciudad(c2) and c1!=c2
  def agregar_camino(self, c1, c2, distancia):
    if c1 < c2: 
      self.caminos[(c1,c2)] = distancia
    else:
      self.caminos[(c2,c1)] = distancia

  # Devuelve la distancia del camino directo entre un par de ciudades.
  # Los caminos no tienen sentido (van de c1 a c2 y viceversa).
  # Si no hay un camino definido entre ambas, devuelve infinito.
  # Pre: self.existe_ciudad(cd) and self.existe_ciudad(c2)
  def obtener_distancia(self, c1, c2):
    if (c1,c2) in self.caminos:
      res = self.caminos[(c1,c2)]
    elif (c2,c1) in self.caminos:
      res = self.caminos[(c2,c1)]
    else:
      res = float('inf')
    return res

  # Devuelve una copia de las ciudades del mapa.
  def obtener_ciudades(self):
    return self.ciudades.copy()

  # Dada una lista de ciudades (todas definidas en el mapa), devuelve
  # la suma de las distancias desde la primera ciudad hasta la última.
  def distancia_de_recorrido(self, recorrido):
    res = 0.0
    for i in range(len(recorrido)-1):
      res += self.obtener_distancia(recorrido[i], recorrido[i+1])
    return res

