import Librería_números_complejos

def SumaVector(v1,v2):

    respuesta = []
    
    for i in range(len(v1)):
        respuesta.append(Librería_números_complejos.Suma(v1[i],v2[i]))
        

    return respuesta

def InversoVector(v):

    respuesta = []

    for i in range(len(v)):
        respuesta.append((v[i][0]*-1,v[i][1]*-1))

    return respuesta
        
def ProductoEscalarVector(c,v):

    respuesta = []

    for i in range(len(v)):
        respuesta.append(Librería_números_complejos.Producto(c,v[i]))

    return respuesta

def SumaMatriz(matriz1, matriz2):

    respuesta = []

    for i in range(len(matriz1)):
        respuesta.append(SumaVector(matriz1[i],matriz2[i]))

    return respuesta

def InversaMatriz(matriz):

    respuesta = []

    for i in range(len(matriz)):
        respuesta.append(InversoVector(matriz[i]))

    return respuesta

def ProductoEscalarMatriz(c,matriz):

    respuesta = []

    for i in range(len(matriz)):
        respuesta.append(ProductoEscalarVector(c,matriz[i]))
    
    return respuesta

def MatrizTranspuesta(matriz):

    respuesta = []
    
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        respuesta.append(fila)

    return respuesta

def MatrizConjugada(matriz):

    respuesta = []

    for i in range(len(matriz)):
        conjugado = []
        for j in range(len(matriz[i])):
            conjugado.append(Librería_números_complejos.Conjugado(matriz[i][j]))
        respuesta.append(conjugado)

    return respuesta

def MatrizAdjunta(matriz):

    respuesta = MatrizTranspuesta(matriz)
    respuesta = MatrizConjugada(respuesta)
    return respuesta

def AccionMatrizVector(matriz,vector):

    respuesta = []

    if len(matriz[0]) == len(vector):
        suma = (0,0)

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                temporal = Librería_números_complejos.Producto(matriz[i][j],vector[j])
                suma = Librería_números_complejos.Suma(temporal,suma)
                
            respuesta.append(suma)
            suma = (0,0)

        return respuesta
    else:
        return "Dimensiones incorrectas"
    
def NormaMatriz(matriz):

    respuesta = 0
    for i in (matriz):
        for j in i:
            respuesta += (j[0])**2
            respuesta += (j[1])**2

    return respuesta**0.5

def DistanciaMatriz(matriz1,matriz2):
    
    respuesta = 0
    
    for i in range(len(matriz1)):
        for j in range(len(matriz1[i])):
            valor = Librería_números_complejos.Resta(matriz1[i][j],matriz2[i][j])
            respuesta += valor[0]**2 + valor[1]**2
    
    return respuesta**0.5

def matrizmultiplication(matriz1, matriz2):
    
    filasMatriz2 = len(matriz2)
    columnasMatriz1 = len(matriz1[0])
    
    if filasMatriz2 == columnasMatriz1:
        filas = len(matriz1)
        columnas = len(matriz2[0])
        matriz = [[(0, 0)] * columnas for x in range(filas)]
        
        for i in range(0, filas):
            for j in range(0, columnas):
                for k in range(0, len(matriz2)):
                    m = Librería_números_complejos.Producto(matriz1[i][k], matriz2[k][j])
                    n = matriz[i][j]
                    matriz[i][j] = (m[0]+n[0], m[1]+n[1])
                    
    return matriz

def MatrizIdentidad(fila,columna):

    identidad = [[(0,0)]*fila for i in range(columna)]

    for i in range(fila):
        for j in range(columna):

            if i==j:
                identidad[i][j] = (1,0)

    return identidad
    
def RevisarUnitaria(matriz):
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    if filas == columnas:
        transpuesta = MatrizTranspuesta(matriz)
        matriz = matrizmultiplication(matriz,transpuesta)
        identidad = MatrizIdentidad(len(matriz),len(matriz[0]))

        if matriz == identidad:
            return True
        
        else: return False
    
def MatrizHermitania(matriz):

    if matriz == MatrizAdjunta(matriz):
        return True
    else: return False

def ProductoTensor(dato1,dato2):

    respuesta = []
    control = 0
    posicioni = 0
    posicionj = 0

    while (posicioni < (len(dato1)-1)*2):
        fila1 = dato1[posicioni]
        fila2 = dato2[posicionj]
        fila = []
        
        for i in fila1:
            for j in fila2:
                fila.append(Librería_números_complejos.Producto(i,j))
        
        posicionj += 1
        fila2 = dato2[posicionj]
        respuesta.append(fila)
        fila = []
        
        for i in fila1:
            for j in fila2:
                fila.append(Librería_números_complejos.Producto(i,j))
                
        posicioni += 1
        posicionj -= 1
        respuesta.append(fila)
   
    return respuesta
            

    
