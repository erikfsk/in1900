def trapes(f,a,b,N):
    s = f(a) + f(b)
    step = (b-a)/float(N)
    for i in range(1,N):
        s += 2*f(a+(i*step))
    return s*(step/2.)



def test_trapes(c,d):
    forventet = 2.0
    def f(x,c_=c,d_=d):
        return c_*x + d_
    kalkulert = trapes(f,0,2,2**5)
    tol = 1e-8
    success = abs(forventet - kalkulert) < tol 
    msg = "forventet = %g     kalkulert = %g" % (forventet,kalkulert)
    assert success,msg


test_trapes(1,0)



from math import factorial,exp


def f_k(x_a,k):
    return (x_a+k)*exp(x_a)


def taylor_generell(x,n,a=0):
    s = 0
    for k in range(0,n+1):
        s += f_k(a,k)/factorial(k) * (x-a)**k
    return s


def taylor(x,n):
    s = 0
    for k in range(1,n+1):
        s += float(x)**k/factorial(k-1)
    return s

def test_taylor():
    forventet = exp(1)
    kalkulert = taylor(1,7) # en eller annen N fra B. jeg vet ikke!
    tol = 0.001000000001 # 0.001 for taylor tilnarming 0.00000001 for numerisk feil pa pc
    success = abs(forventet - kalkulert) < tol
    msg = "forventet = %g     kalkulert = %g" % (forventet,kalkulert)
    assert success,msg

test_taylor()



from numpy import *
from matplotlib.pyplot import *

def funk(x):
    return x**2

def funk_derivert(x):
    return 2*x



def eulers_method_2(x,f_derivert):
    y = [funk(0)]
    for i in range(1,len(x)):
        y.append(y[-1] + (x[1]-x[0])*f_derivert(x[i-1]))
    return y


def eulers_method(x_start,x_slutt,N,f_derivert):
    x = linspace(x_start,x_slutt,N)
    y = zeros(N)
    for i in range(1,len(x)):
        y[i] = y[i-1] + ((x[1]-x[0])*f_derivert(x[i-1])) 
    return x,y
print eulers_method(0,20,10,funk_derivert)

x,y= eulers_method(0,20,10,funk_derivert)
plot(eulers_method(0,20,10,funk_derivert))
plot(x,y,"r-")
plot(x,funk(x),"g-")
show()























































