#Answer 1

with open("test.txt") as f:
	list=f.readlines()
	n=int(input("Enter the line from where you want to read the file:"))
	for i in range(n-1,len(list)):
		print(list[i])
	f.close()	
