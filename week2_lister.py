t = []
y = []

for i in range(11):
    t.append(i)
    y.append(i**2)

ty1 = [t,y]
ty2 = [[i,j] for i,j in zip(t,y)]

for tmp in range(len(ty1[0])):
    print ty1[0][tmp],ty1[1][tmp] 



print "t",t
print "y",y
print "ty1",ty1
print "ty2",ty2