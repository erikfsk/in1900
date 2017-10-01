#how to write to a file.
with open("test.txt","w") as outfile:
	outfile.write("test") #these two
	outfile.write("test") # lines are equal to the next line
	outfile.write("test\ntest") # just like with the print function. u can use \n here...


#just like a for loop. The indentation matters. 
#indentation to the left breaks the for-loop
for i in [1]:
	None
#break

#indentation to the left closes the file
with open("test.txt","r") as infile:
	None
#close

#two ways to open a file
#the first way is showed above
#the second way is below this

infile = open("test.txt","r")
infile.close() #remember to close the file

#you can use open with a r or w as the second input. 
#r stands for read
#W stands for write
#a stands for append (works just like a list)