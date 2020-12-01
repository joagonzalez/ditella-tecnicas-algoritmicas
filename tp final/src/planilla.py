from copy import deepcopy

############################ PLANILLA ################################
        
# Encapsula una planilla donde se asignan tópicos a estudiantes.
class Planilla:
    # Para comenzar una nueva planilla, necesitamos conocer las preferencias
    # declaradas por los estudiantes.
    def __init__(self, preferencias):
        self._prefs = preferencias
        self._e2t = dict()  # Mapeo de estudiante a tópico.
        self._t2e = dict()  # Mapeo de tópico a estudiante.
        self.size =  self._prefs._cantidad

    # Metodo para saber el tamano de la clase
    # para poder encontrar soluciones vecinas
    def cantidad(self):
        return self.size

    # Metodo para retornar la solucion de esta plantilla 
    def solucion(self):
        return self._e2t

    # Asigna el tópico t al estudiante e.  
    # Si e ya tenía tópico, o si t ya estaba asignado, no hace nada.
    def asignar(self, e, t):
        if self.estudiante_libre(e) and self.topico_libre(t):
            self._e2t[e] = t
            self._t2e[t] = e
        pass
    
    # Borra la asignación del tópico t al estudiante e.  
    # Si e no tenía asignado t, no hace nada.
    def desasignar(self, e, t):
        if (not self.estudiante_libre(e)) and (self._e2t[e] == t) and \
           (not self.topico_libre(t))     and (self._t2e[t] == e):
            del self._e2t[e]
            del self._t2e[t]
        pass

    # Devuelve el conjunto de estudiantes que ya tienen tópico asignado.
    def estudiantes_con_topico(self):
        return set(self._e2t.keys())
    
    # Devuelve el conjunto de estudiantes que no tienen tópico asignado.
    def estudiantes_sin_topico(self):
        return self._prefs.estudiantes() - self.estudiantes_con_topico()
    
    # Devuelve el conjunto de tópicos que están asignados a alguien.
    def topicos_con_estudiante(self):
        return set(self._t2e.keys())
    
    # Devuelve el conjunto de tópicos que no están asignados a nadie.
    def topicos_sin_estudiante(self):
        return self._prefs.topicos() - self.topicos_con_estudiante()

    # Devuelve el tópico asignado al estudiante e. 
    # Precondición:  e in self.estudiantes_con_topico()
    def topico_asignado_a_estudiante(self, e):
        return self._e2t[e]

    # Devuelve el estudiante que tiene asignado el tópico t. 
    # Precondición:  t in self.topicos_con_estudiante()
    def estudiante_asignado_a_topico(self, t):
        return self._t2e[t]
    
    # Dice si el estudiante e está disponible para asignarle un tópico.
    def estudiante_libre(self, e):
        return (e not in self._e2t)
    
    # Dice si el tópico t está disponible para asignar a un estudiante.
    def topico_libre(self, t):
        return (t not in self._t2e)

    # Devuelve el costo de la asignación actual. 
    # Si falta asignar estudiantes, devuelve infinito.
    def calcular_costo(self):
        if len(self.estudiantes_sin_topico())==0:
            c = 0
            for e in self.estudiantes_con_topico():
                t = self._e2t[e]
                c += self._prefs.ranking_de_topico_para_estudiante(t, e)
        else:
            c = float('inf')  # infinito
        return c

    # Devuelve una representación imprimible de esta planilla.
    def __repr__(self):
        return str(self._e2t)

    # Devuelve una copia de la planilla.
    def copy(self):
        return deepcopy(self)

############################ PREFERENCIAS ##############################

# Encapsula las preferencias de tópicos declaradas por cada estudiante.
class Preferencias:
    def __init__(self, nombre):
        self._cantidad = 0    # Cantidad de estudiantes y de tópicos.
        self._prefs = dict()  # Lista de tópicos para cada estudiante, ordenados por preferencia.
                                
        if nombre == "Ejemplo3":
            self._preferencias_ejemplo3()
        elif nombre == "Ejemplo5":
            self._preferencias_ejemplo5()
        elif nombre == "Ejemplo10":
            self._preferencias_ejemplo10()
        elif nombre == "Ejemplo12":
            self._preferencias_ejemplo12()
        elif nombre == "Ejemplo15":
            self._preferencias_ejemplo15()
        elif nombre == "Ejemplo50":
            self._preferencias_ejemplo50()
        
    # Devuelve el conjunto de estudiantes de la materia.
    def estudiantes(self):
        return set(range(1, self._cantidad+1))
    
    # Devuelve el conjunto de tópicos disponibles.
    def topicos(self):
        return set(range(1, self._cantidad+1))

    # Devuelve la lista ordenada de tópicos declarados por el estudiante e.    
    def preferencias_del_estudiante(self, e):
        return self._prefs[e].copy()

    # Devuelve la posición en los tópicos del estudiante e del tópico t, tal
    # que para el primer tópico se devuelve 0, y para el último _cantidad-1.
    def ranking_de_topico_para_estudiante(self, t, e):
        return self._prefs[e].index(t)

    def __repr__(self):
        return str(self._prefs)

    def _preferencias_ejemplo3(self):
        self._cantidad = 3
        self._prefs[1] = [2,1,3]
        self._prefs[2] = [1,2,3]
        self._prefs[3] = [1,3,2]

    def _preferencias_ejemplo5(self):
        self._cantidad = 5
        self._prefs[1] = [3,1,2,4,5]
        self._prefs[2] = [4,3,1,2,5]
        self._prefs[3] = [5,1,2,3,4]
        self._prefs[4] = [1,5,4,2,3]
        self._prefs[5] = [2,1,3,4,5]

    def _preferencias_ejemplo10(self):
        self._cantidad = 10
        self._prefs[1] = [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
        self._prefs[2] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self._prefs[3] = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
        self._prefs[4] = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]
        self._prefs[5] = [4, 3, 2, 1, 5, 6, 7, 8, 9, 10]
        self._prefs[6] = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
        self._prefs[7] = [6, 5, 4, 3, 2, 1, 7, 8, 9, 10]
        self._prefs[8] = [7, 6, 5, 4, 3, 2, 1, 8, 9, 10]
        self._prefs[9] = [8, 7, 6, 5, 4, 3, 2, 1, 9, 10]
        self._prefs[10]= [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]

    def _preferencias_ejemplo12(self):
        self._cantidad = 12
        self._prefs[1] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1]
        self._prefs[2] = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2]
        self._prefs[3] = [4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3]
        self._prefs[4] = [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
        self._prefs[5] = [6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5]
        self._prefs[6] = [7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6]
        self._prefs[7] = [8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7]
        self._prefs[8] = [9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8]
        self._prefs[9] = [10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._prefs[10]= [11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self._prefs[11]= [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self._prefs[12]= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    def _preferencias_ejemplo15(self):
        self._cantidad = 15
        self._prefs[1] = [4, 13, 8, 7, 6, 9, 14, 5, 1, 15, 3, 2, 11, 12, 10]
        self._prefs[2] = [12, 14, 4, 2, 8, 6, 10, 3, 7, 9, 13, 15, 5, 1, 11]
        self._prefs[3] = [11, 2, 12, 15, 8, 9, 13, 3, 10, 7, 6, 5, 4, 14, 1]
        self._prefs[4] = [10, 15, 14, 1, 7, 4, 13, 6, 3, 9, 5, 12, 8, 11, 2]
        self._prefs[5] = [9, 10, 12, 5, 4, 1, 8, 11, 6, 3, 2, 14, 13, 15, 7]
        self._prefs[6] = [4, 15, 1, 8, 10, 11, 5, 9, 7, 12, 6, 3, 14, 2, 13]
        self._prefs[7] = [13, 15, 2, 11, 4, 9, 1, 12, 3, 6, 10, 14, 5, 7, 8]
        self._prefs[8] = [9, 2, 14, 5, 15, 10, 6, 12, 3, 8, 7, 11, 1, 4, 13]
        self._prefs[9] = [13, 4, 7, 9, 6, 8, 2, 5, 12, 1, 15, 10, 14, 11, 3]
        self._prefs[10] = [2, 10, 14, 15, 8, 1, 3, 13, 9, 11, 4, 7, 6, 12, 5]
        self._prefs[11] = [9, 3, 13, 6, 7, 5, 10, 15, 2, 1, 11, 4, 8, 14, 12]
        self._prefs[12] = [7, 13, 14, 10, 4, 2, 12, 9, 11, 6, 15, 5, 8, 1, 3]
        self._prefs[13] = [12, 11, 5, 14, 8, 1, 9, 7, 4, 10, 2, 15, 6, 13, 3]
        self._prefs[14] = [3, 13, 8, 2, 12, 6, 9, 7, 15, 11, 1, 4, 14, 10, 5]
        self._prefs[15] = [8, 15, 5, 12, 13, 10, 11, 6, 9, 4, 7, 2, 14, 3, 1]
        
    def _preferencias_ejemplo50(self):
        self._cantidad = 50
        self._prefs[1] = [2, 25, 26, 24, 1, 47, 30, 15, 27, 16, 39, 4, 5, 31, 41, 13, 49, 17, 21, 37, 45, 34, 11, 22, 6, 44, 12, 36, 3, 28, 8, 20, 35, 14, 33, 23, 7, 32, 18, 38, 43, 48, 40, 50, 9, 19, 46, 42, 29, 10]
        self._prefs[2] = [3, 2, 10, 31, 39, 1, 46, 11, 21, 30, 22, 33, 27, 41, 38, 48, 26, 13, 9, 35, 43, 44, 7, 18, 14, 45, 29, 6, 36, 32, 5, 24, 19, 40, 23, 16, 50, 15, 28, 25, 47, 34, 42, 20, 8, 12, 17, 37, 49, 4]
        self._prefs[3] = [33, 22, 7, 41, 37, 1, 38, 8, 3, 5, 45, 13, 9, 25, 14, 4, 15, 30, 40, 46, 10, 28, 17, 36, 21, 26, 34, 35, 23, 48, 11, 12, 20, 42, 44, 39, 19, 27, 24, 43, 18, 16, 2, 31, 49, 47, 32, 29, 6, 50]
        self._prefs[4] = [5, 4, 9, 36, 19, 8, 38, 39, 40, 48, 37, 15, 23, 32, 35, 17, 44, 14, 13, 12, 20, 18, 1, 50, 26, 29, 10, 42, 21, 7, 45, 25, 49, 31, 41, 22, 24, 28, 27, 43, 30, 33, 16, 2, 3, 46, 47, 34, 6, 11]
        self._prefs[5] = [7, 11, 36, 2, 48, 39, 3, 34, 6, 44, 29, 13, 42, 31, 40, 50, 33, 12, 26, 32, 1, 18, 15, 5, 43, 9, 30, 14, 35, 10, 49, 27, 47, 25, 20, 38, 41, 4, 17, 37, 16, 21, 22, 19, 8, 23, 46, 28, 24, 45]
        self._prefs[6] = [47, 25, 48, 2, 14, 27, 45, 30, 28, 36, 6, 42, 38, 18, 11, 9, 40, 34, 15, 32, 37, 24, 33, 23, 13, 19, 21, 17, 5, 4, 39, 35, 43, 20, 31, 46, 3, 22, 50, 41, 16, 8, 12, 29, 26, 44, 1, 7, 49, 10]
        self._prefs[7] = [21, 48, 33, 6, 40, 10, 9, 7, 4, 12, 18, 31, 39, 13, 23, 38, 22, 34, 15, 3, 26, 5, 30, 35, 27, 43, 44, 28, 41, 32, 8, 37, 45, 1, 29, 36, 47, 16, 14, 19, 50, 2, 49, 42, 11, 24, 17, 25, 46, 20]
        self._prefs[8] = [15, 25, 30, 33, 13, 9, 48, 47, 44, 43, 2, 28, 35, 41, 49, 11, 40, 42, 32, 29, 31, 3, 36, 16, 20, 8, 22, 46, 38, 34, 17, 12, 21, 50, 27, 18, 6, 45, 24, 14, 1, 4, 5, 19, 37, 26, 23, 10, 7, 39]
        self._prefs[9] = [13, 20, 28, 25, 36, 43, 35, 6, 18, 44, 30, 50, 47, 48, 17, 31, 32, 2, 41, 46, 21, 19, 9, 34, 11, 27, 8, 33, 26, 45, 12, 39, 7, 4, 29, 22, 49, 15, 23, 24, 3, 1, 38, 16, 37, 10, 14, 40, 42, 5]
        self._prefs[10] = [41, 11, 26, 24, 28, 5, 37, 45, 30, 8, 15, 7, 47, 35, 34, 21, 27, 46, 42, 16, 43, 33, 25, 40, 49, 44, 12, 6, 18, 38, 39, 17, 4, 50, 32, 13, 9, 10, 48, 22, 31, 14, 29, 23, 36, 1, 20, 19, 2, 3]
        self._prefs[11] = [40, 43, 42, 16, 39, 44, 47, 41, 31, 3, 46, 29, 25, 23, 33, 19, 50, 24, 4, 9, 5, 38, 35, 17, 13, 34, 28, 21, 2, 8, 15, 36, 18, 7, 10, 49, 48, 32, 14, 6, 1, 45, 20, 27, 11, 22, 26, 30, 37, 12]
        self._prefs[12] = [5, 3, 41, 37, 27, 11, 9, 42, 23, 32, 22, 13, 28, 16, 50, 10, 24, 17, 8, 6, 1, 46, 43, 18, 34, 30, 36, 40, 38, 12, 48, 7, 2, 47, 39, 44, 25, 45, 4, 14, 26, 35, 29, 19, 33, 49, 31, 21, 20, 15]
        self._prefs[13] = [35, 21, 46, 14, 7, 13, 16, 32, 15, 18, 43, 25, 9, 39, 27, 45, 3, 11, 29, 19, 38, 24, 8, 40, 48, 47, 36, 23, 37, 2, 22, 28, 20, 10, 5, 49, 41, 34, 31, 12, 33, 6, 50, 1, 30, 17, 44, 42, 4, 26]
        self._prefs[14] = [21, 27, 36, 29, 13, 20, 35, 47, 22, 16, 5, 37, 46, 30, 44, 15, 41, 43, 18, 4, 10, 7, 17, 45, 12, 40, 6, 49, 24, 9, 48, 8, 32, 1, 39, 42, 2, 38, 26, 25, 28, 19, 3, 14, 34, 33, 31, 50, 11, 23]
        self._prefs[15] = [38, 23, 9, 10, 41, 18, 14, 19, 4, 16, 13, 12, 3, 15, 28, 31, 40, 29, 50, 37, 17, 2, 8, 24, 45, 39, 49, 25, 32, 48, 7, 26, 33, 34, 44, 42, 21, 1, 43, 35, 6, 22, 30, 47, 36, 27, 46, 11, 20, 5]
        self._prefs[16] = [37, 49, 6, 45, 10, 43, 18, 3, 19, 40, 5, 8, 17, 41, 20, 32, 25, 31, 33, 24, 15, 28, 47, 46, 29, 34, 48, 23, 50, 26, 39, 21, 42, 30, 11, 35, 13, 7, 1, 4, 9, 44, 14, 22, 36, 16, 27, 2, 38, 12]
        self._prefs[17] = [33, 43, 30, 28, 2, 6, 47, 11, 37, 20, 23, 50, 48, 15, 19, 14, 35, 31, 41, 26, 5, 16, 36, 27, 49, 42, 29, 12, 39, 45, 4, 34, 17, 3, 32, 24, 22, 7, 9, 18, 44, 8, 46, 21, 13, 25, 1, 40, 10, 38]
        self._prefs[18] = [10, 8, 3, 9, 12, 40, 19, 48, 38, 22, 31, 1, 29, 27, 42, 44, 46, 11, 2, 47, 25, 21, 15, 35, 45, 49, 16, 20, 13, 41, 18, 50, 17, 30, 26, 24, 37, 33, 34, 43, 23, 32, 39, 6, 36, 28, 4, 7, 5, 14]
        self._prefs[19] = [19, 50, 41, 10, 36, 11, 17, 37, 4, 18, 43, 45, 38, 42, 8, 39, 13, 25, 28, 33, 35, 24, 1, 47, 2, 49, 7, 31, 46, 6, 26, 15, 14, 9, 30, 20, 5, 12, 21, 48, 32, 34, 3, 29, 27, 40, 16, 22, 23, 44]
        self._prefs[20] = [24, 41, 27, 11, 5, 17, 39, 34, 9, 30, 32, 22, 14, 12, 4, 25, 37, 26, 31, 33, 36, 3, 23, 10, 28, 6, 19, 2, 8, 50, 44, 7, 21, 18, 15, 40, 43, 20, 46, 38, 48, 13, 47, 49, 16, 45, 1, 29, 35, 42]
        self._prefs[21] = [30, 47, 42, 14, 18, 9, 44, 41, 31, 29, 26, 35, 22, 3, 24, 23, 25, 33, 15, 11, 38, 17, 40, 5, 12, 37, 48, 6, 36, 13, 19, 34, 27, 2, 49, 43, 21, 8, 28, 46, 1, 39, 10, 7, 4, 20, 32, 16, 45, 50]
        self._prefs[22] = [35, 12, 2, 8, 34, 30, 50, 38, 15, 16, 4, 41, 5, 21, 3, 43, 31, 22, 11, 13, 36, 19, 29, 44, 32, 33, 20, 9, 14, 10, 39, 6, 37, 7, 48, 17, 26, 49, 27, 28, 45, 18, 23, 25, 42, 47, 46, 1, 40, 24]
        self._prefs[23] = [41, 15, 28, 25, 30, 44, 29, 10, 48, 2, 12, 50, 21, 43, 37, 14, 45, 38, 9, 6, 49, 19, 23, 33, 18, 46, 32, 8, 1, 34, 42, 27, 11, 31, 20, 22, 13, 16, 36, 17, 39, 35, 47, 26, 40, 5, 24, 3, 7, 4]
        self._prefs[24] = [5, 7, 11, 29, 22, 48, 36, 39, 30, 26, 13, 50, 46, 45, 17, 16, 20, 28, 2, 34, 31, 1, 4, 25, 19, 6, 41, 10, 12, 9, 18, 15, 38, 27, 14, 43, 37, 3, 24, 32, 40, 35, 49, 8, 21, 23, 33, 42, 44, 47]
        self._prefs[25] = [7, 14, 45, 8, 31, 36, 30, 20, 12, 34, 1, 9, 35, 3, 23, 24, 19, 10, 21, 42, 33, 43, 2, 18, 17, 47, 25, 46, 38, 40, 48, 49, 26, 44, 15, 50, 4, 39, 6, 16, 11, 41, 27, 37, 5, 22, 32, 29, 28, 13]
        self._prefs[26] = [25, 10, 29, 1, 18, 32, 33, 43, 7, 27, 44, 39, 46, 19, 36, 22, 20, 12, 2, 9, 47, 30, 24, 35, 4, 48, 14, 34, 31, 41, 26, 28, 13, 11, 49, 45, 15, 38, 40, 6, 21, 50, 16, 5, 23, 37, 3, 17, 8, 42]
        self._prefs[27] = [39, 25, 34, 6, 28, 30, 19, 35, 17, 4, 3, 38, 14, 23, 47, 43, 9, 41, 2, 12, 1, 10, 29, 46, 49, 13, 45, 18, 36, 32, 20, 48, 27, 26, 42, 31, 5, 40, 16, 21, 24, 8, 44, 37, 50, 22, 15, 11, 7, 33]
        self._prefs[28] = [10, 17, 20, 43, 18, 33, 8, 7, 15, 47, 22, 46, 11, 24, 9, 36, 35, 38, 32, 3, 26, 12, 37, 25, 5, 29, 23, 50, 19, 44, 49, 1, 28, 13, 41, 4, 34, 2, 14, 6, 48, 45, 16, 21, 27, 40, 30, 42, 31, 39]
        self._prefs[29] = [15, 39, 20, 43, 10, 7, 5, 3, 22, 26, 41, 1, 33, 48, 47, 35, 21, 12, 30, 40, 25, 42, 38, 44, 28, 36, 45, 13, 34, 49, 29, 16, 8, 31, 18, 19, 11, 17, 46, 50, 32, 2, 14, 27, 9, 23, 24, 6, 4, 37]
        self._prefs[30] = [38, 45, 37, 18, 28, 50, 12, 30, 4, 41, 11, 6, 46, 3, 7, 49, 15, 23, 26, 2, 29, 1, 40, 47, 44, 39, 19, 42, 13, 43, 48, 25, 14, 22, 36, 31, 34, 16, 24, 17, 21, 8, 5, 27, 33, 10, 9, 20, 35, 32]
        self._prefs[31] = [5, 14, 38, 18, 21, 42, 11, 9, 4, 17, 30, 19, 26, 2, 24, 47, 41, 40, 45, 3, 46, 7, 49, 12, 20, 34, 29, 6, 27, 25, 32, 15, 16, 33, 39, 13, 22, 43, 28, 48, 23, 50, 31, 44, 37, 1, 35, 8, 36, 10]
        self._prefs[32] = [31, 21, 45, 42, 20, 39, 3, 7, 50, 27, 47, 48, 46, 26, 28, 30, 29, 23, 38, 33, 1, 49, 8, 17, 10, 37, 6, 22, 18, 16, 40, 24, 15, 32, 2, 14, 13, 43, 11, 12, 36, 35, 41, 9, 25, 34, 5, 44, 4, 19]
        self._prefs[33] = [32, 17, 5, 12, 20, 28, 9, 6, 46, 26, 25, 18, 43, 15, 8, 23, 39, 36, 44, 42, 47, 19, 33, 29, 3, 11, 4, 50, 31, 7, 34, 35, 14, 24, 27, 41, 2, 21, 10, 1, 22, 49, 13, 40, 37, 16, 45, 30, 48, 38]
        self._prefs[34] = [11, 21, 9, 6, 23, 44, 41, 39, 25, 26, 49, 33, 34, 45, 38, 17, 46, 32, 28, 47, 7, 4, 13, 36, 50, 15, 43, 19, 31, 16, 20, 29, 24, 22, 14, 12, 1, 8, 42, 2, 35, 30, 3, 48, 10, 18, 5, 37, 40, 27]
        self._prefs[35] = [25, 43, 15, 5, 10, 27, 34, 45, 42, 28, 41, 21, 50, 2, 39, 9, 29, 16, 6, 17, 13, 1, 11, 46, 36, 30, 47, 35, 20, 38, 48, 49, 19, 32, 8, 40, 31, 37, 23, 14, 44, 7, 24, 4, 3, 22, 18, 26, 12, 33]
        self._prefs[36] = [7, 46, 50, 20, 32, 35, 14, 13, 1, 43, 42, 16, 15, 4, 48, 44, 19, 29, 45, 11, 25, 41, 10, 6, 23, 3, 26, 33, 8, 39, 5, 24, 37, 47, 36, 18, 27, 40, 31, 49, 17, 2, 21, 28, 12, 34, 30, 22, 38, 9]
        self._prefs[37] = [1, 45, 39, 26, 47, 32, 31, 38, 22, 10, 4, 6, 16, 29, 9, 18, 13, 14, 15, 24, 34, 7, 48, 12, 37, 40, 43, 21, 50, 2, 35, 30, 49, 19, 11, 33, 3, 17, 44, 28, 42, 20, 41, 27, 36, 5, 23, 8, 46, 25]
        self._prefs[38] = [14, 45, 18, 10, 2, 30, 9, 33, 25, 22, 48, 46, 31, 8, 47, 23, 12, 5, 36, 39, 29, 16, 44, 6, 13, 37, 28, 49, 43, 24, 7, 17, 19, 40, 42, 21, 34, 27, 50, 35, 4, 20, 11, 3, 32, 38, 41, 1, 15, 26]
        self._prefs[39] = [15, 41, 3, 49, 39, 42, 38, 30, 44, 1, 37, 47, 5, 22, 43, 34, 28, 18, 40, 11, 25, 27, 21, 29, 48, 19, 24, 12, 9, 16, 33, 31, 45, 4, 13, 7, 36, 46, 14, 2, 26, 23, 35, 32, 50, 8, 17, 6, 10, 20]
        self._prefs[40] = [12, 11, 4, 39, 9, 14, 17, 6, 33, 5, 47, 32, 49, 27, 2, 48, 10, 36, 50, 21, 28, 42, 1, 35, 43, 19, 37, 45, 31, 26, 16, 29, 34, 15, 24, 7, 3, 30, 13, 40, 20, 41, 44, 38, 25, 22, 8, 23, 18, 46]
        self._prefs[41] = [45, 16, 36, 42, 29, 23, 3, 12, 1, 14, 44, 43, 46, 21, 8, 20, 13, 34, 22, 32, 19, 15, 30, 40, 37, 4, 49, 9, 7, 26, 48, 11, 27, 10, 41, 39, 35, 5, 24, 33, 47, 38, 50, 6, 17, 25, 2, 28, 31, 18]
        self._prefs[42] = [50, 25, 17, 13, 6, 40, 5, 34, 8, 11, 22, 16, 43, 3, 1, 44, 24, 19, 45, 33, 39, 47, 30, 32, 10, 12, 36, 41, 28, 38, 31, 46, 29, 9, 37, 18, 48, 42, 23, 4, 7, 27, 15, 21, 35, 49, 26, 2, 14, 20]
        self._prefs[43] = [3, 21, 6, 49, 9, 34, 25, 44, 22, 47, 24, 10, 11, 16, 15, 8, 39, 30, 48, 26, 37, 12, 29, 17, 40, 18, 41, 1, 35, 46, 36, 43, 4, 45, 42, 28, 13, 23, 27, 33, 31, 7, 38, 19, 14, 5, 20, 32, 2, 50]
        self._prefs[44] = [16, 6, 19, 39, 24, 7, 44, 31, 4, 33, 2, 27, 13, 12, 29, 34, 20, 28, 37, 42, 49, 32, 9, 3, 25, 17, 15, 50, 8, 1, 35, 11, 30, 47, 26, 46, 14, 40, 48, 36, 10, 41, 45, 21, 18, 22, 23, 5, 43, 38]
        self._prefs[45] = [23, 30, 7, 31, 42, 14, 3, 22, 34, 19, 25, 38, 20, 41, 16, 13, 44, 46, 5, 15, 36, 6, 29, 11, 47, 37, 45, 50, 35, 32, 4, 10, 28, 8, 9, 26, 49, 43, 1, 24, 12, 48, 2, 40, 21, 27, 18, 33, 39, 17]
        self._prefs[46] = [1, 15, 4, 45, 29, 23, 17, 25, 3, 20, 41, 31, 19, 49, 21, 5, 16, 47, 32, 50, 12, 14, 37, 9, 44, 38, 22, 18, 8, 36, 33, 48, 46, 42, 30, 24, 28, 6, 39, 7, 40, 10, 27, 26, 13, 34, 11, 43, 35, 2]
        self._prefs[47] = [3, 31, 27, 21, 15, 4, 37, 35, 5, 34, 8, 39, 23, 24, 50, 25, 30, 36, 40, 22, 45, 2, 9, 46, 18, 26, 7, 6, 19, 13, 41, 11, 1, 29, 32, 47, 43, 12, 33, 42, 16, 14, 38, 17, 44, 28, 48, 10, 49, 20]
        self._prefs[48] = [23, 4, 31, 45, 26, 24, 29, 1, 21, 3, 36, 7, 28, 5, 50, 44, 9, 42, 8, 6, 12, 33, 43, 20, 35, 41, 37, 11, 49, 27, 25, 39, 32, 47, 16, 17, 48, 30, 40, 13, 10, 46, 22, 34, 2, 15, 19, 14, 18, 38]
        self._prefs[49] = [2, 17, 9, 11, 47, 6, 38, 48, 30, 37, 4, 35, 43, 27, 13, 31, 14, 8, 7, 32, 10, 5, 34, 12, 49, 19, 3, 29, 21, 24, 40, 50, 15, 33, 20, 45, 39, 42, 26, 44, 36, 28, 41, 23, 18, 46, 22, 16, 25, 1]
        self._prefs[50] = [45, 10, 8, 4, 7, 17, 30, 29, 6, 47, 11, 13, 36, 25, 39, 31, 1, 46, 9, 34, 16, 18, 38, 27, 48, 5, 3, 19, 22, 43, 40, 49, 20, 37, 2, 42, 12, 44, 21, 14, 33, 35, 24, 26, 28, 32, 41, 15, 50, 23]