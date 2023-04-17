import stemmerMain
import writersNames

# sentence = input("ቃላትን ያስገቡ፡ ")
sentence = "የተደረሰ በይስማዕከ ወርቁ መጽሐፎች"
words = sentence.split()
queryList = []
len = len(words)
i = 0
while (i < len):
    word = words[i]
    if (word not in writersNames.writers[0]):
        word = stemmerMain.stemmerMain(word)
        queryList.append(word)
        if (word in writersNames.writers[0]):
            for item in writersNames.writers:
                if (i < len-1):
                    if (words[i+1] in item[1]):
                        queryList.append(words[i+1])
                        i = i+1
                    else:
                        continue

    i = i+1


print(queryList)
