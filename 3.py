#Answer 3
with open("test.txt") as f1, open("test2.txt","w") as f2:
	data = f1.read()
	f2.write(data)
	f1.close()
	f2.close()
with open("test2.txt") as f3:
	data1=f3.read()
	print("Content of 2nd file:")
	print()
	print(data1)
	

	
