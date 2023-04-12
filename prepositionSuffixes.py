import letterDefinitions
def PrepositionSuffix(word):
    FirstcharOne = word[0]
    firstTwoChar=word[:2]

    
    if (FirstcharOne in letterDefinitions.prepositionSuffixes or firstTwoChar in letterDefinitions.prepositionSuffixes):
        if FirstcharOne in letterDefinitions.prepositionSuffixes:
            word = word[1:]
        else: 
            word = word[2:]
            
    
    return word