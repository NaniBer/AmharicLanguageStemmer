import letterDefinitions


def Mis(word):
    lastcharOne = word[-1]
    lastcharTwo = word[-2:]
    if (word not in letterDefinitions.pluralWords):
        if (lastcharOne in letterDefinitions.mis and word[-2] in letterDefinitions.fourthLetter):
            index = letterDefinitions.fourthLetter.index(word[-2])
            word = word[:-2]
            word += letterDefinitions.sixthLetter[index]
        elif (lastcharTwo in letterDefinitions.mis):
            word = word[:-2]
    elif (word in letterDefinitions.pluralWords):
        index = letterDefinitions.pluralWords.index(word)
        word = letterDefinitions.singleWords[index]

    return word
