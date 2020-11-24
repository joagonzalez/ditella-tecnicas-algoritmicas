class Casillero:
  def __init__(self, fil, col):
    self.fil = fil
    self.col = col

  def __repr__(self):
    return "(" + str(self.fil) + "," + str(self.col) + ")"

class Tablero:
  # Crea un tablero de NxN.
  def __init__(self, n):
    self.tab = []
    self.tam = n
    self.cant_reinas = 0
    for i in range(self.tam):
      fila = []
      for j in range(self.tam):
        fila.append(0)
      self.tab.append(fila)  

  # Devuelve la cantidad de filas/columnas del tablero.
  def tamaño(self):
    return self.tam

  # Dice si el casillero c esta amenazado por una reina.
  # PRE: self.enRango(c).
  def amenazado(self, c):
    return self.tab[c.fil][c.col] != 0

  # Devuelve la cantidad de reinas en el tablero.
  def cantidadDeReinas(self):
    return self.cant_reinas

  # Dice si en el casillero c hay una reina.
  # PRE: self.enRango(c).
  def hayReina(self, c):
    return self.tab[c.fil][c.col] == 'Q'

  # Pone una reina en el casillero c.
  # PRE: self.enRango(c) and not self.amenazado(c).
  def ponerReina(self, c):
    self.cant_reinas += 1
    # Amenazo filas y columnas.
    for i in range(self.tam):
      self.tab[c.fil][i] += 1
      self.tab[i][c.col] += 1
    # Amenazo las 2 diagonales.
    for i in range(c.fil+c.col+1):
      if self.enRangoAux(i, c.fil+c.col-i):
        self.tab[i][c.fil+c.col-i] += 1
    for i in range(self.tam):
      if self.enRangoAux(c.fil-i, c.col-i):
        self.tab[c.fil-i][c.col-i] += 1
      if self.enRangoAux(c.fil+i, c.col+i):
        self.tab[c.fil+i][c.col+i] += 1
    # Pongo la reina
    self.tab[c.fil][c.col] = 'Q'

  # Saca una reina del casillero c.
  # PRE: self.enRango(c) and self.hayReina(c).
  def sacarReina(self, c):
    self.cant_reinas -= 1
    # Saco la reina.
    self.tab[c.fil][c.col] = 5
    # Desamenazo filas y columnas.
    for i in range(self.tam):
      self.tab[c.fil][i] -= 1
      self.tab[i][c.col] -= 1
    # Desamenazo las 2 diagonales.
    for i in range(c.fil+c.col+1):
      if self.enRangoAux(i, c.fil+c.col-i):
        self.tab[i][c.fil+c.col-i] -= 1
    for i in range(self.tam):
      if self.enRangoAux(c.fil-i, c.col-i):
        self.tab[c.fil-i][c.col-i] -= 1
      if self.enRangoAux(c.fil+i, c.col+i):
        self.tab[c.fil+i][c.col+i] -= 1

  # Dice si (fil,col) es un casillero valido en el tablero.
  def enRangoAux(self, fil, col):
    return 0<=fil and 0<=col and fil<self.tamaño() and col<self.tamaño()

  # Dice si c es un casillero valido en el tablero.
  def enRango(self, c):
    return self.enRangoAux(c.fil, c.col)

  # Devuelve la lista de casilleros sin amenazas.
  def casillerosSinAmenazas(self):
    RV = []
    for col in range(self.tam):
      for fil in range(self.tam):
        c = Casillero(fil, col)
        if not self.amenazado(c):
          RV.append(c)
    return RV

  # Devuelve un string listando los casilleros con reinas.
  def listarReinas(self):
    RV = ""
    for col in range(self.tam):
      for fil in range(self.tam):
        c = Casillero(fil, col)
        if self.hayReina(c):
          RV = RV + str(c) + " "
    return RV
  
  # Devuelve una copia del tablero.
  def copy(self):
    copia = Tablero(self.tam)
    copia.tab = []
    for i in range(copia.tam):
      fila = self.tab[i].copy()
      copia.tab.append(fila)  
    return copia

  # Representación como string de un tablero.
  def __repr__(self):
    RV = "  "
    for i in range(self.tam):
      RV += str(i)+" "
    RV += "\n"
    for i in range(self.tam):
      RV += str(i)+" "
      for j in range(self.tam):
        RV += str(self.tab[i][j]) + " "
      RV += "\n"
    return RV

  def __eq__(self, other):
    return self.tab==other.tab

  # Hash de un tablero.
  def __hash__(self):
    h = str(self.tam)
    for col in range(self.tam):
      for fil in range(self.tam):
        c = self.tab[fil][col]
        h += str(c if c!='Q' else 100)
    return int(h)

