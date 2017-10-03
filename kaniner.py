from numpy import *
from matplotlib.pyplot import *

def kaniner(food,months):
	f_left = arange(food, (food -2*months),-2)
	r = ones(months)

	for i in range(2,months):
		r[i] = r[i-1] + r[i-2]
		if food - 2*sum(r[:i]) > 0:
			f_left[i] = food - 2*sum(r[:i])
		else:
			r[i] = (food - 2*sum(r[:i-1]))/2. 
			f_left[i:] = 0
			r[i+1:] = 0
			break
			
	fasit = [food - 2*sum(r[:i]) if food - 2*sum(r[:i]) >= 0 else 0 for i in range(months)]
	return r,f_left,fasit

r, f_left,fasit = kaniner(200,12)
plot(r, "o-",label="rabbit population")
plot(f_left, "o-",label="food supply")
plot(fasit, "ro",label="FASIT")
xlabel("Months, n")
ylabel("Number of rabbits, r, in each month")
title("Fibonaccis rabbit growth simulation over 1 year")
legend()
show()