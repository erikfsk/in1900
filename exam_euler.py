from numpy import *
from matplotlib.pyplot import * 



def derivert(x):
    return x    



def eulers_method_list(x):
    y = [1]
    for i in range(1,len(x)):
        y.append(y[-1] + (x[1] - x[0])*derivert(y[-1]))
    return y


x_start = 0; x_slutt = 10; N = 200
x = linspace(x_start,x_slutt,N)

plot(x,eulers_method_list(x),"r-")
plot(x,exp(x),"g-")
show()


def eulers_method_punkter(a,b,N):
    x_step = float(b-a)/N
    x = [a]
    y = [1]
    for i in range(1,N+1):
        x.append(x[-1] + x_step)
        y.append(y[-1] + x_step*derivert(y[-1]))
    return x,y

x,y = eulers_method_punkter(0,10,200) #x_start,x_slutt,linspace
plot(x,y,"r-")
plot(x,exp(x),"g-")
show()


def eulers_method_punkter(a,b,N):
    x_step = float(b-a)/N
    x = [a]
    y = [0]
    vy = [0]
    for i in range(1,N+1):
        x.append(x[-1] + x_step)
        y.append(y[-1] + x_step*vy[-1])
        vy.append(vy[-1] + x_step*(-9.81))
    return x,y,vy

x,y,vy = eulers_method_punkter(0,10,200) #x_start,x_slutt,linspace
plot(x,y,"r-")
plot(x,vy,"g-")
show()




