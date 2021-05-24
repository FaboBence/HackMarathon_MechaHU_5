from copy import deepcopy

# Closed part

words = ["rush", "writer", "grate", "ignorant", "cloudy", "chicken", "illness", "useless", "challenge", "comfortable",
		 "noxious", "desk", "shade", "error", "great", "zonked", "flagrant", "cute", "plan", "daughter", "dare", "giraffe", 
		 "airplane", "aunt", "men", "blood", "vase", "cheap", "obsolete", "tomatoes", "receipt", "festive", "screeching",
		 "moor", "ingredients", "great", "skill", "us", "expansion", "rex", "lesson", "one", "nemo", "sack"]

attached = []
kiir = []
for i,firstword in enumerate(words):
	tmp_words = deepcopy(words) # List of words that have not been used
	attached.append(firstword)
	kiir.append(firstword) # tmp
	tmp_words.remove(firstword)
	
	iteracio = 0
	while len(tmp_words)>0 and iteracio+1 < len(tmp_words): # Addig fut, amíg megtaláljuk a leghosszabb "összetett" szót
		for word in tmp_words:
			found = False
			for j in range(1,1+min(len(attached[i]),len(word))): # j: hány betűt nézünk meg
				if attached[i][-j:] == word[:j]:
					attached[i] += word[j:]
					kiir[i] += ' ' + word # tmp
					tmp_words.remove(word)
					found = True
					break
			if found:
				break
		iteracio += 1
		if found:
			iteracio = 0

# Kiiratás
for word in kiir:
	print(word.count(" ")+1, word)
		
