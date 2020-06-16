

def runs():
	import sys
	import mapper
	import ast
	#mapper.somefunc()
	
	file = open('intermediate.txt',"r")
	sys.stdout = open("result.txt", 'w')
	
	lst=[]
	
	for w in file.readlines():
		lst.append(ast.literal_eval(w.strip("\n")))

	bucket = set(lst)
	
	second_list = []
	
	for i in bucket:
		second_list.append((i[0],lst.count(i)))
		
	second_list = sorted(second_list, key= lambda x:x[1], reverse= True)
	second_list= [str(x) for x in second_list]
	
	
	for i in second_list:
		print("".join(i))
	
		
if __name__ == "__main__":
	runs()