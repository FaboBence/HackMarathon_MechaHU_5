from copy import deepcopy

# Closed part

def attacher(words_in_a_list):
	tmp = words_in_a_list[0]
	for i in range(1,len(words_in_a_list)):
		for j in range(1,1+min(len(tmp),len(words_in_a_list[i]))):
			if tmp[-j:] == words_in_a_list[i][:j]:
				tmp += words_in_a_list[i][j:]
	return tmp

def recursive(dictionary,list_of_words,last_word):
	for word in dictionary[last_word]:
		recursive(list_of_words.append(word))

words = ["rush", "writer", "grate", "ignorant", "cloudy", "chicken", "illness", "useless", "challenge", "comfortable",
		 "noxious", "desk", "shade", "error", "great", "zonked", "flagrant", "cute", "plan", "daughter", "dare", "giraffe", 
		 "airplane", "aunt", "men", "blood", "vase", "cheap", "obsolete", "tomatoes", "receipt", "festive", "screeching",
		 "moor", "ingredients", "great", "skill", "us", "expansion", "rex", "lesson", "one", "nemo", "sack"]
def create_path(word, dictionary):
	lista = [word]
	puffer=[dictionary[word]]
	while True:
		if len(dictionary[lista[-1]])>0 and dictionary[lista[-1]][0] not in lista:
			lista.append(dictionary[lista[-1]][0])
		else:
			break
	return lista

attached = []
kiir = []
dictionary = {}

#init dict
for word in words:
	hova=[]
	for i in words:
		if word != i:
			for j in range(1,1+min(len(i),len(word))): # j: hány betűt nézünk meg
				if word[-j:] == i[:j]:
					hova.append(i)
					break
	dictionary[word]=hova
for kiiras in dictionary:
	print(kiiras, dictionary[kiiras])

#print(create_path(words[2],dictionary))
	

for i,firstword in enumerate(words):
	tmp_words = deepcopy(words) # List of words that have not been used
	attached.append(firstword)
	kiir.append([firstword]) # tmp
	tmp_words.remove(firstword)
	
	recursive(kiir[0])

	iteracio = 0
	while len(tmp_words)>0 and iteracio+1 < len(tmp_words): # Addig fut, amíg megtaláljuk a leghosszabb "összetett" szót
		for word in tmp_words:
			found = False
			for j in range(1,1+min(len(attached[i]),len(word))): # j: hány betűt nézünk meg
				if attached[i][-j:] == word[:j]:
					attached[i] += word[j:]
					kiir[i].append(word) # tmp
					tmp_words.remove(word)
					found = True
					break
			if found:
				break
		iteracio += 1
		if found:
			iteracio = 0

# Kiiratás
for i,word in enumerate(kiir):
	print(len(word), attacher(kiir[i]))
