import letterDefinitions


def GenderSuffixes(word):
    lastcharOne = word[-1]
    if (word not in letterDefinitions.pluralWords):

        if (lastcharOne == "ች" and word[-2] not in letterDefinitions.seventhLetter):
            word = word[:-1]

        elif (lastcharOne in letterDefinitions.femaleGenderLetters or lastcharOne in letterDefinitions.secondLetter):
            if (lastcharOne in letterDefinitions.femaleGenderLetters):

                index = letterDefinitions.femaleGenderLetters.index(
                    lastcharOne)
            else:
                index = letterDefinitions.secondLetter.index(lastcharOne)

            word = word[:-1]
            word += letterDefinitions.sixthLetter[index]

    elif (word in letterDefinitions.pluralWords):
        index = letterDefinitions.pluralWords.index(word)
        word = letterDefinitions.singleWords[index]

    return word
