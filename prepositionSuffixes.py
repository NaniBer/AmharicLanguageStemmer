import letterDefinitions
def PrepositionSuffix(word):
    FirstcharOne = word[0]
    firstTwoChar=word[:2]
    print(firstTwoChar)
    # print(FirstcharOne)
    
    if FirstcharOne in letterDefinitions.prepositionSuffixes:
        word = word[1:]
        print(word)
    else:
        print(word)
    return word