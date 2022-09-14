from numerosComplejos import *

def main():
    matriz = [[[-5,0],[3,0],[4,0],[-1,0]],[[7,0],[5,0],[2,0],[4,0]],[[2,0],[-1,0],[-6,0],[0,0]]]
    vector = [[4,0],[2,0],[-6,0]]
    print("accion " + str(accionEntreMatrizyVector(matriz,vector)))

def accionEntreMatrizyVector(matrix, vector):
    row, col = len(matrix), len(matrix[0])
    length = len(vector)

    if (col == length):
        answ = [[0, 0] for x in range(row)]

        for i in range(row):
            for j in range(col):
                mult = multiplicarComplejos(matrix[i][j], vector[j])
                answ[i] = sumarComplejos(answ[i], mult)

        return answ
    print("Las dimensiones de las matrices, no son los adecuados para su multiplicacion")

    
    

    
    
    
main()