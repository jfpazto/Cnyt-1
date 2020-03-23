import math

def Fase(c1):
  
    if c1[0] != 0:
        angulo = math.atan2(c1[1],c1[0])
    else:
        print("No se puede dividir en cero",c1)

    return math.degrees(angulo)

def ConverPolaCarte(a,b):

    ParteReal = a*math.cos(b)
    ParteImagi = a*math.sin(b)

    return (ParteReal,ParteImagi)
    
def ConverCartePola(c1):
    
    if c1[0] != 0:
        p = (c1[0]*c1[0] + c1[1]*c1[1])**(1/2)
        angulo = math.atan(c1[1]/c1[0])
    else:
        print("No se pede dividir entre cero",c1)

    return (p,math.degrees(angulo))
    
def Conjugado(complejo1):

    #complejo1[1] *= -1
    ParteReal = complejo1[0]
    ParteImagi = complejo1[1]
    #complejo1[1] *= -1

    return (ParteReal,-1*ParteImagi)
    
def Modulo(c1):

    modulo = (c1[0]*c1[0] + c1[1]*c1[1])**(1/2)

    return modulo
    
def Division(c1,c2):

    NumerReal = c1[0]*c2[0] + c1[1]*c2[1]
    DenomReal = c2[0]*c2[0] + c2[1]*c2[1]
    ParteReal = NumerReal/DenomReal
    NumerImagi = c2[0]*c1[1] - c1[0]*c2[1]
    DenomImagi = c2[0]*c2[0] + c2[1]*c2[1]
    ParteImagi = NumerImagi/DenomImagi
    
    return (ParteReal,ParteImagi)
    
def Resta(c1,c2):

    ParteReal = c1[0] - c2[0]
    ParteImagi = c1[1] - c2[1]
    return (ParteReal,ParteImagi)
    
def Producto(c1,c2):

    ParteReal = c1[0]*c2[0]-c1[1]*c2[1]
    ParteImagi = c1[0]*c2[1]+c1[1]*c2[0]

    return (ParteReal,ParteImagi)
    
def Suma(c1,c2):

    ParteReal = c1[0] + c2[0]
    ParteImagi = c1[1] + c2[1]

    return (ParteReal,ParteImagi)

