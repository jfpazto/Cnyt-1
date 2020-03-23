import matplotlib.pyplot as plt
import math


def conjugado(c_1):
    """
    La función recibe un número complejo c_1 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion conjugado c_1.
    """
    return (c_1[0],(c_1[1]*(-1)))

def sumaVec(el1,el2):
    resul = [0,0]
    resul[0] = el1[0] + el2[0]
    resul[1] = el1[1] + el2[1]
    return (resul[0],resul[1])

def realiza_multiplicacion(vec1,vec2):
    '''recibe dos matrices y realiza la multiplicacion'''
    lista = [0,0,0,0]
    res = [0,0] 
    con = 0
    for i in vec1:
        for j in vec2:
            lista[con] = i*j
            con += 1        
    res[0] = lista[0] + (-1*lista[3]) 
    res[1] = lista[1] + lista[2]
    return (res[0],res[1])

def Bin_polar(c_1):
    '''Esta funcion recibe un arreglo calcula su fase y la retorna'''
    mod=modulo(c_1)
    direc=math.atan(c_1[1]/c_1[0])
    return [mod[0],round(math.degrees(direc),2)]

def polar_Bin(c_1):
    '''Esta funcion recibe un arreglo de la forma [r,el angulo en°]
    y retorna el valor del numero complejo de forma Binomial'''
    a=c_1[0]*math.cos(math.radians(c_1[1]))
    b=c_1[0]*math.sin(math.radians(c_1[1]))
    imprime([round(a,2),round(b,2)])
def ele_n(c_1,n):
    '''Esta funcion recibe un arreglo de la forma[a+bi,"n" el numero del exponente]
    y retorna el valor de elevar un numero complejo a la n'''
    polar=Bin_polar(c_1)
    polar_Bin([round(polar[0]**n,2),round(polar[1]*n,2)])
def imprime(arreglo):
    print("El numero es:",arreglo[0],"+",str(arreglo[1])+"i")
    
def division(c_1,c_2):
    """
    La función recibe dos números complejos c_1 y c_2 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion c_1 / c_2.
    """
    conjugado = [c_2[0],(c_2[1]*(-1))]
    divisor=producto(c_1,conjugado)
    dividendo= producto(c_2,conjugado)
    if c_2[0] != 0 :
        return [int(divisor[0][0])/int(dividendo[0][0]),int(divisor[1][0])/int(dividendo[0][0])]
    else:
        print("error no se puede divisir por 0")
def multiplicacionVec(vec1,vec2):
    '''recibe dos vectores y realiza su multiplicacion'''
    ini = (0,0)
    longitud=len(vec1)
    con=0
    while con!=longitud:
        suma = realiza_multiplicacion(vec1[con],vec2[con])
        ini = sumaVec(ini,suma)
        con+=1

    return ini


def accionMat(vec1,mat1):
    lista = []
    longitud=len(mat1)
    con=0
    while con!=longitud:
        lista.append(multiplicacionVec(vec1,mat1[con]))
        con+=1
    return lista


def MatrizporVector(vec1,mat1):
    '''Recibe un vector y una matriz y realiza su multiplicacion'''
    lista = [] 
    for i in range(len(mat1)):
        suma = 0
        for j in range(len(mat1[i])):
            mult= mat1[i][j]*vec1[j]
            suma += mult
        lista.append(suma)
    return lista 


def producto_tensor(mat1,mat2):
    '''Realiza el producto tensor de dos matrices'''
    matriz = []
    for i in range(len(mat1)):
        final = [[]] *len(mat2)
        for j in range(len(mat1[i])):
            res = matriz_escalar(mat1[i][j],mat2)
            for k in range(len(mat2)):
                final[k] = final[k] + res[k]
        for k in range(len(mat2)):
            matriz.append(final[k])
    return matriz


def producto_tensor_vec(vec1,vec2):
    '''Realiza el producto tensor de dos vectores'''
    res = [0 for i in range(len(vec1)*len(vec2))]
    con = 0
    for i in range(len(vec1)):
        lista = vector_escalar(vec1[i],vec2)
        for k in range(len(lista)):
            res[con] = lista[k]
            con+=1
    return res


def matriz_escalar(num,mat1):
    matriz=[]
    for i in range(0,len(mat1)):
        vector=[]
        for j in range(0,len(mat1[0])):
            vector.append(realiza_multiplicacion(mat1[i][j],num))
        matriz.append(vector)
    return matriz

def vector_escalar(num,mat1):
    matriz=[]
    for i in range(0,len(mat1)):
            matriz.append(realiza_multiplicacion(mat1[i],num))
    return matriz


def clasico_dinamico(clicks):
 
    matriz = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(1/2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(1/2,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
    [(0,0),(1/3,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
    [(0,0),(1/3,0),(0 ,0),(0 ,0),(1,0),(0,0),(0,0),(0,0)],
    [(0,0),(1/3,0),(1/3,0),(0,0),(0,0),(1,0),(0,0),(0,0)],
    [(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(1,0),(0,0)],
    [(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(0,0),(1,0)]]
    
     
    vector_inicial=[[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]    
    estado = vector_inicial
    
    for i in range(clicks):
        estado = accionMat(estado,matriz)
        
    titulo = plt.figure('Sistema dinamico despues de 2 clicks Tiempo') # Figure
    titulo1 = titulo.add_subplot(111) # Axes

    nombres_ejex = ['P.0','P.1','P.2','P.3','P.4','P.5','P.6','P.7']
    datos = [estado[0][0],estado[1][0],estado[2][0],estado[3][0],estado[4][0],estado[5][0],estado[6][0],estado[7][0]]
    num_datos = range(len(datos))

    titulo1.bar(num_datos, datos, width=0.5, align='center')
    titulo1.set_xticks(num_datos)
    titulo1.set_xticklabels(nombres_ejex)

    plt.show()
    return estado


#------------------------------------Dinamica Sistema Probabilistico---------------------------------------------------#
'''def sistemaProbabilistico(clicks):
    # Matriz de la dinámica para el sistema probabilístico A
    MA = [[[0,0],[0.2,0],[0.3,0],[0.5,0]],
      [[0.3,0],[0.2,0],[0.1,0],[0.4,0]],
      [[0.4,0],[0.3,0],[0.2,0],[0.1,0]],
      [[0.3,0],[0.3,0],[0.4,0],[0,0]]]
    # Matriz de la dinámica para el sistema probabilístico B
    MB = [[[0,0],[1/6,0],[5/6,0]], 
      [[1/3,0],[1/2,0],[1/6,0]], 
      [[2/3,0],[1/3,0],[0,0]] 
     ]
    # Vector de estado inicial sistema probabilístico A
    VA = [[0.2,0],[0.1,0],[0.6,0],[0.1,0]]
    # Vector de estado inicial sistema probabilístico B
    VB = [[0.7,0],[0.15,0],[0.15,0]]
    m1 = producto_tensor(MA,MB)
    vectorI= producto_tensor_vec(VA,VB)
    estado = vectorI
    for i in range(clicks):
        estado = accionMat(estado,m1)
    fig = plt.figure(u'Evolucion Dinamica del Sistema ensamblado A-B despues de 5 clicks de tiempo') # Figure
    ax = fig.add_subplot(111) # Axes

    nombres = ['00','01','02','10','11','12','20','21','22','30','31','32']
    datos = [estado[0][0],estado[1][0],estado[2][0],estado[3][0],estado[4][0],estado[5][0],estado[6][0],estado[7][0],estado[8][0],estado[9][0],estado[10][0],estado[11][0]]
    xx = range(len(datos))

    ax.bar(xx, datos, width=0.5, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)

    plt.show()
    return estado
#Sistema probabilistico despues de 5 clicks de tiempo 
sistemaProbabilistico(5)'''
