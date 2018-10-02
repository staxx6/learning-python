fobj = open("testdict.txt", "r") #"r" for read file

wordDict = {}

for line in fobj:
    line = line.strip() # removes white space symbols, here the \n for new line
    word = line.split(" ") # left side is english word in right the german
    wordDict[word[0]] = word[1]

fobj.close()

while True:
    word = input("Type a word: ")
    if word in wordDict: # looks only the keys!
        print("The german word is:", wordDict[word])
    else:
        print("The word is not known")

print(wordDict) 