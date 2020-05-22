import sys 

inp = input("Hey please input a number: ")
syst = sys.argv[1]

print(syst, inp)

if(int(inp) == int(syst)):
		print("matched with sys args!!!")


