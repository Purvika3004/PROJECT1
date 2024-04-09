f=open("demo.txt","r")
content=f.read() 
print(content)
f.close()

n = int(input("Enter Lines To Read: "))
f = open("demo.txt","r")
for i in range(n):
	print(f.readline())


f=open("demo.txt","r")
content=f.readline() 
print(content)
f.close()

