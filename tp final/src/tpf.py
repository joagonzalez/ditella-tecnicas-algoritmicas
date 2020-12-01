import os
import datetime
import random
from threading import Timer
from planilla import Planilla, Preferencias
from copy import deepcopy

def asignar_random(prefs):
    '''
    funcion que genera una solucion aleatoria del espacio de soluciones
    posibles en la asignacion de topicos a estudiantes
    '''
    sol = Planilla(prefs)
    while len(sol.estudiantes_sin_topico()) > 0:
        e = random.choice(list(sol.estudiantes_sin_topico()))
        t = random.choice(list(sol.topicos_sin_estudiante()))
        sol.asignar(e, t)
    return sol

def exitfunc():
    '''
    funcion que se ejecuta al pasar 1 hora de ejecucion del script
    '''
    print("Hora de salida: ", datetime.datetime.now())
    os._exit(0)

def calcular_tiempo(func, *args, **kwargs):
    '''
    decorator que permite reutilizar codigo para calcular
    tiempo de ejecucion de cada algoritmo
    '''
    def wrapper(*args, **kwargs):
        comienzo = datetime.datetime.now()
        sol = func(*args, **kwargs)
        tiempo = (datetime.datetime.now() - comienzo).total_seconds()
        print('	Tiempo de ejecucion: {}'.format(tiempo))
        return sol
    return wrapper

@calcular_tiempo
def asignar_greedy(prefs):
    '''
    Asigna estudiantes y topicos por:
    - orden en que un estudiante es listado por prefs.
    - orden de preferencias asumiendo que el primero es el mas preferido.
    '''
    sol = Planilla(prefs)
    # Itero a traves de los estudiantes sin topico.
    for e in sol.estudiantes_sin_topico():
        # Obtengo la lista de preferencias de los topicos del estudiante e.
        prefs_e = prefs.preferencias_del_estudiante(e)
        # Obtengo los topicos sin estudiante al momento.
        topicos_sin_asignar = sol.topicos_sin_estudiante()
        i = 0
        t_i = prefs_e[i]
        while (t_i not in topicos_sin_asignar) and (i < len(prefs_e)):
            '''
            Mientras sea un topico asignado se sigue iternado. Cuando se encuentra el topico
            de menor costo (se itera de menor costo a mayor costo) libre se deja de iterar y se asigna
            el topico al estudiante
            '''
            i = i + 1
            t_i = prefs_e[i]
        sol.asignar(e, t_i)
    return sol

@calcular_tiempo
def asignar_backtracking(prefs):
    sol = Planilla(prefs)
    return asignar_backtracking_internal(sol, prefs)

def asignar_backtracking_internal(sol, prefs):
    # Analizamos el caso base, no hay estudiantes sin topico
    if not sol.estudiantes_sin_topico():
        return sol
    # Aun tenemos estudiantes a los cuales asignar un topico
    # Consecuentemente, para cada estudiante que resta vamos a
    # avanzar un paso. Avanzar un paso implicar iterar en cada
    # uno de los estudiantes, obtener una solucion para ellos, y
    # si es mejor que la que dispongo, la guardo. Sino descarto
    # la mejor solucion por esa rama.
    mejor_solucion = None
    mejor_costo = None
    for e in sol.estudiantes_sin_topico():
        # 1.- Avanzo un paso y asigno un topico segun las preferencias del
        #     estudiante e.
        prefs_e = prefs.preferencias_del_estudiante(e)
        # Obtengo los topicos sin estudiante al momento.
        topicos_sin_asignar = sol.topicos_sin_estudiante()
        i = 0
        t_i = prefs_e[i]
        while (t_i not in topicos_sin_asignar) and (i < len(prefs_e)):
            i = i + 1
            t_i = prefs_e[i]
        sol.asignar(e, t_i)
        
        # 2.- Resuelvo recursivamente para el estudiante e
        #     Notar la copia de la solucion. Necesitamos pasar una nueva
        #     instancia de la solucion para que se le hagan las modificaciones
        #     pertinentes a la misma sin afectar a la actual.
        sol_e = asignar_backtracking_internal(deepcopy(sol), prefs)
        # Evaluo si es mejor solucion que las que dispongo al momento.
        sol_costo_e = sol_e.calcular_costo()
        if (not mejor_solucion or not mejor_costo) or sol_costo_e < mejor_costo:
            mejor_solucion = sol_e
            mejor_costo = sol_costo_e
        
        # 3.- Retrocedemos un paso mediante la desasignacion del
        #     estudiante e.
        sol.desasignar(e, t_i)
    # Retorno la mejor solucion.
    return mejor_solucion

@calcular_tiempo
def asignar_bl(prefs, solucion_inicial):
    '''
    buscamos las soluciones vecinas de la solucion_inicial
    de todas las soluciones obtenidas, buscamos la que tiene mejor costo
    y nos quedamos con la mejor solucion local. El criterio de solucion 
    vecina elegido es en base a todas las formas posibles de invertir pares
    de topicos asignados a estudiantes
    '''
    mejorable = True
    max_iters = 1e6
    i = 0
    solucion_actual = solucion_inicial
    costo_actual = solucion_inicial.calcular_costo()
    

    while mejorable and i <= int(max_iters):
        costo_mejor_vecino = float('inf')
        mejor_vecino = None
        # recorremos todas las soluciones vecinas y encontramos la mejor
        for i in range(1, solucion_actual.cantidad()-2):
            for j in range(i+1, solucion_actual.cantidad()-1):
                vecino = solucion_actual.copy()
                # swap de topicos asignados
                vecino.solucion()[i],vecino.solucion()[j] = vecino.solucion()[j],vecino.solucion()[i] 

                if vecino.calcular_costo() < costo_mejor_vecino:
                    costo_mejor_vecino = vecino.calcular_costo()
                    mejor_vecino = vecino

        # si el costo de la mejor solucion vecina es mejor que la actual entonces seguimos buscando mejoras
        # sino, consideramos que no vale la pena pagar el costo de oportunidad por seguir buscando posibles
        # soluciones
        
        mejorable = costo_mejor_vecino < costo_actual
        if mejorable:
            # se continua buscando mejores soluciones hasta que no se puede mejorar
            solucion_actual = mejor_vecino
            costo_actual = costo_mejor_vecino

        i += 1
    
    return solucion_actual

@calcular_tiempo
def asignar_bli(prefs, iters):
    # Generacion de iters soluciones con asignar_bl() con el fin de realizar una
    # busqueda mas exhaustiva en el espacio de soluciones.
    soluciones = [asignar_bl(prefs, asignar_random(prefs)) for _ in range(iters)]
    # Retorno la que gue genere el menor costo
    return min(soluciones, key=lambda solucion : solucion.calcular_costo())

def eval_asignacion(asignar_f, algoritmo, iters=0):
    casos = ['Ejemplo3', 'Ejemplo5', 'Ejemplo10', 'Ejemplo12', 'Ejemplo15', 'Ejemplo50']
    # casos_test = ['Ejemplo3', 'Ejemplo5', 'Ejemplo10']
    for caso in casos:
        prefs = Preferencias(caso)
        if algoritmo == 'bl':
            solucion_inicial = asignar_random(prefs)
            sol = asignar_f(prefs, solucion_inicial)
        elif algoritmo == 'bli':
            sol = asignar_f(prefs, iters)
        else:
            sol = asignar_f(prefs)

        print('	Preferencias {}: {}'.format(caso, prefs))
        print('	Solucion: {}'.format(sol))
        print('	Costo: {}'.format(sol.calcular_costo()))
        print('	-------------------------------------------')

if __name__ == '__main__':
    ITERS = [3, 5, 10, 20, 30] 

    Timer(3600, exitfunc).start() # salida en 1 hora    
    print('Funcion asignar: asignar_greedy()')
    eval_asignacion(asignar_greedy, algoritmo='greedy')

    print('Funcion asignar: asignar_bl()')
    eval_asignacion(asignar_bl, algoritmo='bl')

    for repetitions in ITERS:
        print('Funcion asignar (iters = {}): asignar_bli()'.format(repetitions))
        eval_asignacion(asignar_bli, algoritmo='bli', iters=repetitions)

    print('Funcion asignar: asignar_backtracking()')
    eval_asignacion(asignar_backtracking, algoritmo='backtracking')

    exitfunc()
