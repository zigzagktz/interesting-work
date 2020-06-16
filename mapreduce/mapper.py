

def somefunc(): 
	import sys
	sys.stdout = open("out.txt",'w')
	
	filename = open(input(),"r")
	
	for line in filename.readlines():
		try: 
			lst = line.strip()
			lst = line.split()
			lst = list(map(lambda x:(x,1),lst))
			for w in lst:
				print(w)
		except:
			break
			
if __name__ == "__main__":
	somefunc()
