possessionWords1 = ["ዋ", "ኤ", "ህ ", "ሽ"]
possessionWords2 = ["አችን", "አቸው"]
possessionWord3 = ["ሁ", "ሉ", "ሑ", "ሙ", "ሡ", "ሩ", "ሱ", "ሹ", "ቁ", "ቡ", "ቱ", "ቹ", "ኁ", "ኑ", "ኙ",
                    "ኡ", "ኩ", "ኹ", "ዉ", "ዑ", "ዙ", "ዡ", "ዩ", "ዱ", "ጁ", "ጉ", "ጡ", "ጩ", "ጱ", "ጹ", "ፁ", "ፉ", "ፑ"]
possessionWords4 =["ሄ", "ሌ", "ሔ", "ሜ", "ሤ", "ሬ", "ሴ", "ሼ", "ቄ", "ቤ", "ቴ", "ቼ", "ኄ", "ኔ", "ኜ",
                    "ኤ", "ኬ", "ኼ", "ዌ", "ዔ", "ዜ", "ዤ", "ዬ", "ዴ", "ጄ", "ጌ", "ጤ", "ጬ", "ጴ", "ጼ", "ፄ", "ፌ", "ፔ"]
possessionword6 =["ሃ", "ላ", "ሓ", "ማ", "ሣ", "ራ", "ሳ", "ሻ", "ባ", "ቫ", "ታ", "ቻ", "ኃ", "ና", "ኛ", "ኣ", "ካ", "ኻ", "ዋ", "ዓ", "ዛ",
                  "ዣ", "ያ", "ዳ", "ጃ", "ጋ", "ጣ", "ጫ", "ጳ", "ጻ", "ፃ", "ፋ", "ፓ"]
possessionWords5=["ችን"]

replacement =     ["ህ", "ል", "ሕ", "ም", "ሥ", "ር", "ስ", "ሽ", "ቅ", "ብ", "ቭ", "ት", "ች", "ኅ", "ን", "ኝ",
                    "እ", "ክ", "ኽ", "ው", "ዕ", "ዝ", "ዥ", "ይ", "ድ", "ጅ", "ግ", "ጥ", "ጭ", "ጵ", "ጽ", "ፅ", "ፍ", "ፕ"]

# word = input("ቃላትን ያስገቡ፡ ")
word = "ደብተራችን"
i = 0
lastword = word[-1]
values = range(31)
lastthreewords = word[-3:]
lasttwowords= word[-2:]


# print(lastword)
if lastword in possessionWords1:
    word = word[:1]
    print(word)

elif lastthreewords in possessionWords2:
    word = word[:-3]
    print(word)
elif lasttwowords in possessionWords5:
    word = word[:-2]
    index= possessionword6.index(word[-1])
    word= word.replace(word[-1], replacement[index])
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
