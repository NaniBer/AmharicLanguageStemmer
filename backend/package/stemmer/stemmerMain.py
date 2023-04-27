from .possessionSuffixes import PossessionSuffixes
from .prepositionSuffixes import PrepositionSuffix
from .genderSuffixes import GenderSuffixes
from .pluralSuffixes import PluralSuffixes
from .dictionary import stemWord
from .miscallenous import Mis
from .writersNames import writers


def stemmerMain(word):
    # Check if the word is a stem word or author's first name
    i = 0
    if (word not in writers[0]):

        while (word not in stemWord and word not in writers[0] and i < 3):

            lastcharOne = word[-1]
            lastcharTwo = word[-2:]

            # Steps Preposition -> possesion -> gender -> plural

            word = Mis(word)
            if (word in stemWord):
                break
            word = PossessionSuffixes(word)
            if (word in stemWord):
                break
            word = GenderSuffixes(word)
            if (word in stemWord):
                break
            word = PluralSuffixes(word)
            if (word in stemWord):
                break
            word = PrepositionSuffix(word)
            if (word in stemWord):
                break
            i = i+1

    return word
