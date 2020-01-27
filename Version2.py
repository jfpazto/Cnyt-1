import math
'''Esta libreria se encarga de realizar diferentes operaciones para los numeros
complejos , las cuales son: Suma, Resta, Multiplicaion, Division, Conjugado, Modulo,
Fase, Conversión entre representaciones polar y cartesiano'''
def suma(arr1,arr2):
    '''Esta funcion recibe dos arreglos de la forma[a,bi] y retorna el resultado de la forma[a,bi]'''
    return [int(arr1[0])+int(arr2[0]),int(arr1[1])+int(arr2[1])]
def resta(arr1,arr2):
    '''Esta funcion recibe dos arreglos de la forma[a,bi] y retorna el resultado de la resta en la forma[a,bi]'''
    return [int(arr1[0])-int(arr2[0]),int(arr1[1])-int(arr2[1])]
def multiplicacion(arr1,arr2):
    '''Esta funcion recibe dos arreglos de la forma[a,bi] y retorna el resultado de la multiplicacion en la forma[a,bi]'''
    return [(int(arr1[0])*int(arr2[0]))-(int(arr1[1])*int(arr2[1])),(int(arr1[0])*int(arr2[1]))+(int(arr1[1])*int(arr2[0]))]
def conjugado(arr1):
    '''Esta funcion recibe un arreglo de la forma [a,bi] y retorna el resultado de su conjugado
       en la forma [a,-bi]'''
    return [int(arr1[0]),int(arr1[1])*-1]
def division(arr1,arr2):
    '''Esta funcion recibe dos arreglos de la forma[a,bi] y retorna el resultado de la division en la forma[a,bi]'''
    conju=conjugado(arr2)
    divisor=multiplicacion(arr1,conju)
    dividendo=multiplicacion(arr2,conju)
    if dividendo[0] != 0:
        return [divisor[0]/dividendo[0],divisor[1]/dividendo[0]]
    else:
        print("ERROR, no se puede dividir por cero")
def modulo(arr1):
    '''Esta funcion recibe un arreglo de la forma [a,bi] y retorna su modulo'''
    return [math.sqrt(int(arr1[0])**2+int(arr1[1])**2)]
def Bin_polar(arr1):
    '''Esta funcion recibe un arreglo calcula su fase y la retorna'''
    mod=modulo(arr1)
    direc=math.atan(arr1[1]/arr1[0])
    return [mod[0],round(math.degrees(direc),2)]
def polar_Bin(arr1):
    '''Esta funcion recibe un arreglo de la forma [r,el angulo en°]
    y retorna el valor del numero complejo de forma Binomial'''
    a=arr1[0]*math.cos(math.radians(arr1[1]))
    b=arr1[0]*math.sin(math.radians(arr1[1]))
    imprime([round(a,2),round(b,2)])
def ele_n(arr1,n):
    '''Esta funcion recibe un arreglo de la forma[a+bi,"n" el numero del exponente]
    y retorna el valor de elevar un numero complejo a la n'''
    polar=Bin_polar(arr1)
    polar_Bin([round(polar[0]**n,2),round(polar[1]*n,2)])
def imprime(arreglo):
    print("El numero es:",arreglo[0],"+",str(arreglo[1])+"i")
def fase(arr1):
    angulo=math.degrees(math.atan2(arr1[1],arr1[0]))
    print("La fase del numero es:",str(round(angulo,2))+"°")



