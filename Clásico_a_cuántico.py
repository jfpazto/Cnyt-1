import matplotlib.pyplot as plt
import Librería_vectores_matrices
import math
def Canicas(matriz, vector, click):

    if len(matriz) == len(vector):

        estado = vector
        while click != 0:
            
            estado = Librería_vectores_matrices.AccionMatrizVector(matriz,estado)
            click -= 1

        
        titulo = plt.figure('Sistema dinamico despues de 2 clicks Tiempo') # Figure
        titulo1 = titulo.add_subplot(111) # Axes

        nombres_ejex = ['P.0','P.1','P.2','P.3','P.4','P.5','P.6','P.7']
        datos = [estado[0][0],estado[1][0],estado[2][0],estado[3][0],estado[4][0],estado[5][0],estado[6][0],estado[7][1]]
        num_datos = range(len(datos))

        titulo1.bar(num_datos, datos, width=0.5, align='center')
        titulo1.set_xticks(num_datos)
        titulo1.set_xticklabels(nombres_ejex)

        plt.show()
        return estado
##        for i in range(len(respuesta)):
##
##            if respuesta[i][0] != 0:
##                respuesta[i][0] = True
##                respuesta[i][1] = True
##            else:
##                respuesta[i][0] = False
##                respuesta[i][1] = False
    else:
        print("Dimensiones incorrectas. Por favor digita de nuevo")

def Probabilidad(matriz, vector):

    respuesta = vector
    
    if len(matriz) == len(vector):        
        respuesta = Librería_vectores_matrices.AccionMatrizVector(matriz,respuesta)
        return respuesta
    else:
        print("Dimensiones incorrectas. Por favor digita de nuevo")

def DobleRendija(matriz):

    respuesta = matrizmultiplication(matriz,matriz)
    return respuesta

print(Canicas([[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(1/math.sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(1/math.sqrt(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(0,0),(-1/math.sqrt(6),1/math.sqrt(6)),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
    [(0,0),(-1/math.sqrt(6),-1/math.sqrt(6)),(0 ,0),(0 ,0),(1,0),(0,0),(0,0),(0,0)],
    [(0,0),(1/math.sqrt(6),-1/math.sqrt(6)),(-1/math.sqrt(6),1/math.sqrt(6)),(0,0),(0,0),(1,0),(0,0),(0,0)],
    [(0,0),(0,0),(-1/math.sqrt(6),-1/math.sqrt(6),0),(0,0),(0,0),(0,0),(1,0),(0,0)],
    [(0,0),(0,0),(1/math.sqrt(6),-1/math.sqrt(6)),(0,0),(0,0),(0,0),(0,0),(1,0)]],[(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],2))
