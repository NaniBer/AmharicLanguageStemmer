import letterDefinitions
def GenderSuffixes(word):
    lastcharOne = word[-1]
    if(lastcharOne=="ች"):
        word=word[:-1]

    elif(lastcharOne in letterDefinitions.femaleGenderLetters or lastcharOne in letterDefinitions.secondLetter):
        if(lastcharOne in letterDefinitions.femaleGenderLetters):
            index= letterDefinitions.femaleGenderLetters.index(lastcharOne)
        else:
            index= letterDefinitions.secondLetter.index(lastcharOne)
        
        word=word[:-1]
        word+=letterDefinitions.sixthLetter[index]
        
    return word

