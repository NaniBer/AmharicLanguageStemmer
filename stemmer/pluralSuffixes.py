import letterDefinitions


def PluralSuffixes(word):
    lastcharOne = word[-1]
    lastcharTwo = word[-2:]

    if (word not in letterDefinitions.pluralWords):
        if (lastcharOne in letterDefinitions.pluralSuffixesOne):  # if the last letter has ች
            if lastcharTwo in letterDefinitions.pluralSuffixesTwo:  # if the last two letters are in the array
                word = word[:-2]
            else:
                if (word[-2] in letterDefinitions.seventhLetter):
                    index = letterDefinitions.seventhLetter.index(word[-2])
                    word = word[:-2]
                    word += letterDefinitions.sixthLetter[index]
                elif (word[-2] in letterDefinitions.fourthLetter):
                    index = letterDefinitions.fourthLetter.index(word[-2])
                    word = word[:-2]
                    word += letterDefinitions.sixthLetter[index]
                else:
                    word = word[:-1]

        elif lastcharTwo in letterDefinitions.pluralSuffixesTwo:
            word = word[:-2]
    elif (word in letterDefinitions.pluralWords):
        index = letterDefinitions.pluralWords.index(word)
        word = letterDefinitions.singleWords[index]

    return word


print(PluralSuffixes("ከአባቱ"))
