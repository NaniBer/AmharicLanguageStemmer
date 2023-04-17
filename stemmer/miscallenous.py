import letterDefinitions


def Mis(word):
    lastcharOne = word[-1]
    lastcharTwo = word[-2:]

    if (lastcharTwo in letterDefinitions.mis):
        word = word[:-2]
    return word
