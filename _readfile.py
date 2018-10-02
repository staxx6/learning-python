fobj = open("testdict.txt", "r") #"r" for read file

wordDict = {}

for line in fobj:
    word = line.split(" ") # left side is english word in right the german
    wordDict[word[0]] = word[1]

fobj.close()

print(wordDict)