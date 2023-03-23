word = input("ቃላትን ያስገቡ፡ ")
lastcharOne = word[-1]
lastcharTwo = word[-2:]

sixthLetter=["ህ", "ል", "ሕ", "ም", "ሥ", "ር", "ስ", "ሽ", "ቅ", "ብ", "ቭ", "ት", "ች", "ኅ", "ን", "ኝ", "እ", "ክ", "ኽ", "ው", "ዕ", "ዝ", "ዥ", "ይ", "ድ", "ጅ", "ግ", "ጥ", "ጭ", "ጵ", "ጽ", "ፅ", "ፍ", "ፕ"]
femaleGenderLetters=["", "ሏ", "ሗ", "ሟ", "ሧ", "ሯ", "ሷ", "ሿ", "ቋ", "ቧ", "ቯ", "ቷ", "ቿ", "ኋ", "ኗ", "ኟ", "ኧ", "ኳ", "ዃ", "","", "ዟ", "ዧ", "","ዷ","ጇ", "ጓ", "ጧ", "ጯ", "ጷ","ጿ","", "ፏ", "ፗ","ች"]
maleGenderLetters=["ሁ","ሉ", "ሑ", "ሙ", "ሡ", "ሩ", "ሱ", "ሹ", "ቁ", "ቡ", "ቩ","ቱ", "ቹ", "ኁ", "ኑ", "ኙ","ኡ","ኩ","ኹ", "ዉ", "ዑ", "ዙ","ዡ","ዩ","ዱ","ጁ","ጉ","ጡ","ጩ", "ጱ","ጹ","ፁ","ፉ","ፑ"]


if(lastcharOne=="ች"):
    word=word[:-1]

elif(lastcharOne in femaleGenderLetters or lastcharOne in maleGenderLetters):
    if(lastcharOne in femaleGenderLetters):
        index= femaleGenderLetters.index(lastcharOne)
    else:
        index= maleGenderLetters.index(lastcharOne)
    
    word=word[:-1]
    word+=sixthLetter[index]
    

print(word)

