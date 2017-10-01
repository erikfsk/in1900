from numpy.lib.scimath import sqrt
import numpy

def funksjon(x):
    return 2*x

def test_funksjon():
    computed = funksjon(10) #pcen regner for oss
    forventet = 20 #manuelt
    assert forventet == computed 
    print "INGEN FEIL"


test_funksjon()

tol = 1
forventet = 20
computed = funksjon(10)
#assert
if abs(forventet-computed) < tol:
    None
else:
    exit("Assertion error: ....")