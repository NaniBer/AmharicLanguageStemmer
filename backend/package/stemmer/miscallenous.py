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


def Mis(word):
    lastcharOne = word[-1]
    lastcharTwo = word[-2:]
    if (word not in pluralWords):
        if (lastcharOne in mis and word[-2] in fourthLetter):
            index = fourthLetter.index(word[-2])
            word = word[:-2]
            word += sixthLetter[index]
        elif (lastcharTwo in mis):
            word = word[:-2]
        if (lastcharOne in mis):
            word = word[:-1]
    elif (word in pluralWords):
        index = pluralWords.index(word)
        word = singleWords[index]

    return word
