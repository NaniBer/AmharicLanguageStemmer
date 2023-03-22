word = input("ቃላትን ያስገቡ፡ ")
lastcharOne = word[-1]
lastcharTwo = word[-2:]

seventhLetter=["ሆ","ሎ", "ሖ","ሞ","ሦ", "ሮ","ሶ", "ሾ" ,"ቆ", "ቦ", "ቮ", "ቶ", "ቾ", "ኆ", "ኖ", "ኞ", "ኦ", "ኮ", "ኾ", "ዎ", "ዖ", "ዞ", "ዦ", "ዮ", "ዶ", "ጆ", "ጎ", "ጦ", "ጮ", "ጶ", "ጾ", "ፆ", "ፎ", "ፖ"]
sixthLetter=["ህ", "ል", "ሕ", "ም", "ሥ", "ር", "ስ", "ሽ", "ቅ", "ብ", "ቭ", "ት", "ች", "ኅ", "ን", "ኝ", "እ", "ክ", "ኽ", "ው", "ዕ", "ዝ", "ዥ", "ይ", "ድ", "ጅ", "ግ", "ጥ", "ጭ", "ጵ", "ጽ", "ፅ", "ፍ", "ፕ"]
fifthLetter=["ሃ", "ላ", "ሓ", "ማ", "ሣ", "ራ", "ሳ", "ሻ", "ቃ", "ባ", "ቫ", "ታ", "ቻ", "ኃ", "ና", "ኛ", "ኣ", "ካ", "ኻ", "ዋ", "ዓ", "ዛ", "ዣ", "ያ", "ዳ", "ጃ", "ጋ", "ጣ", "ጫ", "ጳ", "ጻ", "ፃ", "ፋ", "ፓ"]

exceptionWords=["መአት"]
singleWords=["መነኩሴ", "ሀገር", "ርእስ", "ህዝብ", "ድንግል", "ቄስ", "ሊቅ", "እንብሳ", "ንጉስ", "ድብር", "ሃዋርያ", "ዳቦ", "መሮ", "ጌታ"]
pluralWords=["መነኮሳት", "አህጉር", "አርእስት", "አህዛብ", "ደናግል", "ቀሳውስት", "ሊቃውንት", "እናብስት", "ነገስታት", "እድባራት", "ሃዋርያት", "ዳቦች", "መሮች", "ጌቶች"] 

pluralSuffixesTwo = ["አት", "ኦች", "ዎች"]

pluralSuffixesOne = ["ች","ት","ን"]

if word not in exceptionWords:
    if(word not in pluralWords):
        if (lastcharOne in pluralSuffixesOne): #if the last letter has ች
            if lastcharTwo in pluralSuffixesTwo: #if the last two letters are in the array
                word = word[:-2]
            else:
                if(word[-2] in seventhLetter):
                    index=seventhLetter.index(word[-2])
                    word=word[:-2]
                    word+=sixthLetter[index]
                elif (word[-2]in fifthLetter):
                    index=fifthLetter.index(word[-2])
                    word=word[:-2]
                    word+=sixthLetter[index]
                else:           
                    word = word[:-1]

        elif lastcharTwo in pluralSuffixesTwo:
            word = word[:-2]
    elif(word in pluralWords):
        index=pluralWords.index(word)
        word=singleWords[index]


print(word)


