import letterDefinitions


def PossessionSuffixes(word):
    if (word not in letterDefinitions.pluralWords):
        lastword = word[-1]
        lastthreewords = word[-3:]
        lasttwowords = word[-2:]

        if (len(word) > 3):
            lastthirdletter = word[-3]
        else:
            lastthirdletter = ""

        if lastword in letterDefinitions.possessionWords1 and lasttwowords not in letterDefinitions.possessionWords5:

            word = word[:-1]

        elif lastthreewords in letterDefinitions.possessionWords2:

            word = word[:-3]

        elif lasttwowords in letterDefinitions.possessionWords5:

            if (lastthirdletter in letterDefinitions.femaleGenderLetters):
                word = word[:-2]
                index = letterDefinitions.femaleGenderLetters.index(word[-1])
                word = word.replace(
                    word[-1], letterDefinitions.sixthLetter[index])
            elif (word[-1] in letterDefinitions.fourthLetter or lastthirdletter in letterDefinitions.fourthLetter):
                word = word[:-2]
                index = letterDefinitions.fourthLetter.index(word[-1])
                word = word.replace(
                    word[-1], letterDefinitions.sixthLetter[index])

        elif lastword in letterDefinitions.secondLetter:
            index = letterDefinitions.secondLetter.index(word[-1])
            word = word.replace(word[-1], letterDefinitions.sixthLetter[index])

        elif lastword in letterDefinitions.possessionWords4:
            index1 = letterDefinitions.possessionWords4.index(word[-1])
            word = word.replace(
                word[-1], letterDefinitions.sixthLetter[index1])
    elif (word in letterDefinitions.pluralWords):
        index = letterDefinitions.pluralWords.index(word)
        word = letterDefinitions.singleWords[index]

    return word
