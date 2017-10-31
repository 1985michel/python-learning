import json
data = json.load(open("data.json"))#ou ("data.json","r") mas o r ja e default
type(data)#print dictionary
#print(data) #imprime tudo
#print(data["rain"]) #imprime a definicao de rain
print(len(data))
print(data["woman"])

#verificando se uma determinada palavra consta no dicionario
print("boy" in data)#true
print("cebola" in data)#false



def translate(word):
	word = word.lower()
	if(word in data):
		return data[word]

	match = bestMatch(word)
	if(len(match)>0):
		print("Did you mean: %s ?" %match[0]) #é necessário dizer que se quero primeiro pq é uma lista
		if input("'Y' or 'N': ") == 'Y':
			return data[match[0]]
		else:
			return "Try again"
		#for d in data:
			 #if(compareTwoStrings(word,d) >0.8):
			  	#return("Do you mean: "+d+" ?") 
	else:
		return("This word doesn't exist, try again.")


#import difflib
from difflib import SequenceMatcher

def compareTwoStrings(a,b):
	return SequenceMatcher(None, a,b).ratio()



#print(translate("meal"))
#print(translate("Fejoada"))

#testando agora com uma palavra com caps

#print(translate("rain"))
#print(translate("RAIN"))
#print(dir(str))#apresentar os atributos e métodos

#https://docs.python.org/3/library/
#para ver as bibliotecas do python



from difflib import get_close_matches
#help(get_close_matches)#para obter ajuda sobre um método

def bestMatch(word):
	return get_close_matches(word,data.keys(),1)
	#pass
#print(bestMatch("rainn"))

#print(dir(dict))

#print(translate("maria"))
print(translate(input("What word do you want to define? ")))

print(translate)
exit()