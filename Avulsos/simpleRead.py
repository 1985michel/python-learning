

file = open("fruits.txt","r")
content = file.read()

#observe que content e uma unica string
print(type(content))

#voltando ao comeco
file.seek(0)

#lendo novamente linha por linha dessa vez
content = file.readlines()

#observe que agora cada linha forma uma string de uma lista
print(type(content))

for x in content:
	print(len(x))

file.close()