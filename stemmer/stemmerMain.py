import possessionSuffixes
import prepositionSuffixes
import genderSuffixes
import pluralSuffixes
import dictionary
import miscallenous
import writersNames


def stemmerMain(word):
    # Check if the word is a stem word or author's first name
    i = 0
    if (word not in writersNames.writers[0]):

        while (word not in dictionary.stemWord and word not in writersNames.writers[0] and i < 3):

            lastcharOne = word[-1]
            lastcharTwo = word[-2:]

            # Steps Preposition -> possesion -> gender -> plural

            word = miscallenous.Mis(word)
            if (word in dictionary.stemWord):
                break
            word = possessionSuffixes.PossessionSuffixes(word)
            if (word in dictionary.stemWord):
                break
            word = genderSuffixes.GenderSuffixes(word)
            if (word in dictionary.stemWord):
                break
            word = pluralSuffixes.PluralSuffixes(word)
            if (word in dictionary.stemWord):
                break
            word = prepositionSuffixes.PrepositionSuffix(word)
            if (word in dictionary.stemWord):
                break
            i = i+1

    return word


print(stemmerMain("በታሪክ"))
