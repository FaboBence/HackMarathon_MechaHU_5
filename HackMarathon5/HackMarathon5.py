from copy import deepcopy

# Closed part
def create_path(word, dictionary):
	lista = [word]
	puffer=[dictionary[word]]
	while True:
		if len(dictionary[lista[-1]])>0 and dictionary[lista[-1]][0] not in lista:
			lista.append(dictionary[lista[-1]][0])
		else:
			break
	return lista

def attacher(words_in_a_list):
	tmp = words_in_a_list[0]
	for i in range(1,len(words_in_a_list)):
		for j in range(1,1+min(len(tmp),len(words_in_a_list[i]))):
			if tmp[-j:] == words_in_a_list[i][:j]:
				tmp += words_in_a_list[i][j:]
	return tmp

def recursive(dictionary,list_of_words,longest = []):
	skipped = 0
	for word in dictionary[list_of_words[-1]]:
		if word in list_of_words:
			skipped += 1
			continue
		cpy = deepcopy(list_of_words)
		cpy.append(word)
		ret = recursive(dictionary, cpy, longest)
		if len(longest) < len(ret):
			longest = deepcopy(ret)

	if skipped == len(dictionary[list_of_words[-1]]):
		if len(list_of_words) > len(longest):
			longest = deepcopy(list_of_words)
		elif len(list_of_words) == len(longest) and len(attacher(list_of_words)) < len(attacher(longest)):
			longest = deepcopy(list_of_words)
		
	return deepcopy(longest)

def recursive_2(list_of_words, longest = []):
	skipped = 0
	hova = []
	str_of_words = attacher(list_of_words)
	for i in words:
		if str_of_words != i:
			for j in range(1,1+min(len(str_of_words),len(i))): # j: hány betűt nézünk meg
				if str_of_words[-j:] == i[:j]:
					hova.append(i)
					break
	#stop = 0
	for word in hova:
		if word in list_of_words:
			skipped += 1
			continue
		cpy = deepcopy(list_of_words)
		cpy.append(word)
		ret = recursive_2(cpy, longest)
		if len(ret) > len(longest):
			longest = deepcopy(ret)
		elif len(ret) == len(longest) and len(attacher(list_of_words)) < len(attacher(longest)):
			longest = deepcopy(ret)
		
	if skipped == len(hova):
		if len(list_of_words) > len(longest):
			longest = deepcopy(list_of_words)
		elif len(list_of_words) == len(longest) and len(attacher(list_of_words)) < len(attacher(longest)):
			print('   longest: '+attacher(longest))
			longest = deepcopy(list_of_words)
			print('   replace: '+attacher(longest))
		
	return deepcopy(longest)

words = ["blood", "zonked", "rush", "writer", "grate", "ignorant", "cloudy", "chicken", "illness", "useless", "challenge", "comfortable",
		 "noxious", "desk", "shade", "error", "great", "flagrant", "cute", "plan", "daughter", "dare", "giraffe",
		 "airplane", "aunt", "men", "vase", "cheap", "obsolete", "tomatoes", "receipt", "festive", "screeching",
		 "moor", "ingredients", "great", "skill", "us", "expansion", "rex", "lesson", "one", "nemo", "sack"]

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

# Searching for the longest concatenation
print()
for i,firstword in enumerate(words):
	kiir.append([firstword])
	#kiir[i] = recursive(dictionary, kiir[i])
	kiir[i] = recursive_2(kiir[i])

	# Kiiratás
	print(len(kiir[i]), attacher(kiir[i]))