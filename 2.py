list2=[]
sum=0
with open("test.txt") as f:
	list=f.readlines()
	for i in list:
		list2.append(i.split())
	for i in range(0,len(list2)):
		sum=sum+len(list2[i])
	print("Number of words in file:", sum)
	f.close()
