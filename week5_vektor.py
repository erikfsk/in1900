import numpy as np

def h(x):
    return x/10.

n = 41
#loop
x_array = np.linspace(-4,4,n)
y_array = np.zeros(n)
for i in range(n):
	y_array[i] = h(x_array[i])

#vectorized
x_array2 = np.linspace(-4, 4, n)
y_array2 = h(x_array2)

print x_array2 == x_array
print y_array2 == y_array