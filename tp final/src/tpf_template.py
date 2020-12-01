from planilla import Preferencias, Planilla
prefs = Preferencias("Ejemplo3")
print(prefs)
# imprime {1: [2, 1, 3], 2: [1, 2, 3], 3: [1, 3, 2]}
print(prefs.estudiantes())
# imprime {1, 2, 3}
sol = Planilla(prefs)
print(sol)
# imprime {}
sol.asignar(1, 2)
print(sol.estudiantes_con_topico()) # imprime {1}
print(sol.topicos_sin_estudiante()) # imprime {1, 3}
print(sol)
# imprime {1: 2}
sol.asignar(1, 1)
# el estudiante 1 ya tenia topico
# sol.asignar(3, 2)
print(sol)
print(sol.calcular_costo())
print(sol.estudiante_libre(3))
sol.asignar(2, 1)
sol.asignar(3, 3)
print(sol)
print(sol.calcular_costo())
# el topico 2 no estaba disponible
# imprime {1: 2}
# imprime inf
# imprime True
# imprime {1: 2, 2: 1, 3: 3}
# imprime 1