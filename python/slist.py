with open("stud.txt")as f:
	slist=f.readlines()
	print (slist)
slist=[x.strip() for x in slist]
print("The content of the file are:",slist)

