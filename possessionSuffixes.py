import letterDefinitions

def PossessionSuffixes(word):
    lastword = word[-1]
    lastthreewords = word[-3:]
    lasttwowords= word[-2:]


    # print(lastword)
    if lastword in letterDefinitions.possessionWords1:
        word = word[:1]


    elif lastthreewords in letterDefinitions.possessionWords2:
        word = word[:-3]

    elif lasttwowords in letterDefinitions.possessionWords5:
        word = word[:-2]
        index= letterDefinitions.possessionword6.index(word[-1])
        word= word.replace(word[-1], letterDefinitions.sixthLetter[index])


    elif lastword in letterDefinitions.possessionWord3:
        index = letterDefinitions.possessionWord3.index(word[-1])
        word = word.replace(word[-1], letterDefinitions.sixthLetter[index])
            

    elif lastword in letterDefinitions.possessionWords4:
        index1 = letterDefinitions.possessionWords4.index(word[-1])
        word = word.replace(word[-1], letterDefinitions.sixthLetter[index1])
            
    return word
