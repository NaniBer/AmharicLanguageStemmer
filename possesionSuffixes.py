possesionWords1= ["ዋ", "ኤ", "ህ ", "ሽ"]
possesionWords2= ["አችን", "አቸው"]

possesionWord3= ["ሁ", "ሉ", "ሑ", "ሙ", "ሡ", "ሩ","ሱ","ሹ", "ቁ" , "ቡ", "ቱ", "ቹ", "ኁ", "ኑ", 
                 "ኡ","ኩ","ኹ", "ዉ", "ዑ", "ዙ", "ዡ","ዩ","ዱ", "ጁ","ጉ", "ጡ", "ጩ", "ጱ", "ፁ", "ፉ", "ፑ"]

possesionWords4= ["ሄ", "ሌ", "ሔ", "ሜ", "ሤ","ሬ", "ሴ", "ሼ", "ቄ", "ቤ", "ቬ", "ቴ", "ቼ","ኄ","ኔ","ኜ","ኤ","ኬ","ኼ","ዌ","ዔ",
                 "ዜ","ዤ","ዬ","ዴ","ጄ","ጌ","ጤ","ጬ","ጴ","ጼ","ፄ","ፌ","ፔ"]

replacement= ["ህ", "ል", "ሕ", "ም", "ሥ", "ር", "ስ", "ሽ", "ቅ", "ብ", "ቭ", "ት", "ች", "ኅ", "ን", "ኝ", "እ", 
                  "ክ", "ኽ", "ዕ", "ዝ", "ዥ", "ይ", "ድ", "ጅ", "ግ", "ጥ", "ጭ", "ጵ", "ፅ", "ፍ", "ፕ"]

# word = input("ቃላትን ያስገቡ፡ ")
word= "እርሳሴ"
i=0   
lastword = word[-1] 
values= range(31)
lastthreewords= word[-3:]

# print(lastword)
if lastword in possesionWords1:
 word= word[:1] 
 print (word)

elif lastthreewords in possesionWords2:
 word= word[:-3]
 print(word)

elif lastword in possesionWord3 :
  for i in values:
    index= possesionWord3.index(word[-1])
    word= word.replace(word[-1], replacement[index] )
    print(word)
        
    
elif lastword in possesionWords4:
      for i in values:
       index1= possesionWords4.index(word[-1])
       word= word.replace(word[-1], replacement[index1])
       print(word)
else:
  print(word)

      
 

 

