import possessionSuffixes
import prepositionSuffixes
import genderSuffixes
import pluralSuffixes
import dictionary
import miscallenous
import writersNames

# word = input("ቃላትን ያስገቡ፡ ")

# word = "የተደረሰ"


def stemmerMain(word):
    # Check if the word is a stem word or author's first name

    while (word not in dictionary.stemWord and word not in writersNames.writers[0]):

        lastcharOne = word[-1]
        lastcharTwo = word[-2:]

        # Steps Preposition -> possesion -> gender -> plural
        word = miscallenous.Mis(word)
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

    print(word)
    return word
