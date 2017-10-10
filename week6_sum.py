from numpy import *

x_list = [1,2,3,4,5,6,7,8,9]
x = linspace(1,9,9)
print(x)
print(x_list)

print(sum(x_list)) #works with list as well
print("sum-function sum:", sum(x*2 + 5))

summen = 0
for i in range(len(x)):
	summen += x[i]*2 + 5
print("for-loop sum: ",summen)
