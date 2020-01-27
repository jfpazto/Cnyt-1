import Version2 as c
import math
def test_suma():
    assert c.suma([5,2],[-8,3])==[-3,5],"Debe ser -3+5i"

def test_resta():
    assert c.resta([5,2],[4,-2])==[1,4],"Debe ser 1+4i"

def test_multiplicacion():
    assert c.multiplicacion([5,2],[2,-3])==[16,-11],"Debe ser 16-11i"

def test_division():
    assert c.division([3,2],[1,-2])==[-0.2,1.6],"Debe ser -1/5+8/5"

def test_conjugado():
    assert c.conjugado([4,2])==[4,-2],"Debe ser 4-2i"

def test_modulo():
    assert c.modulo([3,5])==[math.sqrt(34)],"Debe ser 5.830951"
def test_fase():
    
    assert c.fase([3,5])==[59.04],"Debe ser 5.830951"
def test_coor_cart_pola():
    assert c.Bin_polar([8,3])==[8.54400374531753, 20.56],"Debe ser"
def test_coor_pol_car():
    assert c.polar_Bin([2,135])==[8.54400374531753, 20.56],"Debe ser"

if __name__=='__main__':    
    test_suma()
    test_resta()
    test_multiplicacion()
    test_division()
    test_conjugado()
    test_modulo()
    print("Prueba exitosa")
