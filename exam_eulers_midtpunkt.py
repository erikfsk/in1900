from numpy import *
from matplotlib.pyplot import * 


def derivert(x):
    return x    



def eulers_method_midtpunkt_punkter(a,b,N):
    x_step = float(b-a)/N
    x = [a]
    y = [1]
    for i in range(1,N+1):
        x.append(x[-1] + x_step)
        y_midt = y[-1] + x_step*0.5*derivert(y[-1])
        y.append(y[-1] + x_step*derivert(y_midt))
    return x,y

x,y = eulers_method_midtpunkt_punkter(0,10,200) #x_start,x_slutt,linspace
plot(x,y,"r-")
plot(x,exp(x),"g-")
show()

print y[-1]/exp(x[-1])


