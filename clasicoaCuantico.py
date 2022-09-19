from numerosComplejos import *
import matplotlib.pyplot as plot
import numpy as np
def main():
    booleanMatrix = [[False, False, False, False, False, False], [True, False, False, False, False, True],
                     [True, False, False, False, False, False], [
        False, False, True, False, False, False],
        [False, False, False, True, False, False], [False, False, False, False, True, False]]

    vectIni = [True, False, False, False, False, False]
    print("Experimento canicas " + str(experimentoCanicas(1, booleanMatrix[:], vectIni[:])))
    
    matrix = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.3333333333333333, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.3333333333333333, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.3333333333333333, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0.5, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0.5, 0], [0.5, 0], [0, 0],
               [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0, 0], [0.5, 0], [0.5, 0],
               [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0, 0], [0, 0], [0.5, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]

    vectIni = [[1, 0], [0, 0], [0, 0], [
        0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    
    print("Multiple rendija clasico  " +
          str(multipleRendijaClasico(matrix[:], vectIni[:], 1)))
    
    matrix = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.7071067811865475, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0.7071067811865475, 0], [0, 0], [0, 0], [
                  0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [-0.4082482904638631, 0.4082482904638631],
               [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [-0.4082482904638631, -0.4082482904638631],
               [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
              [[0, 0], [0.4082482904638631, -0.4082482904638631], [-0.4082482904638631,
                                                                   0.4082482904638631], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
              [[0, 0], [0, 0], [-0.4082482904638631, -0.4082482904638631],
               [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
              [[0, 0], [0, 0], [0.4082482904638631, -0.4082482904638631], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]

    vectIni = [[1, 0], [0, 0], [0, 0], [
        0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    
    print("Multiple rendija cuantico  " + str(multipleRendijaCuantico(matrix[:], vectIni[:], 1)))
    
    Matriz_Doble_Rendija = [
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0],
            [0, 0], [0, 0], [0, 0], [0, 0]],
        [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0],
            [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [-1 / math.sqrt(6), 1 / math.sqrt(6)],
            [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)],
            [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
        [[0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [-1 / math.sqrt(6),
                                                         1 / math.sqrt(6)], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0]],
        [[0, 0], [0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)],
            [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
        [[0, 0], [0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]

    Estado_Inicial = [[1, 0], [0, 0], [0, 0], [
        0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

    answ = accionMatrizVector(multipleRendijaCuantico(Matriz_Doble_Rendija[:],
                                                              Estado_Inicial[:], 2),  Estado_Inicial)
    graphProbabilitiesVector(answ)
    

def accionBooleanentreMatrizVector(matrix, vector):
    row, col = len(matrix), len(matrix[0])
    length = len(vector)

    if (col == length):
        answ = [False for c in range(row)]

        for i in range(row):
            And = True

            for j in range(col):
                And = matrix[i][j] and vector[j]
                answ[i] = answ[i] or And

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")

def experimentoCanicas( clicks ,booleanMatrix, vectIni  ):
    if ( clicks >= 0 and type( clicks ) is int ):
        for c in range( clicks ):
            vectIni = accionBooleanentreMatrizVector(booleanMatrix, vectIni)
        return vectIni


def multipleRendijaClasico(matrix, vectIni, clicks):
    if (clicks >= 0) and (type(clicks) is int):
        for x in range(clicks):
            vectIni = accionMatrizVector(matrix, vectIni)
        return vectIni
    return -1


def multipleRendijaCuantico(matrix, vectIni, clicks):
    if ( clicks  >= 0 ) and ( type( clicks ) is int ):
        length  = len( vectIni )
        copyMatrix = matrix[:]
        
        for x in range(clicks  ):
            matrix = multiplicacionDeMarticesIguales( matrix, copyMatrix)

        return matrizFinal(matrix)
    return -1


def graphProbabilitiesVector( vector  ):
    x = np.array([x for x in range(len(vector))])
    y = np.array([round(vector[x][0]*100, 2) for x in range(len(vector))])

    plot.bar( x,y , color ='g', align='center')
    plot.title('Probabilidades vector')
    plot.show()
  
  

def matrizFinal(matrix):
    row, column = len(matrix), len(matrix[0])
    for i in range(row):
        nRow = []
        for j in range(column):
            nRow.append([(moduloComplejos(matrix[i][j])**2), 0])

        matrix[i] = nRow
    return matrix


    
    
    
main()