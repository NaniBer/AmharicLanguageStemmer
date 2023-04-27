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


def GenderSuffixes(word):
    lastcharOne = word[-1]
    if (word not in pluralWords):

        if (lastcharOne == "ች" and word[-2] not in seventhLetter):
            word = word[:-1]

        elif (lastcharOne in femaleGenderLetters or lastcharOne in secondLetter):
            if (lastcharOne in femaleGenderLetters):

                index = femaleGenderLetters.index(
                    lastcharOne)
            else:
                index = secondLetter.index(lastcharOne)

            word = word[:-1]
            word += sixthLetter[index]

    elif (word in pluralWords):
        index = pluralWords.index(word)
        word = singleWords[index]

    return word
