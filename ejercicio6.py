"""Realiza el  código para calcular el determinante de una matriz cuadrada de [5 x 5],
 regla de Sarrus de forma recursiva y de forma iterativa"""

def creacionmatriz(fil1,fil2,fil3):
    matriz = [fil1, fil2,fil3]
    return matriz

def multiplicacion(m):
    m1 = int(m[0][0]*m[1][1]*m[2][2])
    m2 = int(m[1][0]*m[2][1]*m[0][2])
    m3 = int(m[2][0]*m[0][1]*m[1][2])

    mtotal = m1+m2+m3
    return mtotal

def inversion(m):
    minversa=[]
    for i in m:
        r = i[::-1]
        minversa.append(r)
    return minversa

def determinante(fil1,fil2,fil3):
    matriz = creacionmatriz(fil1,fil2,fil3)
    matinvertida = inversion(matriz)
    det = multiplicacion(matriz)-multiplicacion(matinvertida)
    return det

fila1 = [2,1,0]
fila2 = [3,1,-1]
fila3= [2,0,4]

print(determinante(fila1,fila2,fila3))







