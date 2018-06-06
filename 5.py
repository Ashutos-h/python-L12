#Answer 5
import random
list=[]
f=open('random.txt','w')

print("Generating 10 random numbers and writing them in file: \n")
for i in range(10):
        num=random.randint(1,100)
        f.write(str(num)+"\n")
f.close()

f1=open('random.txt','r+')

list= f1.read().splitlines()
print("Content of file: \n")
print(list)
      
for i in range(len(list)):
	list[i]=int(list[i])

list.sort()

f2=open('sorted.txt','w')

for i in range(len(list)):
	f2.write(str(list[i])+"\n")

f2.close()

f2=open('sorted.txt','r+')
print("Reading the sorted content: ")
data=f2.read()
print(data)

f.close()
f1.close()
f2.close()
