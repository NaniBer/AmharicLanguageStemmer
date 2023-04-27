import stemmerMain
import writersNames
import tf
import idf
import searchQuery
import ranking

# sentence = input("ቃላትን ያስገቡ፡ ")
sentence = "የተደረሰ በይስማዕከ መጽሐፎች"
sentence2 = "ጥቁር ሀዘን ጨለማም ቀለም"

words = sentence2.split()
queryList = []
len = len(words)
i = 0
values = {}
sorted_dict = {}
while (i < len):
    word = words[i]
    if (word not in writersNames.writers[0]):
        word = stemmerMain.stemmerMain(word)
        queryList.append(word)
        if (word in writersNames.writers[0]):
            for item in writersNames.writers:
                if (i < len-2):
                    if (words[i+1] in item[1]):
                        queryList.append(words[i+1])
                        i = i+1
                    else:
                        continue

    i = i+1
relatedBooks = searchQuery.searchQuery(queryList)
ranking.ranking(queryList, relatedBooks)
