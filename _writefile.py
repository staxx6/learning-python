dictCountries = {'Spain': 'Spanien', 'Germany': 'Deutschland', 'Sweden': 'Schweden', 'France': 'Frankreich', 'Italy': 'Italien'}

fobj = open("output.txt", "w") # kills everthing in it! create files if not found

for word in dictCountries:
    fobj.write("{} {}\n".format(word, dictCountries[word]))

fobj.close()