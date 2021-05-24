from copy import deepcopy

word1 = "train"
word2 = "inside"

ures = []
print(len(deepcopy(ures)))

listof = [word1,word2]
cpy = deepcopy(listof)
cpy.append(word1)

listof.append(word2)
print(cpy,listof)
print("salmon" in listof)

print(word1[-2:] == word2[:2])
word1 += word2[2:]
print(word1)

