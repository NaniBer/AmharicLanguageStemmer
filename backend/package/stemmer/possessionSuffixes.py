from .letterDefinitions import femaleGenderLetters
from .letterDefinitions import seventhLetter
from .letterDefinitions import sixthLetter
from .letterDefinitions import fifthLetter
from .letterDefinitions import fourthLetter
from .letterDefinitions import secondLetter
from .letterDefinitions import prepositionSuffixes
from .letterDefinitions import exceptionWords
from .letterDefinitions import singleWords
from .letterDefinitions import pluralWords
from .letterDefinitions import pluralSuffixesOne
from .letterDefinitions import pluralSuffixesTwo
from .letterDefinitions import possessionWords1
from .letterDefinitions import possessionWords2
from .letterDefinitions import possessionWord3
from .letterDefinitions import possessionWords4
from .letterDefinitions import possessionWords5
from .letterDefinitions import possessionword6
from .letterDefinitions import mis


mis = ["የው", "የዋ", "ዊ", "ነት", "ና"]


def PossessionSuffixes(word):
    if (word not in pluralWords):
        lastword = word[-1]
        lastthreewords = word[-3:]
        lasttwowords = word[-2:]

        if (len(word) > 3):
            lastthirdletter = word[-3]
        else:
            lastthirdletter = ""

        if lastword in possessionWords1 and lasttwowords not in possessionWords5:

            word = word[:-1]

        elif lastthreewords in possessionWords2:

            word = word[:-3]

        elif lasttwowords in possessionWords5:

            if (lastthirdletter in femaleGenderLetters):
                word = word[:-2]
                index = femaleGenderLetters.index(word[-1])
                word = word.replace(
                    word[-1], sixthLetter[index])
            elif (word[-1] in fourthLetter or lastthirdletter in fourthLetter):
                word = word[:-2]
                index = fourthLetter.index(word[-1])
                word = word.replace(
                    word[-1], sixthLetter[index])

        elif lastword in secondLetter:
            index = secondLetter.index(word[-1])
            word = word.replace(word[-1], sixthLetter[index])

        elif lastword in fifthLetter:
            index1 = fifthLetter.index(word[-1])
            word = word.replace(
                word[-1], sixthLetter[index1])
    elif (word in pluralWords):
        index = pluralWords.index(word)
        word = singleWords[index]

    return word
