# tp_tecnicas_algoritmicas
TP Final de Tecnicas Algoritmicas - Universidad Torcuato Di Tella


### Ejecucion del programa
```bash
cd src
python tpf.py
```

### Dump del programa
En este caso, se utilizan 30 iteraciones para el algoritmo de búsqueda local iterativa. Es interesante observar como se llega a las mismas asignaciones que con backtracking, pero los tiempos difieren en varios ordenes de magnitud.
```
(tp_tecnicas_algoritmicas) jgonzalez@NBI660728:~/dev/tp_tecnicas_algoritmicas/src(master)$ python tpf.py
Funcion asignar: asignar_greedy()
        Tiempo de ejecucion: 4.1e-05
        Preferencias Ejemplo3: {1: [2, 1, 3], 2: [1, 2, 3], 3: [1, 3, 2]}
        Solucion: {1: 2, 2: 1, 3: 3}
        Costo: 1
        -------------------------------------------
        Tiempo de ejecucion: 5.3e-05
        Preferencias Ejemplo5: {1: [3, 1, 2, 4, 5], 2: [4, 3, 1, 2, 5], 3: [5, 1, 2, 3, 4], 4: [1, 5, 4, 2, 3], 5: [2, 1, 3, 4, 5]}
        Solucion: {1: 3, 2: 4, 3: 5, 4: 1, 5: 2}
        Costo: 0
        -------------------------------------------
        Tiempo de ejecucion: 8.3e-05
        Preferencias Ejemplo10: {1: [1, 10, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3: [2, 1, 3, 4, 5, 6, 7, 8, 9, 10], 4: [3, 2, 1, 4, 5, 6, 7, 8, 9, 10], 5: [4, 3, 2, 1, 5, 6, 7, 8, 9, 10], 6: [5, 4, 3, 2, 1, 6, 7, 8, 9, 10], 7: [6, 5, 4, 3, 2, 1, 7, 8, 9, 10], 8: [7, 6, 5, 4, 3, 2, 1, 8, 9, 10], 9: [8, 7, 6, 5, 4, 3, 2, 1, 9, 10], 10: [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]}
        Solucion: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
        Costo: 45
        -------------------------------------------
Funcion asignar: asignar_bl()
        Tiempo de ejecucion: 2.2e-05
        Preferencias Ejemplo3: {1: [2, 1, 3], 2: [1, 2, 3], 3: [1, 3, 2]}
        Solucion: {3: 1, 2: 2, 1: 3}
        Costo: 3
        -------------------------------------------
        Tiempo de ejecucion: 0.000326
        Preferencias Ejemplo5: {1: [3, 1, 2, 4, 5], 2: [4, 3, 1, 2, 5], 3: [5, 1, 2, 3, 4], 4: [1, 5, 4, 2, 3], 5: [2, 1, 3, 4, 5]}
        Solucion: {3: 5, 5: 4, 1: 1, 2: 3, 4: 2}
        Costo: 8
        -------------------------------------------
        Tiempo de ejecucion: 0.025416
        Preferencias Ejemplo10: {1: [1, 10, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3: [2, 1, 3, 4, 5, 6, 7, 8, 9, 10], 4: [3, 2, 1, 4, 5, 6, 7, 8, 9, 10], 5: [4, 3, 2, 1, 5, 6, 7, 8, 9, 10], 6: [5, 4, 3, 2, 1, 6, 7, 8, 9, 10], 7: [6, 5, 4, 3, 2, 1, 7, 8, 9, 10], 8: [7, 6, 5, 4, 3, 2, 1, 8, 9, 10], 9: [8, 7, 6, 5, 4, 3, 2, 1, 9, 10], 10: [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]}
        Solucion: {9: 5, 8: 7, 2: 1, 10: 8, 1: 10, 4: 3, 6: 9, 3: 2, 5: 4, 7: 6}
        Costo: 13
        -------------------------------------------
Funcion asignar: asignar_bli()
        Tiempo de ejecucion: 8e-06
        Tiempo de ejecucion: 9e-06
        Tiempo de ejecucion: 6e-06
        Tiempo de ejecucion: 5e-06
        Tiempo de ejecucion: 5e-06
        Tiempo de ejecucion: 9e-06
        Tiempo de ejecucion: 1e-05
        Tiempo de ejecucion: 9e-06
        Tiempo de ejecucion: 9e-06
        Tiempo de ejecucion: 8e-06
        Tiempo de ejecucion: 9e-06
        Tiempo de ejecucion: 5e-06
        Tiempo de ejecucion: 1.1e-05
        Tiempo de ejecucion: 6e-06
        Tiempo de ejecucion: 9e-06
        Tiempo de ejecucion: 1.7e-05
        Tiempo de ejecucion: 1.2e-05
        Tiempo de ejecucion: 1.2e-05
        Tiempo de ejecucion: 1.1e-05
        Tiempo de ejecucion: 1.2e-05
        Tiempo de ejecucion: 1.1e-05
        Tiempo de ejecucion: 1.2e-05
        Tiempo de ejecucion: 1.2e-05
        Tiempo de ejecucion: 1.1e-05
        Tiempo de ejecucion: 1.3e-05
        Tiempo de ejecucion: 1.3e-05
        Tiempo de ejecucion: 1.2e-05
        Tiempo de ejecucion: 1.3e-05
        Tiempo de ejecucion: 1.3e-05
        Tiempo de ejecucion: 1.2e-05
        Tiempo de ejecucion: 0.003135
        Preferencias Ejemplo3: {1: [2, 1, 3], 2: [1, 2, 3], 3: [1, 3, 2]}
        Solucion: {2: 1, 3: 3, 1: 2}
        Costo: 1
        -------------------------------------------
        Tiempo de ejecucion: 0.000397
        Tiempo de ejecucion: 0.000263
        Tiempo de ejecucion: 0.000489
        Tiempo de ejecucion: 0.000402
        Tiempo de ejecucion: 0.000216
        Tiempo de ejecucion: 0.000442
        Tiempo de ejecucion: 0.000215
        Tiempo de ejecucion: 0.000467
        Tiempo de ejecucion: 0.000703
        Tiempo de ejecucion: 0.000405
        Tiempo de ejecucion: 0.00022
        Tiempo de ejecucion: 0.00044
        Tiempo de ejecucion: 0.000418
        Tiempo de ejecucion: 0.000437
        Tiempo de ejecucion: 0.000216
        Tiempo de ejecucion: 0.000471
        Tiempo de ejecucion: 0.000215
        Tiempo de ejecucion: 0.000398
        Tiempo de ejecucion: 0.000245
        Tiempo de ejecucion: 0.000221
        Tiempo de ejecucion: 0.000448
        Tiempo de ejecucion: 0.00048
        Tiempo de ejecucion: 0.000591
        Tiempo de ejecucion: 0.000216
        Tiempo de ejecucion: 0.000415
        Tiempo de ejecucion: 0.000607
        Tiempo de ejecucion: 0.000421
        Tiempo de ejecucion: 0.000394
        Tiempo de ejecucion: 0.000439
        Tiempo de ejecucion: 0.000583
        Tiempo de ejecucion: 0.015026
        Preferencias Ejemplo5: {1: [3, 1, 2, 4, 5], 2: [4, 3, 1, 2, 5], 3: [5, 1, 2, 3, 4], 4: [1, 5, 4, 2, 3], 5: [2, 1, 3, 4, 5]}
        Solucion: {5: 2, 2: 4, 4: 1, 3: 5, 1: 3}
        Costo: 0
        -------------------------------------------
        Tiempo de ejecucion: 0.022645
        Tiempo de ejecucion: 0.017851
        Tiempo de ejecucion: 0.025187
        Tiempo de ejecucion: 0.021656
        Tiempo de ejecucion: 0.021213
        Tiempo de ejecucion: 0.017597
        Tiempo de ejecucion: 0.025087
        Tiempo de ejecucion: 0.02468
        Tiempo de ejecucion: 0.021416
        Tiempo de ejecucion: 0.018004
        Tiempo de ejecucion: 0.02146
        Tiempo de ejecucion: 0.021194
        Tiempo de ejecucion: 0.0177
        Tiempo de ejecucion: 0.021944
        Tiempo de ejecucion: 0.021695
        Tiempo de ejecucion: 0.021268
        Tiempo de ejecucion: 0.021888
        Tiempo de ejecucion: 0.025111
        Tiempo de ejecucion: 0.025063
        Tiempo de ejecucion: 0.021596
        Tiempo de ejecucion: 0.017902
        Tiempo de ejecucion: 0.02136
        Tiempo de ejecucion: 0.021621
        Tiempo de ejecucion: 0.026258
        Tiempo de ejecucion: 0.028162
        Tiempo de ejecucion: 0.021293
        Tiempo de ejecucion: 0.014225
        Tiempo de ejecucion: 0.021304
        Tiempo de ejecucion: 0.025595
        Tiempo de ejecucion: 0.017725
        Tiempo de ejecucion: 0.6573
        Preferencias Ejemplo10: {1: [1, 10, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3: [2, 1, 3, 4, 5, 6, 7, 8, 9, 10], 4: [3, 2, 1, 4, 5, 6, 7, 8, 9, 10], 5: [4, 3, 2, 1, 5, 6, 7, 8, 9, 10], 6: [5, 4, 3, 2, 1, 6, 7, 8, 9, 10], 7: [6, 5, 4, 3, 2, 1, 7, 8, 9, 10], 8: [7, 6, 5, 4, 3, 2, 1, 8, 9, 10], 9: [8, 7, 6, 5, 4, 3, 2, 1, 9, 10], 10: [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]}
        Solucion: {6: 5, 5: 4, 3: 2, 2: 1, 8: 7, 10: 9, 9: 8, 7: 6, 1: 10, 4: 3}
        Costo: 1
        -------------------------------------------
Funcion asignar: asignar_backtracking()
        Tiempo de ejecucion: 0.000786
        Preferencias Ejemplo3: {1: [2, 1, 3], 2: [1, 2, 3], 3: [1, 3, 2]}
        Solucion: {1: 2, 2: 1, 3: 3}
        Costo: 1
        -------------------------------------------
        Tiempo de ejecucion: 0.02197
        Preferencias Ejemplo5: {1: [3, 1, 2, 4, 5], 2: [4, 3, 1, 2, 5], 3: [5, 1, 2, 3, 4], 4: [1, 5, 4, 2, 3], 5: [2, 1, 3, 4, 5]}
        Solucion: {5: 2, 4: 1, 3: 5, 2: 4, 1: 3}
        Costo: 0
        -------------------------------------------
        Tiempo de ejecucion: 783.26797
        Preferencias Ejemplo10: {1: [1, 10, 2, 3, 4, 5, 6, 7, 8, 9], 2: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3: [2, 1, 3, 4, 5, 6, 7, 8, 9, 10], 4: [3, 2, 1, 4, 5, 6, 7, 8, 9, 10], 5: [4, 3, 2, 1, 5, 6, 7, 8, 9, 10], 6: [5, 4, 3, 2, 1, 6, 7, 8, 9, 10], 7: [6, 5, 4, 3, 2, 1, 7, 8, 9, 10], 8: [7, 6, 5, 4, 3, 2, 1, 8, 9, 10], 9: [8, 7, 6, 5, 4, 3, 2, 1, 9, 10], 10: [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]}
        Solucion: {2: 1, 1: 10, 3: 2, 4: 3, 5: 4, 6: 5, 8: 7, 9: 8, 10: 9, 7: 6}
        Costo: 1
        -------------------------------------------
Hora de salida:  2020-11-28 21:09:24.350215
```

