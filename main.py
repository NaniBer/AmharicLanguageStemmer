import possessionSuffixes
import prepositionSuffixes
import genderSuffixes
import pluralSuffixes
import dictionary


# word = input("ቃላትን ያስገቡ፡ ")

word = "በየምክንያቶች"


# Check if the word is a stem word


while word not in dictionary.stemWord:

    lastcharOne = word[-1]
    lastcharTwo = word[-2:]

#     # Steps Preposition -> possesion -> gender -> plural

    word = possessionSuffixes.PossessionSuffixes(word)
    print(word)
    if (word in dictionary.stemWord):
        break
    word = genderSuffixes.GenderSuffixes(word)
    print(word)
    if (word in dictionary.stemWord):
        break
    word = pluralSuffixes.PluralSuffixes(word)
    print(word)
    if (word in dictionary.stemWord):
        break
    word = prepositionSuffixes.PrepositionSuffix(word)


print(word)
