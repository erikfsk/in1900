#tenk igjennom hva du tror dette programmet skriver ut.  

#a
for i in range(5):
	print i,

for i in range(0,5,1):
	print i,

#b
i = 0
while i < 5:
	print i,
	i += 1

#c
if 1 == 1:
	print True
elif 1 > 2:
	print False


#d
assert True 
assert 1 == 1

#e
try:
	assert False
	assert 1 == 2 # blir denne brukt?
except AssertionError:
	print "AssertionError"

#f
argument_global	= 500
argument = 500

def test_funksjon(argument_lokal,argument):
	argument = 100
	argument_lokal = 100
	return argument_lokal

test_funksjon(100,100)


print argument # hvilken verdi har argument? 
print argument_global 

#g
try:
	print argument_lokal
except NameError:
	print "argument_lokal er en lokal variabel som kun eksisterer i test_funksjon"


#h
x = range(1, 17, 5)
y = x
if_statement_og_x_y_verdier = [[x_ != y_ and x_ > y_ + 1, [x_,y_]] for x_ in x[1:-1] for y_ in y[1:-1]]
print if_statement_og_x_y_verdier


#i
from numpy import *
x = zeros(1)
print e**x[0],e**x
x = linspace(0,5,6)
print x

#j
outfile = open("test_test.txt","w")
outfile.write("hello world 3")
outfile.close()
if type(outfile)==type(1337):
	print outfile

#k
with open("test_test.txt","r") as infile:
	words = infile.readline().split()
	print words[2]

#l
try:
	infile.read()
	print True
except:
	None

#m
x = [0 for i in range(3)]
y = [j for j in x]
print x + y

#n
from numpy import *
x = zeros(3)
y = zeros(3)

print x + y

#o
def h(x): return 1 if x >= 0 else 0

x = [0,-1,-2]
y = [0,1,2]

for x_i,y_i in zip(x,y):
	print h(x_i),h(y_i)

#p
if True == True: print True,True
if True == False: print True,False
if False == True: print False,True
if False == False: print False, False

#q
success_1 = 1337 < 117
success_2 = 2 == abs(-2)
success_3 = type(1337.0) == type(117)
success_4 = type(1337) == type(117)

if success_2 == success_4: print "success_2 %s, success_4 %s" % (success_2,success_4)
if success_2 == success_3: print "success_2 %s, success_3 %s" % (success_2,success_3)
if success_1 == success_4: print "success_1 %s, success_4 %s" % (success_1,success_4)
if success_1 == success_3: print "success_1 %s, success_3 %s" % (success_1,success_3)