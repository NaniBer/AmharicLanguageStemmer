word = input("ቃላትን ያስገቡ፡ ")
FirstcharOne = word[0]
    # print(FirstcharOne)
possesionSuffixes = ["የ", "በ", "ከ"]
if FirstcharOne in possesionSuffixes:
     word = word[1:]
     print(word)
else:
     print(word)