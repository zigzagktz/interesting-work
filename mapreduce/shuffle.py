

def shuffle():
	import sys
	import ast
	file = open('out.txt',"r")
	sys.stdout = open("intermediate.txt", 'w')

	lst=[]

	for w in file.readlines():
		lst.append(ast.literal_eval(w.strip("\n")))

	lst = sorted(lst)
	lst  = [str(x) for x in lst]

	for i in lst:
		print(i)

if __name__ == "__main__":
	shuffle()