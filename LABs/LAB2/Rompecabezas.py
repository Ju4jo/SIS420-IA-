# ESTUDIANTE: IGLESIAS ROCABADO DANIELA
# CU: 35-4780

from busquedas_02 import aestrella, ProblemaBusqueda


OBJETIVO = '''a-b-c-d
e-f-g-h
i-j-k-x'''

INICIAL = '''x-k-j-i
h-g-f-e
d-c-b-a'''


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])


def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]


def find_location(filas, element_to_find):
    '''Encuentra la ubicacion de una pieza en el rompecabezas.
       DEvuelve una tupla: fila, columna'''
    for ir, row in enumerate(filas):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


posiciones_objetivo = {}
filas_objetivo = string_to_list(OBJETIVO)
for letra in 'abcefghijkx':
    posiciones_objetivo[letra] = find_location(filas_objetivo, letra)


class EigthPuzzleProblem(ProblemaBusqueda):
    def acciones(self, estado):
        '''Devuelve una lista de piesas que se pueden mover a un espacio vacio.'''
        filas = string_to_list(estado)
        fila_x, columna_x = find_location(filas, 'x')

        acciones = []
        if fila_x > 0:

            acciones.append(filas[fila_x - 1][columna_x])
        if fila_x < 2:
            acciones.append(filas[fila_x + 1][columna_x])
        if columna_x > 0:
            acciones.append(filas[fila_x][columna_x - 1])
        if columna_x < 3:
            acciones.append(filas[fila_x][columna_x + 1])

        return acciones

    def resultado(self, estado, accion):
        '''Devuelve el resultado despues de mover una pieza a un espacio en vacio
        '''
        filas = string_to_list(estado)
        fila_x, columna_x = find_location(filas, 'x')
        fila_n, columna_n = find_location(filas, accion)

        filas[fila_x][columna_x], filas[fila_n][columna_n] = filas[fila_n][columna_n], filas[fila_x][columna_x]

        return list_to_string(filas)

    def es_objetivo(self, estado):
        '''Devuelve True si un estado es el estado_objetivo.'''
        return estado == OBJETIVO

    def costo(self, estado1, accion, estado2):
        '''Devuelve el costo de ejecutar una accion. 
        '''
        return 1

    def heuristica(self, estado):
        '''Devuelve una estimacion de la distancia
        de un estado a otro, utilizando la distancia manhattan.
        '''
        filas = string_to_list(estado)

        distancia = 0

        for numero in 'abcefghijkx':
            fila_n, columna_n = find_location(filas, numero)
            fila_n_objetivo, col_n_goal = posiciones_objetivo[numero]

            distancia += abs(fila_n - fila_n_objetivo) + abs(columna_n - col_n_goal)

        return distancia

    # def heurisica(self,estado):
    #     filas = string_to_list(estado)
    #
    #     distancia = 0
    #
    #     for letra in 'abcdefghijkx':
    #         fila_n, columna_n = find_location(filas, letra)
    #         fila_n_objetivo, col_n_goal = posiciones_objetivo[letra]
    #         if fila_n != fila_n_objetivo and columna_n != col_n_goal:
    #             distancia += 1
    #     return distancia

resultado = aestrella(EigthPuzzleProblem(INICIAL))
it = 0

for accion, estado in resultado.camino():
    print('Move numero', accion)
    it += 1
    print('nro de movimientos', it)
    print(estado)
