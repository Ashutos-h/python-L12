#Answer 4
i=0
j=0
with open("test.txt") as f1,open("ashu.txt") as f2:
	list1=f1.read().splitlines()
	list2=f2.read().splitlines()
	if(len(list1)==len(list2)):
		for i in range(len(list1)):
			print(list1[i]+" "+list2[i])
	elif(len(list1)<len(list2)):
		for i in range(len(list1)):
			print(list1[i]+" "+list2[i])
		for j in range(len(list1),len(list2)):
			print(list2[j])
	else:
		for i in range(len(list2)):
			print(list1[i]+" "+list2[i])
		for j in range(len(list2),len(list1)):
			print(list1[j])
	f2.close()
	f1.close()
	
		
	
	
