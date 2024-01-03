l=[]
l1=int(input("enter the limit:"))
for i in range(l1):
	l2=int(input("enter the numbers:"))
	l.append(l2)
print("smallest number of list =",min(l))
print("largest number of list =",max(l))
print ("The original list is : "+ str(l))
l = list(set(l))
print ("The list after removing duplicates : "+ str(l))

