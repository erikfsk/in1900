def read_file(dat_file="test_test.txt"):
	liste = []


	infile = open(dat_file,"r")
	variabel = float((infile.readline().split())[-1])
	infile.readline() 							#hopp over en linje	 
	lines = infile.readlines() #Dette er en liste, hvor hvert element er en linje i filen
	infile.close()


	for line in lines:
		words = line.split() #Dette er en liste, hvor hvert element er et ord paa en linje
		for word in words:
			liste.append(float(word))
	

	return variabel,sorted(liste) #sorter t med engang...


def test_read_file():
	#lag en test fil
	with open("test_test.txt","w") as outfile:
		outfile.write("variabel: 10\nelementer:\n1 2 3\n4 5")

	#hva forventer du?
	tol = 10E-5
	expected_var = 10.0
	expected_liste = [1.0,2.0,3.0,4.0,5.0] 

	computed_var,computed_liste = read_file()


	assert abs(computed_var-expected_var) < tol
	
	#godkjent
	assert computed_liste == expected_liste

	#dette er veldig bra :) 
	for computed_i,expected_i in zip(computed_liste,expected_liste):
		assert abs(computed_i-expected_i) < tol

def write_file(out_file="test_result.txt"):
	var,liste = read_file()
	with open(out_file,"w") as outfile:
		outfile.write("x     y\n")
		for liste_element in liste:
			outfile.write("%.1f   %.1f\n" % (liste_element,liste_element*var))

if __name__ == '__main__':
	test_read_file()
	write_file()



