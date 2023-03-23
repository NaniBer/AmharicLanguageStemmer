import possessionSuffixes
import prepositionSuffixes
import genderSuffixes
import pluralSuffixes



word = input("ቃላትን ያስገቡ፡ ")

lastcharOne = word[-1]
lastcharTwo = word[-2:]

#Steps Preposition -> possesion -> gender -> plural
word=prepositionSuffixes.PrepositionSuffix(word)
word=possessionSuffixes.PossessionSuffixes(word)
word=genderSuffixes.GenderSuffixes(word)
word=pluralSuffixes.PluralSuffixes(word)


print(word)



