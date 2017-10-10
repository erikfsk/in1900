from matplotlib.pyplot import * 
from numpy import *


x_big = linspace(1,100,20)
x_small = linspace(0,1,100)

#NEI
plot(x_small,x_small*sqrt(x_small),"g-")
plot(x_big,x_big*sqrt(x_big),"ro-")
legend(["$\lambda_{small}$","$\lambda_{big}$"])
show()
#Notice that you can't see the small plot?


#JA
plot(x_small,x_small*sqrt(x_small),"g-")
legend(["$\lambda_{small}$"])
show()
plot(x_big,x_big*sqrt(x_big),"ro-")
legend(["$\lambda_{big}$"])
show()

#JA med litt breifing
subplot(2,1,1) 
# subplot(antall_bilder_i_y_retning ,antall_bilder_i_x_retning, aktivt_bilde)
# aktiv bilde teller bildene i forste rad fra venstre, saa neste rad fra venstre. osv. 
# altsa 1 vil si bilde 1 pa forste rad
# 2 vil si forste bilde pa andre rad, fordi vi bare har et bilde per rad. 
plot(x_small,x_small*sqrt(x_small),"g-")
legend(["$\lambda_{small}$"],loc="best")
subplot(2,1,2)
plot(x_big,x_big*sqrt(x_big),"ro-")
legend(["$\lambda_{big}$"],loc="best")
show()