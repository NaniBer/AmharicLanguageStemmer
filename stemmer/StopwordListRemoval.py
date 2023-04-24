import stemmerMain
import writersNames
StopWords = [
    "ስለሚሆን", "አና", "ስለዚህ", "በመሆኑም", "ሁሉ", "ሆነ", "ሌላ", "ልክ", "ስለ", "በቀር", "ብቻ", "ና", "አንዳች", "አንድ",
    "እንደ", "እንጂ", "ያህል", "ይልቅ", "ወደ", "እኔ", "የእኔ", "ራሴ", "እኛ",  "የእኛ",  "እራሳችን", "አንቺ",  "የእርስዎ",
    "ራስህ", "ራሳችሁ", "እሱ", "እሱን", "የእሱ", "ራሱ",  "እርሷ",  "የእሷ",  "ራሷ",  "እነሱ",  "እነሱን",  "የእነሱ",
    "እራሳቸው", "ምንድን",  "የትኛው", "ማንን", "ይህ",  "እነዚህ",  "እነዚያ",  "ነኝ",  "ነው",  "ናቸው",  "ነበር",
    "ነበሩ", "ሁን", "ነበር",  "መሆን",  "አለኝ",  "አለው",  "ነበረ",  "መኖር",  "ያደርጋል",  "አደረገው",  "መሥራት",  "እና", "ግን",  "ከሆነ",  "ወይም",
    "ምክንያቱም", "እንደ", "እስከ", "ቢሆንም", "ጋር", "ላይ", "መካከል", "በኩል", "ወቅት",  "በኋላ",  "ከላይ", "በርቷል", "ጠፍቷል", "በላይ", "ስር", "እንደገና", "ተጨማሪ",
    "ከዚያ", "አንዴ", "እዚህ", "እዚያ", "መቼ", "የት", "እንዴት", "ሁሉም", "ማናቸውም", "ሁለቱም", "እያንዳንዱ", "ጥቂቶች",
    "ተጨማሪ", "በጣም", "ሌላ", "አንዳንድ", "አይ", "ወይም", "አይደለም", "ብቻ", "የራስ", "ተመሳሳይ", "ስለዚህ", "እኔም",
    "በጣም", "ይችላል", "ይሆናል", "በቃ", "አሁን", "በተጨማሪም", "ሆነው", "ሲሆን", "በተለያዩ", "ይታወቃሉ", "ተለያዩ", "ቆይተዋል", "እያገለግሉ"  # check እያገለግሉ
]
# def RemoveStopWord():
# print("enter a sentence ")
# text = input()
# texts = text.split()

index = []
finalIndex = []

f = open("C:/Users/ASUS/Documents/Projects/Stemmer/AmharicLanguageStemmer/Authors/ኃይሉ ገብረዮሐንስ.txt", "r", encoding="utf8")
a = f.read()
f.close

texts = a.split()
word = texts[0]
word = word[1:]
index.append(word)
print(index)
len = len(texts)
i = 1


while (i < len):
    word = texts[i]
    if word not in StopWords:
        index.append(word)

    i = i+1

for word in index:
    if (word[0] == "“"):
        finalIndex.append(word)
    elif (word[-1] == "”"):
        finalIndex.append(word)
    else:
        word = stemmerMain.stemmerMain(word)
        finalIndex.append(word)


print(finalIndex)
