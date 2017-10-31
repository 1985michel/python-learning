file=open("file01.txt","w")
l =[1,2,3]

for x in l:
	file.write(str(x)+"\n")

file.close()

"""
r reads
r+ read and write
w write
w+ write and read 
a append
a+ append and read

"""