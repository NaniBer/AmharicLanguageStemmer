word = input("ቃላትን ያስገቡ፡ ")
FirstcharOne = word[0]
# print(FirstcharOne)
prepositionSuffixes = ["የ", "በ", "ከ", "ለ"]
if FirstcharOne in prepositionSuffixes:
    word = word[1:]
    print(word)
else:
    print(word)
