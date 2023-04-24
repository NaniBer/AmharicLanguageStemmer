import letterDefinitions


def PrepositionSuffix(word):
    FirstcharOne = word[0]
    firstTwoChar = word[:2]
    if (word not in letterDefinitions.pluralWords):

        if (FirstcharOne in letterDefinitions.prepositionSuffixes or firstTwoChar in letterDefinitions.prepositionSuffixes):
            if FirstcharOne in letterDefinitions.prepositionSuffixes:
                word = word[1:]
            else:
                word = word[2:]
    elif (word in letterDefinitions.pluralWords):
        index = letterDefinitions.pluralWords.index(word)
        word = letterDefinitions.singleWords[index]

    return word
