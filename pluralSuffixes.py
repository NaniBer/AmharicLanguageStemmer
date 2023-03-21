word = input("ቃላትን ያስገቡ፡ ")
lastcharOne = word[-1]
lastcharTwo = word[-2:]

pluralSuffixesTwo = ["አት", "ኦች", "ዎች"]
pluralSuffixesOne = "ች"


if lastcharOne == pluralSuffixesOne:
    if lastcharTwo in pluralSuffixesTwo:
        word = word[:-2]
    else:
        word = word[:-1]

elif lastcharTwo in pluralSuffixesTwo:
    word = word[:-2]


print(word)
