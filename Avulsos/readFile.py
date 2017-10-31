



def openFile(arquivo):
	file = open(arquivo,"r")#open a file on the same directory  
	return file

def readingAFile(file):
	content = file.read()
	return content 
  

def closeTheFile(file):
	file.close()

#Put the pointer in the begining of the file again
def backToBegining(file):
	file.seek(0)

#removendo caracteres indedejados
def removeUnwishedChars(lista):
	result = [i.rstrip("\n") for i in lista]
	return result


arquivo = "fruits.txt"
file = openFile(arquivo)
content = readingAFile(file)
print(content)
#closeTheFile(file)

print("Lendo novamente")
print(file.readlines())
print content#nao imprime nada pq o ponteiro esta no final do arquivo

print("Lendo mais uma vez")
backToBegining(file)
content = file.readlines()
print(content)

print("\n"*3)
print("removendo caracteres indedejados")
content = removeUnwishedChars(content)
print content

closeTheFile(file)
