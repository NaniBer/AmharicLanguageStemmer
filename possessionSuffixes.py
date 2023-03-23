possessionWords1 = ["ዋ", "ኤ", "ህ ", "ሽ"]
possessionWords2 = ["አችን", "አቸው"]
possessionWord3 = ["ሁ", "ሉ", "ሑ", "ሙ", "ሡ", "ሩ", "ሱ", "ሹ", "ቁ", "ቡ", "ቱ", "ቹ", "ኁ", "ኑ", "ኙ",
                    "ኡ", "ኩ", "ኹ", "ዉ", "ዑ", "ዙ", "ዡ", "ዩ", "ዱ", "ጁ", "ጉ", "ጡ", "ጩ", "ጱ", "ጹ", "ፁ", "ፉ", "ፑ"]
possessionWords4 =["ሄ", "ሌ", "ሔ", "ሜ", "ሤ", "ሬ", "ሴ", "ሼ", "ቄ", "ቤ", "ቴ", "ቼ", "ኄ", "ኔ", "ኜ",
                    "ኤ", "ኬ", "ኼ", "ዌ", "ዔ", "ዜ", "ዤ", "ዬ", "ዴ", "ጄ", "ጌ", "ጤ", "ጬ", "ጴ", "ጼ", "ፄ", "ፌ", "ፔ"]
replacement =     ["ህ", "ል", "ሕ", "ም", "ሥ", "ር", "ስ", "ሽ", "ቅ", "ብ", "ቭ", "ት", "ች", "ኅ", "ን", "ኝ",
                    "እ", "ክ", "ኽ", "ው", "ዕ", "ዝ", "ዥ", "ይ", "ድ", "ጅ", "ግ", "ጥ", "ጭ", "ጵ", "ጽ", "ፅ", "ፍ", "ፕ"]

# word = input("ቃላትን ያስገቡ፡ ")
word = "እርሳሴ"
i = 0
lastword = word[-1]
values = range(31)
lastthreewords = word[-3:]

# print(lastword)
if lastword in possessionWords1:
    word = word[:1]
    print(word)

elif lastthreewords in possessionWords2:
    word = word[:-3]
    print(word)

elif lastword in possessionWord3:
    for i in values:
        index = possessionWord3.index(word[-1])
        word = word.replace(word[-1], replacement[index])
        print(word)


elif lastword in possessionWords4:
    for i in values:
        index1 = possessionWords4.index(word[-1])
        word = word.replace(word[-1], replacement[index1])
        print(word)
else:
    print(word)
